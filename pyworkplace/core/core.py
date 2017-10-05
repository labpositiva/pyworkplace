# -*- coding: utf-8 -*-
import json

import requests

from .config import ACCESS_TOKEN
from .config import HEADER_AUTH_KEY
from .config import HEADER_AUTH_VAL_PREFIX
from .config import WORKPLACE_URL
from .config import WORKPLACE_VERSION


class Base(object):
    """Base Workplace Wrapper
    https://developers.facebook.com/docs/workplace/
    """

    _auth_args = None
    _response = None

    version = None
    access_token = None
    workplace_url = None

    def __init__(self, **kwargs):
        """
        @required:
            access_token
        @optional:
            version
        """

        self.version = kwargs.get('version') or WORKPLACE_VERSION
        self.access_token = kwargs.get('access_token') or ACCESS_TOKEN
        self.workplace_url = '{}{}/'.format(
            WORKPLACE_URL,
            WORKPLACE_VERSION,
        )

    @property
    def auth_args(self):
        """Make auth args validation
        https://developers.facebook.com/docs/workplace/
        """
        if not self._auth_args:
            self._auth_args = {
                HEADER_AUTH_KEY: '{} {}'.format(
                    HEADER_AUTH_VAL_PREFIX,
                    self.access_token,
                ),
            }
        return self._auth_args

    def send_raw(self, resource, **kwargs):
        """Make raw request for facebook
        Input:
            resource: recipient id to send to
            method: (get, put)
            data: data content
        Output:
            Response from API as <dict>
        """
        request_endpoint = '{}{}'.format(
            self.workplace_url,
            resource,
        )
        kwargs['url'] = request_endpoint
        kwargs['method'] = kwargs.get('method', 'get')
        kwargs['headers'] = kwargs.get('headers') or self.auth_args

        return self._make_request(**kwargs)

    def _make_request(self, **kwargs):
        """Make request for request by method
        Input:
            request: recipient id to send to
            method: (get, put)
        Output:
            Response from API as <dict>
        """
        method = kwargs.pop('method')
        response = None
        if method == 'get':
            response = requests.get(
                **kwargs
            ).json()
        elif method == 'put':
            response = requests.put(
                **kwargs
            )
        else:
            raise NotImplementedError('Not Implemented')
        return response


class User(Base):
    """Actions for resources Users
    https://developers.facebook.com/docs/workplace/account-management/api
    """

    _url = 'Users'

    def filter_by_username(self, username):
        """Filter by username
        https://developers.facebook.com/scim/v1/Users?filter=userName%20eq%20%22juliusc@example.com%22
        Input:
          username: email of user
        Output:
          Response from API as <dict>
        """
        resource = '{}?filter=userName+eq+"{}"'.format(
            self._url,
            username,
        )
        return self.send_raw(resource=resource)

    def get_by_id(self, user_id):
        """Get by user_id
        https://developers.facebook.com/scim/v1/Users/{{user_id}}
        Input:
          user_id: user id
        Output:
          Response from API as <dict>
        """
        resource = '{}/{}'.format(
            self._url,
            user_id,
        )
        return self.send_raw(resource=resource)

    def update(self, user_id, data):
        """Update
        https://www.facebook.com/scim/v1/Users/{Workplace-assigned user id}
        Input:
          user_id: id de facebook user
          data: payload json data
        Output:
          Response from API as <dict>
        """
        if isinstance(data, dict):
            data = json.dumps(data)
        resource = '{}/{}'.format(
            self._url,
            user_id,
        )
        kwargs = {
            'method': 'put',
            'data': data,
        }
        return self.send_raw(resource=resource, **kwargs)
