# -*- coding: utf-8 -*-
import os

import mock
from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.config import FACEBOOK_GRAPH_URL
from pyworkplace.config import FACEBOOK_GRAPH_VERSION


def test_facebook_graph_version():
    assert_that('v2.6', equal_to(FACEBOOK_GRAPH_VERSION))


def test_url_graph_default():
    assert_that(
        'https://graph.facebook.com/',
        equal_to(FACEBOOK_GRAPH_URL),
    )


@mock.patch.dict(os.environ, {'PYWORKPLACE_GRAPH_VERSION': 'v2.8'})
def test_url_graph():
    assert_that(
        equal_to(FACEBOOK_GRAPH_URL),
        'https://graph.facebook.com/',
    )

    assert_that(
        equal_to(FACEBOOK_GRAPH_VERSION),
        'v2.8',
    )
