from enum import Enum

from src.base_classes.cusrom_enum import EnumList


class TestData(Enum):
    VALID_ID = list(range(1, 4))
    INVALID_ID = ['asd', '!@#$']
    VALID_USER_TO_CREATE = {"name": "dsd", "job": "dsd"}
    EMPT_USER_TO_CREATE = {}

    # inv
    LOGIN_EMPT_USER = {}
    LOGIN_PASSWORD_ONLY = {"password": "cityslicka"}
    LOGIN_EMAIL_ONLY = {"email": "cityslicka"}
    LOGIN_CORRECT_ONLY_PASS = {"email": "eve.holt@dsds.in", "password": "cityslicka"}

    # val
    LOGIN_CORRECT_USER = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    LOGIN_CORRECT_ONLY_EMAIL = {"email": "eve.holt@reqres.in", "password": "f"}




