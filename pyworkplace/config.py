# -*- coding: utf-8 -*-
import ast
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Application

DEBUG = ast.literal_eval(os.environ.get('PYWORKPLACE_DEBUG', 'False'))
HEADER_AUTH_KEY = 'Authorization'
HEADER_AUTH_VAL_PREFIX = 'Bearer'

# Workplace
WORKPLACE_URL = os.environ.get(
    'PYWORKPLACE_URL',
    'https://www.facebook.com/scim/',
)
WORKPLACE_API_VERSION = os.environ.get(
    'PYWORKPLACE_API_VERSION',
    'v1',
)
WORKPLACE_API_URL = os.environ.get(
    'PYWORKPLACE_API_URL',
    'https://developers.facebook.com/scim/{}/'.format(
        WORKPLACE_API_VERSION,
    ),
)
WORKPLACE_ACCESS_TOKEN = os.environ.get('PYWORKPLACE_ACCESS_TOKEN')

FACEBOOK_GRAPH_VERSION = os.environ.get(
    'PYWORKPLACE_GRAPH_VERSION',
    'v2.6',
)
FACEBOOK_GRAPH_URL = os.environ.get(
    'PYWORKPLACE_URL_GRAPH',
    'https://graph.facebook.com/{}/'.format(
        FACEBOOK_GRAPH_VERSION,
    ),
)
