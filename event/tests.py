from django.conf import settings
from django.test import TestCase
from event.fetch import Fetcher
from mock import MagicMock, patch
import unittest

# initialize django settings
settings.configure()


class TestFetcher(unittest.TestCase):

    def setUp(self):
        self.dummy_url = "http://www.japanblockfair.com/"
        self.dummy_html = "test"

    def test_requests_backend_fetch(self):

        # patch requests object from where it's first imported
        with patch('event.fetch.requests', spec=True) as mock_req:

            # mock the get call with "test" return value as html
            mock_resp = MagicMock()
            mock_resp.text = self.dummy_html
            mock_req.get = MagicMock(return_value=mock_resp)

            fetcher = Fetcher()
            html = fetcher.get(self.dummy_url)
            self.assertEquals(self.dummy_html, html)





