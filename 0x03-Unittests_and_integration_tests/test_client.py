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

    @patch("client.get_json")
    def test_public_repos_url(self, mock_get_json):
        """test client.get_json to check the _public_repos_url behavior"""
        test_init = GithubOrgClient("test")
        output = {"repos_url": "www.test.com"}
        mock_get_json.return_value = output
        self.assertEqual(test_init._public_repos_url, output["repos_url"])


if __name__ == "__main__":
    unittest.main()
