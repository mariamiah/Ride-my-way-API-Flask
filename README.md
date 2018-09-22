[![Build Status](https://travis-ci.org/mariamiah/Ride-my-way2.svg?branch=develop)](https://travis-ci.org/mariamiah/Ride-my-way2)
[![Coverage Status](https://coveralls.io/repos/github/mariamiah/Ride-my-way2/badge.svg?branch=develop)](https://coveralls.io/github/mariamiah/Ride-my-way2?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/302d910c9518da06613e/maintainability)](https://codeclimate.com/github/mariamiah/Ride-my-way2/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c08f98348122401696ab3b06dec4e794)](https://app.codacy.com/app/mariamiah/Ride-my-way2?utm_source=github.com&utm_medium=referral&utm_content=mariamiah/Ride-my-way2&utm_campaign=Badge_Grade_Dashboard)


# Ride-my-way2
Ride-My-Way2 provides provides guidelines for the Ride-My-Way APIs which encourage consistency across applications. 

## Getting started
- The URL that identifies the resource should include nouns and not verbs.
- Use HTTP verbs (GET, POST, PUT, DELETE) to operate on the collections and elements.
- Put the version number at the base of your URL.
- Formats should be in the form of api/v1/resource/{id}.json

## Prerequisites
- Web browser 
- Good internet connection

## HTTP status codes
Use three simple, common response codes indicating (1) success, (2) failure due to client-side problem, (3) failure due to server-side problem:
- 200 - OK
- 400 - Bad Request
- 500 - Internal Server Error

## API Resources
- GET /rides
- GET /rides/[id]
- POST /rides
- POST/rides/[id]/requests

## Authors
- Maria Nanfuka https://mariam-ride.herokuapp.com/
