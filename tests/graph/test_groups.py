# -*- coding: utf-8 -*-
from hamcrest import assert_that
from hamcrest import has_entries
from hamcrest import not_none

from pyworkplace.graph import Group

COMMUNITY_ID = 10000000


def test_get_all_members_without_fields():

    params = {
        'version': 'v2.8',
        'access_token': 'this is my token',
        'community_id': COMMUNITY_ID,
    }
    group = Group(**params)

    assert_that(
        group.get_all_members(),
        not_none(),
    )
    response = {
        'url': 'https://graph.facebook.com/v2.8/{}/members'.format(
            COMMUNITY_ID,
        ),
        'params': group.fields,
        'headers': {'access_token': params['access_token']},
        'method': 'get',
    }
    assert_that(
        response,
        has_entries(group.response),
    )


def test_get_all_members_with_fields():
    FIELDS = {
        'fields': 'id,name',
    }

    params = {
        'version': 'v2.8',
        'access_token': 'this is my token',
        'community_id': COMMUNITY_ID,
    }
    group = Group(**params)

    assert_that(
        group.get_all_members(fields=FIELDS),
        not_none(),
    )
    response = {
        'url': 'https://graph.facebook.com/v2.8/{}/members'.format(
            COMMUNITY_ID,
        ),
        'params': FIELDS,
        'headers': {'access_token': params['access_token']},
        'method': 'get',
    }
    assert_that(
        response,
        has_entries(group.response),
    )


# def test_get_
