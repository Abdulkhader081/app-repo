import unittest
from app.app import app

class TestHealthEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_health_endpoint(self):
        response = self.app.get('/healthz')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'healthy', response.data)
        self.assertIn(b'status', response.data)

if __name__ == '__main__':
    unittest.main()
