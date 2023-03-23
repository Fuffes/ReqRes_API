import pytest
import requests
from configuration import *


@pytest.fixture
def get_user_list():
    return requests.get(USER_LIST)


@pytest.fixture
def get_resources_list():
    return requests.get(RESOURCE_LIST)