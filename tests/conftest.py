import pytest
import requests
from configuration import *
from src.enums.all_enums import TestData

@pytest.fixture
def get_user():
    def get_single_user(id=''):
        USER_LIST = 'https://reqres.in/api/users'
        full_url = f'{USER_LIST}/{id}'
        t = requests.get(full_url)
        print(full_url)
        return t

    return get_single_user


@pytest.fixture
def get_resources_list():
    return requests.get(RESOURCE_LIST)

# @pytest.fixture()
# def valid_users():
#     valid_url = f'{USER_LIST}/{TestData.VALID_IDS.}'
#     return valid_url