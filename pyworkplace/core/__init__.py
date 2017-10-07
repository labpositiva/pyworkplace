# -*- coding: utf-8 -*-
import requests

from pyworkplace.config import HEADER_AUTH_KEY
from pyworkplace.config import HEADER_AUTH_VAL_PREFIX
from pyworkplace.config import WORKPLACE_ACCESS_TOKEN
from pyworkplace.config import WORKPLACE_API_VERSION
from pyworkplace.config import WORKPLACE_URL
from pyworkplace.core.enum import BaseEnum


class NotificationType(BaseEnum):
    regular = 'REGULAR'
    silent_push = 'SILENT_PUSH'
    no_push = 'NO_PUSH'


class SettingType(BaseEnum):
    greeting = 'greeting'
    call_to_actions = 'call_to_actions'


class ThreadState(BaseEnum):
    new_thread = 'new_thread'
    existing_thread = 'existing_thread'


class Base(object):
    """Base Workplace Wrapper
    https://developers.facebook.com/docs/workplace/
    """

    _auth_args = None
    _response = None

    version = None
    access_token = None
    url = None

    def __init__(self, **kwargs):
        """
        @required:
            access_token
        @optional:
            version
        """

        self.version = kwargs.get('version') or WORKPLACE_API_VERSION
        self.access_token = kwargs.get(
            'access_token',
        ) or WORKPLACE_ACCESS_TOKEN
        self.url = '{}{}/'.format(
            WORKPLACE_URL,
            WORKPLACE_API_VERSION,
        )

    def _make_request(self, **kwargs):
        """Make request for request by method
        Input:
            request: recipient id to send to
            method: (get, put)
        Output:
            Response from API as <dict>
        """
        method = kwargs.pop('method')
        if method == 'get':
            self._response = requests.get(
                **kwargs
            ).json()
        elif method == 'put':
            self._response = requests.put(
                **kwargs
            )
        else:
            raise NotImplementedError('Not Implemented')
        return self._response

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

    @property
    def response(self):
        return self._response or None

    @response.setter
    def response(self, value):
        raise NotImplementedError('Not Implemented')

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
            self.url,
            resource,
        )
        kwargs['url'] = request_endpoint
        kwargs['method'] = kwargs.get('method', 'get')
        kwargs['headers'] = kwargs.get('headers') or self.auth_args

        return self._make_request(**kwargs)

    def send_message(
        self, recipient_id, message,
        notification_type=NotificationType.regular,
    ):
        return self.send_recipient(
            recipient_id, {
                'message': message,
            }, notification_type,
        )

    def send_recipient(
        self, recipient_id, payload,
        notification_type=NotificationType.regular,
    ):
        payload['recipient'] = {
            'id': recipient_id,
        }
        payload['notification_type'] = notification_type.value
        return self.send_raw(payload)
