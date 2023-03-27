import pytest

from src.base_classes.parser import ResponseParser
from src.enums.all_enums import TestData
from configuration import REGISTRATION_URL


@pytest.mark.parametrize(
    'data', [TestData.LOGIN_CORRECT_USER.value,
             TestData.LOGIN_CORRECT_ONLY_EMAIL.value,
             ]
)
def test_valid_registr(post, data):
    ResponseParser(post(REGISTRATION_URL, data)).validate_status_code(200)


@pytest.mark.parametrize(
    'data', [TestData.LOGIN_EMPT_USER.value,
             TestData.LOGIN_PASSWORD_ONLY.value,
             TestData.LOGIN_EMAIL_ONLY.value,
             TestData.LOGIN_CORRECT_ONLY_PASS.value]
)
def test_invalid_registr(post, data):
    ResponseParser(post(REGISTRATION_URL, data)).validate_status_code(400)
