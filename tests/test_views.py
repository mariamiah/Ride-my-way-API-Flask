import json
from app.views import app
import unittest


class TestClass(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
    # create a rideoffer

    def test_create_rideoffer(self):
            post_data = (
                {
                    'driver': 'den', 'destination': 'kamwokya'
                }
            )

            response = self.client.post('/api/v1/rides',
                                          content_type='application/json',
                                          data=json.dumps(post_data))
            self.assertEqual(response.status_code, 201)
# Fetch all rides


def test_fetch_all_rides(self):
        response = self.client.get('/api/v1/rides',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
# Fetch a single ride offer


# def test_fetch_rideId(self):
        response = self.client.get('/api/v1/rides/<id>',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
# make a ride request


def request_ride_id(self):
        response = self.client.get('/api/v1/rides/<id>/requests',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
if __name__ == "__main__":
    unittest.main()
