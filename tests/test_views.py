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

            response = self.client().post('/api/v1/rides', 
            content_type = 'application/json', data =json.dumps(post_data))
            
            print(response.data)
            self.assertEqual(response.status_code,201)
            # if reply['requests'] == None :
            #     return jsonify({'message': 'Please fill in a request'})
                
    
           
            self.assertEqual(response.status_code, 201 )
        ##Fetch all rides
    def test_fetch_rideoffer(self):
        response= self.client().get('/api/v1/rides',
        content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.status_code,200)
        

if __name__ == "__main__":
    unittest.main()