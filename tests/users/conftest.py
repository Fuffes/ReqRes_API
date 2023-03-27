import pytest
import requests
from configuration import *
from src.enums.all_enums import TestData


def get_single_user(id=''):
    return requests.get(f'{USER_LIST}/{id}')


@pytest.fixture
def get_users():
    return get_single_user


@pytest.fixture
def put_user():
    def put_single_user(id):
        return requests.put(f'{USER_LIST}/{id}')

    return put_single_user


@pytest.fixture
def patch_user():
    def patch_single_user(id):
        return requests.patch(f'{USER_LIST}/{id}')

    return patch_single_user


@pytest.fixture
def delete_user():
    def delete_single_user(id):
        return requests.delete(f'{USER_LIST}/{id}')

    return delete_single_user


@pytest.fixture
def post():
    def post_data(url, data):
        return requests.post(url, data)

    return post_data
