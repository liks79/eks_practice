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

app = create_app()

app.logger.info('SQLALCHEMY_DATABASE_URI: {0}'.format(app.config['SQLALCHEMY_DATABASE_URI']))

APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = os.getenv('APP_PORT', 5000)

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)
