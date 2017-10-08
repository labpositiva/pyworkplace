# -*- coding: utf-8 -*-
import json

from pyworkplace.core import Workplace


class User(Workplace):
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
