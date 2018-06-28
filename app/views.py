from flask import Flask, request,jsonify
from .models import Rideoffer
from run import app
import json 

@app.route('/api/v1/rides' ,methods= ['POST'])
def create_rideoffer():
	""" This endpoint creates a ride offer """
	user = []
	data = request.get_json()
	try:
		if isinstance(data['driver'], str) and isinstance(data['destination'], str):
			id = len(user)
			id += 1 
			Request =Rideoffer(id,data['driver'],data['destination'] )
			user.append(Request)  
		return jsonify(Request.get_dict()), 201
		
	except AttributeError:
		return jsonify({
			'status': 'fail',
			'message': 'failed to create a request. Invalid data'
		}), 400
