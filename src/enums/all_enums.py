from src.base_classes.cusrom_enum import CustomEnum


class TestData(CustomEnum):
    VALID_ID = list(range(1,4))
    INVALID_ID= ['asd','!@#$']



t = TestData.INVALID_ID.value

print(t)

