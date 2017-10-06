# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to

from pyworkplace.config import WORKPLACE_URL


def test_workplace_url():
    assert_that('v2.6', equal_to(WORKPLACE_URL))
