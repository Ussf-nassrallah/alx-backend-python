#!/usr/bin/env python3
''' test client module '''

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    ''' test GithubOrgClient class '''

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org, expected, mock_org):
        ''' test org method '''
        mock_org.return_value = MagicMock(return_value=expected)
        test_client = GithubOrgClient(org)
        self.assertEqual(test_client.org(), expected)
        mock_org.assert_called_once_with(f"https://api.github.com/orgs/{org}")
