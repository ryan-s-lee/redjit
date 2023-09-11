import os

command = os.environ["GUNICORN_SCRIPT_PATH"]
pythonpath = os.environ["REDJIT_PROJECT_PATH"]
wsgi_app = 'redjit.wsgi'
bind = '127.0.0.1:8000'
workers = 3