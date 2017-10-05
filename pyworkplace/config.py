# -*- coding: utf-8 -*-
import ast
import os


DEFAULT_API_VERSION = 2.6

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Application
APP_NAME = os.environ.get('APP_NAME')
APP_DEBUG = ast.literal_eval(os.environ.get('APP_DEBUG', 'False'))
WORKPLACE_URL = os.environ.get('WORKPLACE_URL')
WORKPLACE_VERSION = os.environ.get('WORKPLACE_VERSION')
HEADER_AUTH_KEY = 'Authorization'
HEADER_AUTH_VAL_PREFIX = 'Bearer'
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
API_VERSION = os.environ.get('API_VERSION', DEFAULT_API_VERSION)
