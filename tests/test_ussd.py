import unittest
from app import create_app

class TestUSSD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_ussd_menu(self):
        response = self.client.post('/ussd', data={'sessionId': '12345', 'input': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the USSD menu', response.get_data(as_text=True))

    def test_ussd_option_selection(self):
        response = self.client.post('/ussd', data={'sessionId': '12345', 'input': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('You selected option 1', response.get_data(as_text=True))

    def test_invalid_ussd_input(self):
        response = self.client.post('/ussd', data={'sessionId': '12345', 'input': 'invalid'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input, please try again', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()