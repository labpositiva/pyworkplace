# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import has_entries

from pyworkplace import Page


def test_handle_webhook_error():
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
