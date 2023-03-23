from src.base_classes.cusrom_enum import CustomEnum


class TestData(CustomEnum):
    VALID_IDS = list(range(1,3))
    INVALID_IDS = ['asd', '!@#$']


