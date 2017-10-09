# -*- coding: utf-8 -*-
import mock
from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace import Page


def test_handle_webhook_errors():
    page = Page(**{'page_access_token': 'this is my token'})
    payload = """
        {
            "object":"not_page",
            "entry":[
                {"id":"1691462197845448","time":1472026867114,
                "messaging":[
                    {"sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472026867080,
                     "message":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"hello world"}}
                ]}
            ]
        }
        """
    assert_that(False, equal_to(page.handle_webhook(payload)))

    payload = """
    {
        "object":"page",
        "entry":[
            {"id":"1691462197845448","time":1472026867114,
            "messaging":[
                {"sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472026867080,
                    "unknown":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"hello world"}}
            ]}
        ]
    }
    """

    page.handle_webhook(payload)

    @page.callback
    def unknown():
        pass


def test_handle_webhook_message():
    page = Page(**{'page_access_token': 'this is my token'})
    payload = """
    {
        "object":"page",
        "entry":[
            {"id":"1691462197845448","time":1472026867114,
            "messaging":[
                {"sender":{"id":"1134343043305865"},"recipient":{"id":"1691462197845448"},"timestamp":1472026867080,
                    "message":{"mid":"mid.1472026867074:cfb5e1d4bde07a2a55","seq":812,"text":"hello world"}}
            ]}
        ]
    }
    """
    counter = mock.MagicMock()
    page.handle_webhook(payload)

    @page.handle_message
    def handler1(event):
        assert_that(True, equal_to(event.is_message))
        assert_that(True, equal_to(event.is_text_message))
        assert_that(False, equal_to(event.is_attachment_message))
        assert_that(False, equal_to(event.is_quick_reply))
        assert_that(False, equal_to(event.is_echo))
        assert_that(False, equal_to(event.is_read))
        assert_that(False, equal_to(event.is_postback))
        assert_that(False, equal_to(event.is_postback_referral))
        assert_that(False, equal_to(event.is_optin))
        assert_that(False, equal_to(event.is_delivery))
        assert_that(False, equal_to(event.is_account_linking))
        assert_that(False, equal_to(event.is_referral))
        assert_that(1472026867080, equal_to(event.timestamp))
        assert_that(equal_to(event.sender_id), '1134343043305865')
        assert_that(equal_to(event.recipient_id), '1691462197845448')
        assert_that(equal_to(event.message_text), 'hello world')
        counter()

    page.handle_webhook(payload)
    assert_that(1, equal_to(counter.call_count))

    counter2 = mock.MagicMock()

    def handler2(event):
        counter2()

    page.handle_webhook(payload, message=handler2)
    assert_that(1, equal_to(counter2.call_count))
