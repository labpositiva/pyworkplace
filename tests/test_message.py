# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to
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
        'url': 'https://graph.facebook.com/v2.8/me/messages?access_token={}'.format(
            params['access_token'],
        ),
        'method': 'post',
    }
    assert_that(
        message.response,
        equal_to(response),
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
        'message': {
            'text': 'o/ World',
        },
        'recipient': {'id': RECIPIENT_ID},
        'notification_type': 'REGULAR',
    }

    response = {
        'url': 'https://graph.facebook.com/v2.8/{}'.format(body),
        'method': 'post',
        'headers': {'Authorization': 'Bearer this is my token'},
    }
    assert_that(
        message.response,
        equal_to(response),
    )


# def test_send_button_message():
#     message = Message()
#     text = 'Ahora que quieres hacer?'
#     buttons = [
#         {
#             'type': 'postback',
#             'title': 'TERMINAR PEDIDO',
#             'payload': 'PAYLOAD_TERMINAR_PEDIDO',
#         },
#         {
#             'type': 'postback',
#             'title': 'EDITAR PEDIDO',
#             'payload': 'PAYLOAD_EDITAR_PEDIDO',
#         },
#     ]
#     body = {
#         'recipient': {'id': RECIPIENT_ID},
#         'message': {
#             'attachment': {
#                 'type': 'template',
#                 'payload': {
#                     'template_type': 'button',
#                     'text': text,
#                     'buttons': buttons,
#                 },
#             },
#         },
#         'notification_type': 'REGULAR',
#     }

#     args = {
#         'recipient_id': RECIPIENT_ID,
#         'text': text,
#         'buttons': buttons,
#     }
#     assert_that(
#         message.send_button_message(**args),
#         not_none(),
#     )

#     response = message.response
#     assert_that(
#         json.loads(response.request.body),
#         has_entries(body),
#     )
#     assert_that(response.request.url, equal_to(URL))
