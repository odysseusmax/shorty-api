from flask import Flask
from flask_cors import CORS
import pymongo

from config import Config
from .route import register_routes
from .models import Connections


app = Flask(__name__)
CORS(app)

Connections.pool['db'] = pymongo.MongoClient(Config.DATABASE_URI)

register_routes(app)
