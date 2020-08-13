from unittest import TestCase
from unittest.mock import patch
from .main_function_using_requests import check_google_status

class TestRequest(TestCase):

    def test_main_function_status_ok(self):
        self.assertEqual(check_google_status(), 200)

    @patch('unit_testing_with_python.main_function_using_requests.requests')
    def test_main_function_status_not_ok(self, mock_function):
        print(mock_function)
        mock_function.return_value = 404
        self.assertEqual(check_google_status(),404)
