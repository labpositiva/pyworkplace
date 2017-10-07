# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.core import Base


def test_base_default():
    """ Test Base default
    """
    base = Base()
    assert_that(
        equal_to(base.version),
        'v1',
    )
    assert_that(
        equal_to(base.url),
        'https://developers.facebook.com/scim/v1/',
    )
