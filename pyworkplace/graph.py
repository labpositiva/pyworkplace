# -*- coding: utf-8 -*-
from pyworkplace.core import Facebook


class Graph(Facebook):

    community_id = None
    fields = {
        'fields': ','.join(
            (
                'id',
                'name',
                'members',
                'email',
                'privacy',
                'description',
                'updated_time',
                'administrator',
            ),
        ),
    }

    def __init__(self, *args, **kwargs):
        """
        @required:
            access_token
        @optional:
            version
            url
            community_id
        """
        if not kwargs.get('community_id'):
            raise ValueError('community_id is required')
        super(Graph, self).__init__(*args, **kwargs)
        self.community_id = kwargs['community_id']
        self.url = '{}{}'.format(
            self.url,
            self.community_id,
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
            self.endpoint,
        )
        kwargs['headers'] = kwargs.get(
            'headers', self.auth_args,
        )
        kwargs['params'] = kwargs['params']
        return self._send(**kwargs)


class Groups(Graph):
    endpoint = '/groups'


class Members(Graph):
    endpoint = '/members'

    def get_all_members(self, fields=None):
        """Get all members of group.
        Input:
        Output:
            Response from API as <dict>
        """
        kwargs = {}
        kwargs['params'] = self.fields
        if fields:
            kwargs['params'] = fields
        return self.send_raw(**kwargs)
