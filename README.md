[![Build Status](https://travis-ci.org/mariamiah/Ride-my-way2.svg?branch=develop)](https://travis-ci.org/mariamiah/Ride-my-way2)
[![Coverage Status](https://coveralls.io/repos/github/mariamiah/Ride-my-way2/badge.svg?branch=develop)](https://coveralls.io/github/mariamiah/Ride-my-way2?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/302d910c9518da06613e/maintainability)](https://codeclimate.com/github/mariamiah/Ride-my-way2/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c08f98348122401696ab3b06dec4e794)](https://app.codacy.com/app/mariamiah/Ride-my-way2?utm_source=github.com&utm_medium=referral&utm_content=mariamiah/Ride-my-way2&utm_campaign=Badge_Grade_Dashboard)

# RideShare-API
- RideShare is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers.

## Features
- Users can create an account and log in.
- Drivers can add ride offers..
- Passengers can view all available ride offers.
- Passengers can see the details of a ride offer and request to join the ride. E.g What time the ride leaves, where it is headed e.t.c
- Drivers can view the requests to the ride offer they created.
- Drivers can either accept or reject a ride request.
- Users can only see and respond to ride offers from their friends on the application .
- Passengers get real time notifications when their request is accepted or rejected
### Setup
- clone this repository using `git clone git@github.com:mariamiah/RideShare-API-Flask.git`
- install pipenv
```sh
    pip install --upgrade setuptools wheel
    pip install --user pipenv
```
- specify python version using `pyenv local 3.8.0`
- setup environment using `pipenv shell`
- start project with `pipenv run python app.py`
- lock dependencies with `pipenv lock -r > requirements.txt`
- uninstall dependencies with `pipenv uninstall <package-name>`
- remove virtual environment with `pipenv --rm`