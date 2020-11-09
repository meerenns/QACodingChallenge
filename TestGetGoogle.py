import unittest
from http import HTTPStatus

import requests


class GetGoogleTestCase(unittest.TestCase):
    def test_google_response (self):
        result = requests.get("http://www.google.com")
        self.assertEqual(HTTPStatus.OK, result.status_code)


if __name__ == '__main__':
    unittest.main()
