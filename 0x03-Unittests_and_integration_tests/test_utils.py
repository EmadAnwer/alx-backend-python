#!/usr/bin/env python3

import unittest
from fastapi import param_functions
from parameterized import parameterized
import utils
from unittest.mock import MagicMock, Mock, patch


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
    """Class for Testing Get Json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """Test that utils.get_json returns the expected result."""
        config = {"return_value.json.return_value": test_payload}
        patcher = patch("requests.get", **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


if __name__ == "__main__":
    unittest.main()
