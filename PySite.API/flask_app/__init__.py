from flask import Flask
from flask_cors import CORS
import logging

app = Flask(__name__)

from flask_app import routes
