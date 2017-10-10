# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import has_entries
from hamcrest import not_none

from pyworkplace.message import Template

RECIPIENT_ID = 10000000
URL = ''


def test_send_button():

    params = {
        'version': 'v2.8',
        'access_token': 'this is my token',
    }
    message = Template(**params)

    args = {
        'recipient_id': RECIPIENT_ID,
        'text': 'button',
        'buttons': [
            {
                'type': 'postback',
                'title': 'title',
                'payload': 'POSTBACK',
            },
        ],
    }
    assert_that(
        message.send_button(**args),
        not_none(),
    )
    body = {
        'message': {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'button',
                    'text': 'button'.encode('utf-8'),
                    'buttons': [
                        {
                            'type': 'postback',
                            'title': 'title',
                            'payload': 'POSTBACK',
                        },
                    ],
                },
            },
        },
        'recipient': {'id': RECIPIENT_ID},
        'notification_type': 'REGULAR',

    }

    response = {
        'url': 'https://graph.facebook.com/v2.8/me/messages',
        'params': {'access_token': params['access_token']},
        'json': body,
        'headers': {'Content-type': 'application/json'},
        'method': 'post',
    }
    assert_that(
        response,
        has_entries(message.response),
    )
