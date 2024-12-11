#!/usr/bin/env python3
"""This file is for testing client.py method
"""

import utils
import client
from unittest import TestCase
from unittest.mock import PropertyMock, patch, Mock, MagicMock
from parameterized import parameterized, param, parameterized_class
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(TestCase):
    """This class tests the GithubOrgClient class and its methods
       to make sure all logic for memoization and caching results
       are working with no issues.

    Args:
        TestCase (unittest.TestCase): This is the base unittest class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mockedGetJson):
        """ This method tests org method of GithubOrgClient to make sure
            the result of that function is cached for the first request
            so that subsquent calls to org will return the cached version
            instead of making new api call to github API.

        Args:
            org_name (str)
                This is the name of the base origin repo for github

            mockedGetJson (Mock)
                This is a mocked version of get_json function to verify
                it is called only once regardless how many time org function
                is called.
        """
        mockedGetJson.return_value = MagicMock(return_value={"success": True})
        client_connection = client.GithubOrgClient(org_name)
        self.assertEqual(client_connection.org(), {"success": True})
        self.assertEqual(client_connection.org(), {"success": True})
        self.assertEqual(client_connection.org(), {"success": True})
        mockedGetJson.assert_called_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        mockedGetJson.assert_called_once()

    def test_public_repos_url(self):
        """ This function tests that the public repos url will return
            the property org which is actually a method but being memoized
            to be an attribute of the class GithubOrgClient.
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mocked_attribure:
            mocked_attribure.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                client.GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch(
        "client.get_json",
        return_value=[
            {
                "id": 8566972,
                "node_id": "MDEwOlJlcG9zaXRvcnk4NTY2OTcy",
                "name": "kratu",
                "full_name": "google/kratu",
                "private": False,
            },
            {
                "id": 9060347,
                "node_id": "MDEwOlJlcG9zaXRvcnk5MDYwMzQ3",
                "name": "traceur-compiler",
                "full_name": "google/traceur-compiler",
                "private": False,
            }
        ]
    )
    def test_public_repos(self, mockedGetJson):
        """ This method tests that the public_repos method is working
            as expected by getting all public_repos_url and make a
            request to github and return the names of the repos from the
            result of the request.

        Args:
            mockedGetJson (Mock)
                This is a mocked version of get request to.
        """
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/google/repos"
        ) as public_repos_url:

            repo = "https://api.github.com/orgs/google/repos"
            self.assertEqual(
                client.GithubOrgClient("google").public_repos(),
                ["kratu", "traceur-compiler"]
            )
            mockedGetJson.assert_called_once()
            mockedGetJson.assert_called_with(repo)
            public_repos_url.assert_called_once()

    @parameterized.expand([
        param(
            repo={"license": {"key": "my_license"}},
            license_key="my_license",
            res=True
        ),
        param(
            repo={"license": {"key": "other_license"}},
            license_key="my_license",
            res=False
        )
    ])
    def test_has_license(self, repo: str, license_key: str, res: bool):
        """ This function unit-test GithubOrgClient.has_license method

        Args:
            repo (str)
                This is the object of the repo to check if it has license
                or not

            license_key (str)
                This is the license key that authorize access to the given
                repo

            res (bool)
                This is a boolean flag indicating whether or not the given
                license key is exist in the repo license.
        """
        self.assertEqual(
            client.GithubOrgClient.has_license(repo, license_key),
            res
        )


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    },
])
class TestIntegrationGithubOrgClient(TestCase):
    """ Integeration testing for all features given in the GithubOrgClient
        class using test fixture and mocking abilities to make no external
        requests to API but to monkey patch them and make sure correct
        result are returned.

    Args:
        TestCase (unittest.TestCase)
            This is the base class for all tests.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """ Sets up class fixtures before running any test.
        """
        route_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload
        }

        def get_side_effect(url):
            if url in route_payload:
                return Mock(
                    **{"json.return_value": route_payload[url]}
                )
            return HTTPError
        cls.get_patcher = patch("requests.get", side_effect=get_side_effect)
        cls.get_patcher.start()

    def test_public_urls(self) -> None:
        """ Test that public repos will return the correct repos
        """
        self.assertEqual(
            client.GithubOrgClient("google").public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_apache_license(self) -> None:
        """ Test that public_repos will return repos with the given
            license
        """
        self.assertEqual(
            client.GithubOrgClient("google").public_repos("apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """ Stop the patcher after all tests are done and
            also remove all fixtures.
        """
        cls.get_patcher.stop()
