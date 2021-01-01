#!/bin/bash
exec gunicorn --access-logfile - --config gunicorn_config.py wsgi:app
