Flask Boilerplate
=================

This is a boilerplate for Flask apps.


Components
----------

 * Flask
 * Flask-SQLAlchemy
 * Flask-WTForms
 * Flask-Login
 * Pytest


Installation
------------

You will need to set up a virtualenv, activate it and install the requirements.:

    virtualenv .env
    . ./.env/bin/activate
    pip install -r requirements.txt


Server
------

Running the development server is as easy as:

    ./server.py


Tests
-----

Tests are written using py.test, run them using:

    py.test tests/ -v
