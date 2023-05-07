from enum import Enum
from util.field_validator import StringField, EmailField
from util.validator import DataValidator


class StockCompany(Enum):
    META = "META"
    AAPL = "AAPL"
    MSFT = "MSFT"
    GOOGLE = "GOOGL"
    AMAZON = "AMZN"

    @classmethod
    def has_value(cls, value:str) -> bool:
        return value in [v.value for v in cls.__members__.values()]


class StockInfoValidator(DataValidator):
    symbol = StringField(name="symbol", required=True)

    def is_valid(self) -> bool:
        if StockCompany.has_value(self.symbol.get_value()):
            return super().is_valid()
        self.set_validation_message(f"{self.symbol.get_value()} is not allowed")
        return False


class AuthValidator(DataValidator):
    name = StringField(name="name", required=True)
    lastname = StringField(name="lastname", required=True)
    email = EmailField(name="email", required=True)
