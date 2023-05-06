import re


class DataValidator:
    def __init__(self, data: dict) -> None:
        self.__data = data
        self.__attrs = self.__get_attr()
        self.__set_field_value()
        self.__validation_message = ""

    @classmethod
    def __get_attr(cls) -> list:
        return [
            v
            for a, v in cls.__dict__.items()
            if not re.match("<function.*?>", str(v))
            and not (a.startswith("__") and a.endswith("__"))
        ]

    def __set_field_value(self):
        for field in self.__attrs:
            if field.get_name() in self.__data.keys():
                field.set_value(self.__data[field.get_name()])

    def is_valid(self):
        for field in self.__attrs:
            if not field.is_valid():
                return False
        return True

    def set_validation_message(self, message):
        self.__validation_message = message

    def get_validation_message(self):
        return self.__validation_message
