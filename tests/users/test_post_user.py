import pytest
import requests
from src.base_classes.parser import ResponseParser
from configuration import USER_LIST
from src.enums.all_enums import TestData
from src.pydantic_schemas.sreated_response import *


def test_create_user(post):
    ResponseParser(post(USER_LIST, TestData.VALID_USER_TO_CREATE.value)) \
        .validate_full_json(CreatedRespFull) \
        .validate_status_code(201)


def test_create_emp(post):
    ResponseParser(post(USER_LIST, TestData.EMPT_USER_TO_CREATE.value)) \
        .validate_full_json(CreatedRespEmpt) \
        .validate_status_code(201)



