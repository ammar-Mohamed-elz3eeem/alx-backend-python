#!/usr/bin/env python3
""" This is a unit test module for testing all utils.
"""

import unittest
import unittest.mock
from unittest.mock import Mock
import utils
from parameterized import parameterized, param


class TestAccessNestedMap(unittest.TestCase):
    """ This is a class to test access_nested_map functionality.

    Args:
        unittest (unittest.TestCase)
            This is the base class for testing access_nested_map.
    """

    @parameterized.expand([
        param("One", {"a": 1}, ("a",), expected=1),
        param("Dict", {"a": {"b": 2}}, ("a",), expected={"b": 2}),
        param("Two", {"a": {"b": 2}}, ("a", "b"), expected=2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """ This is the method that tests the access_nested_map
            and checks that it returns the right data.

        Args:
            name (str)
                This is the name that the test case uses.

            nested_map (Dict)
                This is the map that we need to access.

            path (Tuple)
                This is the path to access in the nested_map.

            expected (Any)
                This is the result that should be returned when
                accessing the nested_map using the given path.
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({"a": 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ This is the method that tests the access_nested_map
            and checks that it raises an error in the given path.

        Args:
            nested_map (Dict)
                This is the map that we need to access.

            path (Tuple)
                This is the path to access in the nested_map.
        """
        with self.assertRaises(KeyError) as err:
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ This is a class to test get_json functionality.

    Args:
        unittest (unittest.TestCase)
            This is the base class for testing get_json().
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """ This method tests the get_json functionality and checks
            that the method has called the json method.

        Args:
            url (str)
                This is the url to send to get_json.

            payload (Dict)
                This is the payload response coming from the
                mocked get request.
        """
        attrs = {"json.return_value": payload}
        with unittest.mock.patch("requests.get",
                                 return_value=Mock(**attrs)) as mock:
            ret = utils.get_json(url)
            mock.assert_called_once_with(url)
            self.assertEqual(ret, payload)


class TestMemoize(unittest.TestCase):
    """ This is a class to test memoize functionality.

    Args:
        unittest (unittest.TestCase)
            This is the base class for testing memoize().
    """

    def test_memoize(self):
        """ This is a test case for the memoize function
        """
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()


if __name__ == '__main__':
    unittest.main()
