from service.factory.api import Service, ServiceAPI
from service.factory.param import StringParameter

__all__ = ["stock_api"]


stock_service = Service(
    name="Weather Service", base_url="https://www.alphavantage.co/query"
)


stock_api = ServiceAPI(
    name="weather",
    service=stock_service,
    method="GET",
    params=[
        StringParameter("symbol"),
        StringParameter("function"),
        StringParameter("apikey"),
    ],
    http_headers={"content-type": "application/json"},
)
