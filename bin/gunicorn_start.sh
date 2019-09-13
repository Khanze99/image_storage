#!/bin/bash
cd rest_api_storage && exec gunicorn -c "/project/rest_api_storage/gunicorn_config.py" rest_api_storage.wsgi
