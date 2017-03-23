##########################
##  app/__init__.py
##  Creates the Flask instance
##  and initializes the app 
##  module.
##
##  (c)Damian Matthews
##########################

from flask import Flask
app = Flask(__name__)
from app import routes
