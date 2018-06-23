import json
import flask
from flask import jsonify
from run import app
import unittest

#import requests

class TestClass(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client
        

    # #create a rideoffer
    def test_create_rideoffer(self):
            post_data = (
                {
                    'driver':'den', 
                    'destination':'kamwokya'
                }
            )

            response = self.client().post('/api/v1/users/requests', 
            content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())
            if reply['requests'] == None :
                return jsonify({'message': 'Please fill in a request'})
                
    
            # self.assertEquals(reply['status'], 'OK')
            # self.assertEquals(reply['message'], 'A new request has been created')
            self.assertEqual(response.status_code, 201 )

if __name__ == "__main__":
    unittest.main()