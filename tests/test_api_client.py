import unittest
from unittest.mock import patch, MagicMock
import json
import urllib.error
from activity_lab.api_client import GitHubApiClient


class TestGitHubApiClient(unittest.TestCase):
    def setUp(self):
        self.client = GitHubApiClient(token=None)

    def test_default_headers_without_token(self):
        headers = self.client._get_headers()
        self.assertEqual(headers["Accept"], "application/vnd.github+json")
        self.assertEqual(headers["User-Agent"], "github-activity-lab")
        self.assertNotIn("Authorization", headers)

    def test_headers_with_token(self):
        client = GitHubApiClient(token="ghp_testtoken")
        headers = client._get_headers()
        self.assertEqual(headers["Authorization"], "Bearer ghp_testtoken")
        self.assertEqual(headers["Accept"], "application/vnd.github+json")

    @patch("urllib.request.urlopen")
    def test_successful_json_response(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps({"id": 1, "name": "test"}).encode("utf-8")
        mock_resp.__enter__.return_value = mock_resp
        mock_urlopen.return_value = mock_resp

        result = self.client._request("https://api.github.com/repos/octocat/Hello-World")
        self.assertEqual(result, {"id": 1, "name": "test"})

    @patch("urllib.request.urlopen")
    def test_http_error_returns_error_structure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.HTTPError(
            url="https://api.github.com/repos/octocat/Hello-World",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )
        result = self.client._request("https://api.github.com/repos/octocat/Hello-World")
        self.assertIn("error", result)
        self.assertEqual(result["code"], 404)
        self.assertIn("404", result["error"])

    @patch("urllib.request.urlopen")
    def test_url_error_returns_error_structure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Network unreachable")
        result = self.client._request("https://api.github.com/repos/octocat/Hello-World")
        self.assertIn("error", result)
        self.assertNotIn("code", result)
        self.assertIn("Network unreachable", result["error"])

    @patch("urllib.request.urlopen")
    def test_custom_headers_respected(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.read.return_value = b'{"ok": true}'
        mock_resp.__enter__.return_value = mock_resp
        mock_urlopen.return_value = mock_resp

        custom = {"Accept": "application/vnd.github.star+json", "User-Agent": "custom"}
        self.client._request("https://api.github.com/test", custom_headers=custom)

        call_args = mock_urlopen.call_args
        request_obj = call_args[0][0]
        self.assertEqual(request_obj.headers["Accept"], "application/vnd.github.star+json")
        self.assertEqual(request_obj.headers["User-agent"], "custom")

    def test_get_repo_uses_correct_url(self):
        with patch.object(self.client, "_request", return_value={"full_name": "octocat/Hello-World"}) as mock_req:
            result = self.client.get_repo("octocat", "Hello-World")
            mock_req.assert_called_once_with("https://api.github.com/repos/octocat/Hello-World")
            self.assertEqual(result["full_name"], "octocat/Hello-World")

    def test_get_pull_requests_returns_list(self):
        with patch.object(self.client, "_request", return_value=[{"number": 1}]) as mock_req:
            result = self.client.get_pull_requests("octocat", "Hello-World")
            self.assertEqual(result, [{"number": 1}])
            mock_req.assert_called_once()

    def test_get_pull_requests_non_list_returns_empty(self):
        with patch.object(self.client, "_request", return_value={"error": "bad"}):
            result = self.client.get_pull_requests("octocat", "Hello-World")
            self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
