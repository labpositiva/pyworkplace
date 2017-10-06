# -*- coding: utf-8 -*-
import os

from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.config import FACEBOOK_GRAPH_URL
from pyworkplace.config import FACEBOOK_GRAPH_VERSION


def test_facebook_graph_version():
    assert_that('v2.6', equal_to(FACEBOOK_GRAPH_VERSION))


def test_url_graph_default():
    assert_that(
        'https://graph.facebook.com/v2.6/',
        equal_to(FACEBOOK_GRAPH_URL),
    )


def test_url_graph():
    os.environ['FACEBOOK_GRAPH_VERSION'] = 'v2.8'
    assert_that(
        'https://graph.facebook.com/v2.8/',
        equal_to(FACEBOOK_GRAPH_URL),
    )
