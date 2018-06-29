from flask import Flask, request, jsonify
from .models import RideOffer
from run import app
import json
users = []


@app.route('/api/v1/rides', methods=['POST'])
def create_rideoffer():
    """ This endpoint creates a ride offer """

    data = request.get_json()
    try:
        if isinstance(data['driver'], str) and isinstance(data['destination'], str):
            id = len(users)
            id += 1
            Request = RideOffer(id, data['driver'], data['destination'])
            users.append(Request)
        return jsonify(Request.get_dict()), 201

    except AttributeError:
        return jsonify({
            'status': 'fail',
            'message': 'failed to create a request. Invalid data'
        }), 400


@app.route('/api/v1/rides', methods=['GET'])
def fetch_all_rides():
    """This endpoint fetches all rides"""
    rides = [ride.get_dict() for ride in users]
    return jsonify({'Rides': rides}), 200


@app.route('/api/v1/rides/<id>', methods=['GET'])
def fetch_ride_id(id):
    fetch_rides = []
    data = users
    for obj in users:
        if int(id) > len(data):
            return jsonify({
                'status': 'Fail',
                'message': 'ID not found. Please add a valid ID'
            }), 400
        obj = data[int(id)-1]
        fetch_rides.append(obj.get_dict())
        return jsonify({
            'status': 'Success',
            'request': fetch_rides
        }), 200
