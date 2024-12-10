import unittest
import unittest.mock
from unittest.mock import Mock
import utils
from parameterized import parameterized, param

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        param("One", {"a": 1}, ("a",), expected=1),
        param("Dict", {"a": {"b": 2}}, ("a",), expected={"b": 2}),
        param("Two", {"a": {"b": 2}}, ("a", "b"), expected=2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({"a": 1}, ('a','b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as err:
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        attrs = { "json.return_value": payload }
        with unittest.mock.patch("requests.get", return_value=Mock(**attrs)) as mock:
            ret = utils.get_json(url)
            mock.assert_called_once_with(url)
            self.assertEqual(ret, payload)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()


if __name__ == '__main__':
    unittest.main()
