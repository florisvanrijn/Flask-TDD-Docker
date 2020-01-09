from flask import Flask, jsonify
from flask_restplus import Resource, Api

# instantiating the app
app = Flask(__name__)

api = Api(app)

# Pull in the development config on init:
# set config
app.config.from_object('project.config.DevelopmentConfig') # new

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')