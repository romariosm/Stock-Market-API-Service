from enum import Enum
import re


class StockCompany(Enum):
    META = "META"
    AAPL = "AAPL"
    MSFT = "MSFT"
    GOOGLE = "GOOGL"
    AMAZON = "AMZN"

    @classmethod
    def has_value(cls, value):
        return value in [v.value for v in cls.__members__.values()]


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


class DataValidator:
    def __init__(self, data: dict) -> None:
        self.__data = data
        self.__attrs = self.__get_attr()
        self.__set_field_value()
        self.__validation_message = ""

    @classmethod
    def __get_attr(cls) -> list[Field]:
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


class StockInfoValidator(DataValidator):
    symbol = StringField(name="symbol", required=True)

    def is_valid(self):
        if StockCompany.has_value(self.symbol.get_value()):
            return super().is_valid()
        self.set_validation_message(f"{self.symbol.get_value()} is not allowed")
        return False


class AuthValidator(DataValidator):
    name = StringField(name="name", required=True)
    lastname = StringField(name="lastname", required=True)
    email = EmailField(name="email", required=True)
