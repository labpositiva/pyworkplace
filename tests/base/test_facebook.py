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
