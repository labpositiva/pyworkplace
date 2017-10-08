# -*- coding: utf-8 -*-
import json

from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.event import Event


def test_event_message():
    payload = """
        {"sender":{"id":"sender"},"recipient":{"id":"recipient"},"timestamp":1472026867080,
        "message":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"o/ world"}}
    """
    event = Event(messaging=json.loads(payload))
    assert_that(equal_to(event.sender_id), 'sender')
    assert_that(equal_to(event.recipient_id), 'recipient')
    assert_that(equal_to(event.message_text), 'o/ world')


def test_event_postback():
    payload = """
        {"sender": {"id": "sender"},
        "recipient": {"id": "recipient"}, "timestamp": 1472028006107,
        "postback": {"payload": "DEVELOPED_DEFINED_PAYLOAD"}}
    """
    event = Event(messaging=json.loads(payload))
    assert_that(equal_to(event.sender_id), 'sender')
    assert_that(equal_to(event.recipient_id), 'recipient')
    assert_that(equal_to(event.postback), 'DEVELOPED_DEFINED_PAYLOAD')
    assert_that(equal_to(True), event.is_postback)
