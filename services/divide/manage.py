"""
    manage.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    CLI tool for manage application.

    :description: Microservice for plus operation
    :copyright: © 2020 written by Sungshik Jou.
    :license: MIT, see LICENSE for more details.
"""

from flask.cli import FlaskGroup
from service import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)

app.logger.info('SQLALCHEMY_DATABASE_URI: {0}'.format(app.config['SQLALCHEMY_DATABASE_URI']))


@cli.command('recreate_db')
def recreate_db():
    """
    Re-create database tables.
    :return:
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
