import re


class Field:
    def __init__(self, name: str, required: bool=False) -> None:
        self.__name = name
        self.__required = required
        self.__value = None

    def is_required_valid(self, value: object) -> bool:
        return (value and self.__required) or not self.__required

    def get_name(self) -> str:
        return self.__name

    def is_valid(self) -> bool:
        return False

    def set_value(self, value: object) -> None:
        self.__value = value

    def get_value(self) -> object:
        return self.__value


class StringField(Field):
    def is_valid(self) -> bool:
        return isinstance(self.get_value(), str) and self.is_required_valid(
            self.get_value()
        )


class EmailField(Field):
    FORMAT = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    def is_valid(self) -> bool:
        return (
            isinstance(self.get_value(), str)
            and self.is_required_valid(self.get_value())
            and self.is_email_valid()
        )

    def is_email_valid(self) -> bool:
        return re.fullmatch(self.FORMAT, self.get_value())
