import pytest
import requests
from configuration import *
from src.enums.all_enums import TestData


@pytest.fixture
def get_resources():
    def get_single_resource(id=''):
        return requests.get(f'{RESOURCE_LIST}/{id}')

    return get_single_resource


@pytest.fixture
def put_resource():
    def put_single_resource(id):
        return requests.put(f'{RESOURCE_LIST}/{id}')

    return put_single_resource


@pytest.fixture
def patch_resource():
    def patch_single_resource(id):
        return requests.patch(f'{RESOURCE_LIST}/{id}')

    return patch_single_resource


@pytest.fixture
def delete_resource():
    def delete_single_resource(id):
        return requests.delete(f'{RESOURCE_LIST}/{id}')

    return delete_single_resource
