[![Build Status](https://travis-ci.org/mariamiah/Ride-my-way2.svg?branch=develop)](https://travis-ci.org/mariamiah/Ride-my-way2)

# Ride-my-way2
Ride-My-Way2 provides provides guidelines for the Ride-My-Way APIs which encourage consistency across applications. 

## Getting started
-The URL that identifies the resource should include nouns and not verbs.
-Use HTTP verbs (GET, POST, PUT, DELETE) to operate on the collections and elements.
-Put the version number at the base of your URL, for example http://example.com/v1/path/to/resource.
-Formats should be in the form of api/v2/resource/{id}.json

## Prerequisites
-Web browser 
-Good internet connection

## HTTP status codes
Use three simple, common response codes indicating (1) success, (2) failure due to client-side problem, (3) failure due to server-side problem:
-200 - OK
-400 - Bad Request
-500 - Internal Server Error

## API Resources
-GET /rides
-GET /rides/[id]
-POST /rides
-POST/rides/[id]/requests

## Authors
-Maria Nanfuka https://ridemyway23-api-heroku.herokuapp.com/
