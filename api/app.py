#!/usr/bin/env python3
"""Entry point for the API"""

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

swagger = Swagger(app, template_file='v1/swagger/swagger.yaml')

@app.teardown_appcontext
def close_db(error):
    """Close storage on teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, threaded=True)
