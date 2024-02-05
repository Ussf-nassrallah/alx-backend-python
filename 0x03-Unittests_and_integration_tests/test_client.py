#!/usr/bin/env python3
''' test client module '''

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        ''' test public repos method '''
        test_cases = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }

        mock_get_json.return_value = test_cases["repos"]
        patch_pub_repos = "client.GithubOrgClient._public_repos_url"

        with patch(
            patch_pub_repos,
            new_callable=PropertyMock
        ) as mock_pub_repos:
            mock_pub_repos.return_value = test_cases["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ["episodes.dart", "kratu"]
            )
            mock_pub_repos.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "bsd-3-clause"}}, "bsd-3-clause", True),
        ({"license": {"key": "bsl-1.0"}}, "bsl-1.011", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        ''' test has_license method '''
        self.assertEqual(
            GithubOrgClient('google').has_license(repo, license_key),
            expected
        )
