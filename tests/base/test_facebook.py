# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.core import Facebook


def test_facebook_default():
    """ Make instance facebook.
    """
    facebook = Facebook()
    assert_that(
        'v2.6',
        equal_to(facebook.version),
    )
    assert_that(
        'https://graph.facebook.com/v2.6/',
        equal_to(facebook.url),
    )


def test_facebook_change():
    """ Make instance facebook change
    """
    params = {
        'version': 'v2.8',
        'access_token': 'this is my token',
    }
    facebook = Facebook(**params)
    assert_that(
        'v2.8',
        equal_to(facebook.version),
    )
    assert_that(
        'this is my token',
        equal_to(facebook.access_token),
    )
