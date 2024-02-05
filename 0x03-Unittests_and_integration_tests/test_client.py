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

    @patch('client.GithubOrgClient')
    def test_public_repos_url(self, mock_public_repos_url):
        ''' test _public_repos_url method '''
        test_input = 'google'
        expected_output = {
            'repos_url': "https://api.github.com/orgs/google/repos",
        }

        mock_res = MagicMock(return_value=expected_output)
        mock_res.get.return_value = mock_res
        self.assertEqual(
            GithubOrgClient(test_input)._public_repos_url,
            expected_output['repos_url']
        )
