# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.config import API_VERSION


def test_api_version():
    assert_that('v2.6', equal_to(API_VERSION))
