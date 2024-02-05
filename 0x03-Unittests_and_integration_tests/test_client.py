#!/usr/bin/env python3
"""Test for the clinet module"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """test GithubOrgClient class"""

    @parameterized.expand(
        [
            ("google", {"org": "google"}),
            ("abc", {"org": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, output, mock_get_json):
        """test that GithubOrgClient.org returns the correct value"""
        test_init = GithubOrgClient(org_name)
        mock_get_json.return_value = output
        self.assertEqual(output, test_init.org)
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
