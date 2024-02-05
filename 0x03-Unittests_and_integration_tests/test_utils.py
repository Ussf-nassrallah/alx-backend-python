#!/usr/bin/env python3
''' test_utils module '''

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    ''' TestAccessNestedMap class '''

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' test access_nested_map method '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        ''' test access_nested_map exception '''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' TestGetJson class '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_get_json):
        ''' test get_json method '''
        mock_res = MagicMock()
        mock_res.json.return_value = test_payload
        mock_get_json.get.return_value = mock_res

        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    ''' TestGetJson class '''

    def test_memoize(self) -> None:
        ''' Test memoize method '''

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=lambda: 42,
        ) as memo:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo.assert_called_once()
