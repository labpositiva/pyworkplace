# -*- coding: utf-8 -*-
import requests

from pyworkplace.config import DEBUG
from pyworkplace.config import FACEBOOK_GRAPH_TOKEN
from pyworkplace.config import FACEBOOK_GRAPH_URL
from pyworkplace.config import FACEBOOK_GRAPH_VERSION
from pyworkplace.config import HEADER_AUTH_KEY
from pyworkplace.config import HEADER_AUTH_VAL_PREFIX
from pyworkplace.config import WORKPLACE_ACCESS_TOKEN
from pyworkplace.config import WORKPLACE_API_VERSION
from pyworkplace.config import WORKPLACE_URL
from pyworkplace.core.enum import BaseEnum
from pyworkplace.mixins import BaseMixin


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


class Base(BaseMixin):
    """Base Workplace Wrapper
    https://developers.facebook.com/docs/workplace/
    """

    _auth_args = None
    _response = None
    _after_send = None

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

        self.version = kwargs.get('version', WORKPLACE_API_VERSION)
        self.access_token = kwargs.get(
            'access_token', WORKPLACE_ACCESS_TOKEN,
        )
        self.url = '{}{}/'.format(
            WORKPLACE_URL,
            self.version,
        )

    def _send(self, **kwargs):
        """Make request for request by method
        Input:
            request: recipient id to send to
            method: (get, put)
        Output:
            Response from API as <dict>
        """
        if DEBUG:
            self._response = kwargs
            return self._response
        method = kwargs.pop('method')
        if method == 'get':
            self._response = requests.get(
                **kwargs
            ).json()
        elif method == 'put':
            self._response = requests.put(
                **kwargs
            )
        elif method == 'post':
            self._response = requests.post(
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

    def send_raw(self, **kwargs):
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
            kwargs['resource'],
        )
        kwargs['url'] = request_endpoint
        kwargs['method'] = kwargs.get('method', 'get')
        kwargs['headers'] = kwargs.get(
            'headers', self.auth_args,
        )

        return self._send(**kwargs)

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
        return self.send_raw(**{'payload': payload})


class Facebook(Base):
    request_endpoint = '/me/messages'

    @property
    def auth_args(self):
        """Make auth args validation
        """
        if not self._auth_args:
            self._auth_args = {
                'access_token': self.access_token,
            }
        return self._auth_args

    def __init__(self, **kwargs):
        """
        @required:
            access_token
        @optional:
            version
        """

        self.version = kwargs.get(
            'version',
            FACEBOOK_GRAPH_VERSION,
        )
        self.access_token = kwargs.get(
            'access_token',
            FACEBOOK_GRAPH_TOKEN,
        )
        self.url = '{}{}/'.format(
            FACEBOOK_GRAPH_URL,
            self.version,
        )

    def send_raw(self, **kwargs):
        """Make raw request for facebook
        Input:
            url: url request endpoint
            json: payload
        Output:
            Response from API as <dict>
        """
        kwargs['url'] = '{}{}'.format(
            self.url,
            self.request_endpoint,
        )
        kwargs['params'] = self.auth_args
        kwargs['json'] = kwargs.pop('payload')
        kwargs['headers'] = {'Content-type': 'application/json'}
        kwargs['method'] = 'post'

        return self._send(**kwargs)


class Workplace(Base):
    pass
