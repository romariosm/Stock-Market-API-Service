from datetime import date, timedelta
from flask import current_app


class StockFormatter:
    def __init__(self, results: dict) -> None:
        self.__results = results

    def get_response(self) -> dict:
        last_stock = self.extract_stock(date.today())
        day_before_stock = self.extract_stock(date.today() - timedelta(days=1))
        try:
            return {
                "symbol": self.get_symbol(),
                "open": float(last_stock.get("1. open")),
                "high": float(last_stock.get("2. high")),
                "low": float(last_stock.get("3. low")),
                "net_change": self.get_net_change(last_stock, day_before_stock),
            }
        except Exception as e:
            current_app.logger.error(
                f"There was an error getting stock response. Error={e}"
            )
        return {}

    def get_net_change(self, current_stock, previous_stock):
        try:
            return float(current_stock["4. close"]) - float(previous_stock["4. close"])
        except Exception as e:
            current_app.logger.error(
                f"There was an error calculating net change. Error={e}"
            )
        return 0

    def get_symbol(self) -> str:
        try:
            return self.__results["Meta Data"].get("2. Symbol")
        except Exception as e:
            current_app.logger.error(
                f"There was an error extracting stock symbol. Error={e}"
            )
        return None

    def extract_stock(self, stock_date: date) -> dict:
        try:
            return self.__results["Time Series (Daily)"].get(stock_date.isoformat())
        except Exception as e:
            current_app.logger.error(
                f"It could not be possible to extract stock info date={stock_date.isoformat()} Error={e}"
            )
        return {}
