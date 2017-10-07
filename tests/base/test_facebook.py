# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.core import Facebook


def test_facebook_instance():
    """ Make instance facebook.
    """
    facebook = Facebook()
    assert_that(
        equal_to(facebook.version),
        'v1',
    )
    assert_that(
        equal_to(facebook.url),
        'https://developers.facebook.com/scim/v1/',
    )
