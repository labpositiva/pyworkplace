# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import has_entries
from hamcrest import not_none

from pyworkplace.message import Message

RECIPIENT_ID = 10000000
URL = ''


def test_send_message():

    params = {
        'version': 'v2.8',
        'access_token': 'this is my token',
    }
    message = Message(**params)

    args = {
        'recipient_id': RECIPIENT_ID,
        'message': 'Hola Mundo',
    }
    assert_that(
        message.send_message(**args),
        not_none(),
    )

    body = {
        'message': 'Hola Mundo',
        'recipient': {'id': RECIPIENT_ID},
        'notification_type': 'REGULAR',
    }
    response = {
        'url': 'https://graph.facebook.com/v2.8/me/messages',
        'params': {'access_token': params['access_token']},
        'json': body,
        'headers': {'Content-type': 'application/json'},
    }
    assert_that(
        message.response,
        has_entries(response),
    )


def test_send_text_message():
    params = {
        'version': 'v2.8',
        'access_token': 'this is my token',
    }
    message = Message(**params)
    args = {
        'recipient_id': RECIPIENT_ID,
        'message': 'o/ World',
    }
    assert_that(
        message.send_message(**args),
        not_none(),
    )

    body = {
        'message': 'o/ World',
        'recipient': {'id': RECIPIENT_ID},
        'notification_type': 'REGULAR',
    }
    response = {
        'url': 'https://graph.facebook.com/v2.8/me/messages',
        'params': {'access_token': params['access_token']},
        'json': body,
        'headers': {'Content-type': 'application/json'},
    }
    assert_that(
        message.response,
        has_entries(response),
    )
