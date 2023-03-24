import pytest
import requests
from src.base_classes.parser import ResponseParser
from configuration import USER_LIST
from src.enums.all_enums import TestData
from src.pydantic_schemas.sreated_response import *


def test_create_user(post_user):
    ResponseParser(post_user(TestData.VALID_USER_TO_CREATE.value)) \
        .validate_full_json(CreatedRespFull) \
        .validate_status_code(201)


def test_create_emp(post_user):
    ResponseParser(post_user(TestData.EMPT_USER_TO_CREATE.value)) \
        .validate_full_json(CreatedRespEmpt) \
        .validate_status_code(201)


@pytest.mark.parametrize(
    'data', [TestData.LOGIN_CORRECT_USER.value,
             TestData.LOGIN_CORRECT_ONLY_EMAIL.value,
             ]
)
def test_valid_login(login, data):
    ResponseParser(login(data)).validate_status_code(200)


@pytest.mark.parametrize(
    'data', [TestData.LOGIN_EMPT_USER.value,
             TestData.LOGIN_PASSWORD_ONLY.value,
             TestData.LOGIN_EMAIL_ONLY.value,
             TestData.LOGIN_CORRECT_ONLY_PASS.value]
)
def test_invalid_login(login, data):
    ResponseParser(login(data)).validate_status_code(400)
