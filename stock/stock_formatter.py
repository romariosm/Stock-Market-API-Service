from datetime import date, timedelta
from flask import current_app


class StockFormatter:
    def __init__(self, results: dict) -> None:
        self.__results = results

    def get_response(self) -> dict:
        stocks_loaded = self.load_stock_date()
        stock_ordered_by_date = self.order_by_date(stocks_loaded)
        if not len(stock_ordered_by_date) > 1:
            current_app.logger.warning(
                f"There were not enough stock dates to calculate net change"
            )
            return {}
        last_stock = stocks_loaded[stock_ordered_by_date[0]]
        day_before_stock = stocks_loaded[stock_ordered_by_date[1]]
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

    def load_stock_date(self):
        stocks = {}
        for k, v in self.__results["Time Series (Daily)"].items():
            stocks[date.fromisoformat(k)] = v
        return stocks

    def order_by_date(self, stocks):
        return sorted(stocks)
