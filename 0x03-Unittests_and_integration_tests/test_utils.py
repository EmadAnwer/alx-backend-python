#!/usr/bin/env python3

import unittest
from fastapi import param_functions
from parameterized import parameterized
import utils
from unittest.mock import MagicMock, patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand(
        [
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, output) -> None:
        """test access_nested_map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, error):
        """test access_nested_map using invalid inputs"""
        with self.assertRaises(error):
            self.assertEqual(utils.access_nested_map(nested_map, path))

    class TestGetJson(unittest.TestCase):
        """TestGetJson class"""

        @parameterized.expand(
            [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False}),
            ]
        )
        @patch("utils.requests.get")
        def test_get_json(self, test_url, test_payload, mock_requests_get):
            """test get_json using by patching requests.get
            return test_payload
            """
            mock_response = mock_requests_get.return_value
            mock_response.json.return_value = test_payload
            get_json_value = utils.get_json(test_url, test_payload)
            self.assertDictEqual(get_json_value, test_payload)


if __name__ == "__main__":
    unittest.main()
