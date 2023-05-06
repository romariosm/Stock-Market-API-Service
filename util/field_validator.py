import re


class Field:
    def __init__(self, name, required=False) -> None:
        self.__name = name
        self.__required = required
        self.__value = None

    def is_required_valid(self, value):
        return (value and self.__required) or not self.__required

    def get_name(self):
        return self.__name

    def is_valid(self):
        return False

    def set_value(self, value):
        self.__value = value

    def get_value(self):
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
