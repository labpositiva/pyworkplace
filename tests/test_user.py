# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import has_entries
from hamcrest import not_none

from pyworkplace.user import User

USER_ID = 10000000


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


def test_get_by_id():

    params = {
        'version': 'v1',
        'access_token': 'this is my token',
    }
    user = User(**params)

    args = {
        'user_id': USER_ID,
    }

    assert_that(
        user.get_by_id(**args),
        not_none(),
    )
    response = {
        'url': 'https://www.facebook.com/scim/v1/Users/{}'.format(USER_ID),
        'headers': {
            'Authorization': 'Bearer {}'.format(params['access_token']),
        },
        'method': 'get',
    }
    assert_that(
        response,
        has_entries(user.response),
    )
