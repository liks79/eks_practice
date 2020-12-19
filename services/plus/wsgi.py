"""
    wsgi.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    WSGI(Web Server Gateway Interface) script to deploy AWS ElasticBeanstalk.

    :description: Microservice for plus operation
    :copyright: © 2020 written by Sungshik Jou.
    :license: MIT, see LICENSE for more details.
"""

import os
from service import create_app, db

application = create_app()

application.logger.info('SQLALCHEMY_DATABASE_URI: {0}'.format(application.config['SQLALCHEMY_DATABASE_URI']))

APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = os.getenv('APP_PORT', 8080)

if __name__ == '__main__':
    application.run(host=APP_HOST, port=APP_PORT)
