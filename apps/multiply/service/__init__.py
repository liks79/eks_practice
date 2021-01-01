"""
    service/__init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    :description: Microservice for plus operation
    :copyright: © 2020 written by Sungshik Jou.
    :license: MIT, see LICENSE for more details.
"""

import os
import logging
import sys
import json
import datetime
from bson.objectid import ObjectId
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


# instantiate the database
db = SQLAlchemy()


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


def create_app(script_info=None):

    # instantiate the application
    app = Flask(__name__)

    # initiate some config value for JWT Authentication
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'my_jwt')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    app.config['PROPAGATE_EXCEPTIONS'] = True

    # initiate some config value for JWT Authentication
    jwt = JWTManager(app)
    app.json_encoder = JSONEncoder

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    # # set config
    app_settings = os.getenv('APP_SETTINGS', 'service.config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # set logger to STDOUT
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.DEBUG)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from service.api.multiply import multiply_blueprint
    app.register_blueprint(multiply_blueprint, url_prefix='/multiply')

    # Setup models for DB operations
    with app.app_context():
        try:
            db.create_all()
            app.logger.info('Create database tables')
        except Exception as e:
            app.logger.error(e)


    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'application': app, 'database': db}

    return app
