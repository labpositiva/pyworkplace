# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import has_entries
from hamcrest import not_none

from pyworkplace.user import User


def test_filter_email():

    params = {
        'version': 'v1',
        'access_token': 'this is my token',
    }
    user = User(**params)

    args = {
        'email': 'slovacus@gmail.com',
    }

    assert_that(
        user.filter_by_email(**args),
        not_none(),
    )
    # 'https://www.facebook.com/scim/v1/Users?filter=userName+eq+"slovacus@gmail.com"
    response = {
        'url': 'https://www.facebook.com/scim/v1/Users',
        'params': {'filter': 'userName+eq+"slovacus@gmail.com"'},
        'headers': {
            'Authorization': 'Bearer {}'.format(params['access_token']),
        },
        'method': 'get',
    }
    assert_that(
        response,
        has_entries(user.response),
    )
