#!/usr/bin/env python3
"""Test for the clinet module"""
import unittest
from unittest.mock import PropertyMock, patch
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

    @patch("client.get_json")
    @patch(
        "client.GithubOrgClient._public_repos_url",
        new_callable=PropertyMock,
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """test public_repos using PropertyMock"""
        test_instance = GithubOrgClient("test")
        mock_public_repos_url.return_value = "www.test.com"
        repos_list = {"repos": ["r1", "r2", "r3", "...etc"]}
        mock_get_json.return_value = repos_list
        self.assertEqual(test_instance.repos_payload, repos_list)
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
