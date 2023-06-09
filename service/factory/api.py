from enum import Enum
import requests

# import xmltodict
import json


class Method(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class Service:
    """
    service definition class
    """

    def __init__(self, name: str, base_url: str):
        self.__name = name
        self.__base_url = base_url

    def __str__(self) -> str:
        return self.__base_url


class ServiceAPI:
    """
    API service consumer
    """

    def __init__(self, name: str, service: Service, method: str, params: list, http_headers: list) -> None:
        self.__name = name
        self.__service = service
        self.__method = method
        self.__params = params
        self.__http_headers = http_headers

    def validate_params(self, **kwargs):
        """
        Validates params sent are correct according to its type
        """
        for param in self.__params:
            if not param.is_valid(kwargs.get(param.get_name)):
                raise Exception("{} type is not valid".format(param))

    def execute(self, **kwargs) -> dict:
        """
        Executes service to retrieve data
        """
        self.validate_params(**kwargs)
        if self.__method == Method.GET.name:
            response = requests.get(
                "{}/{}".format(self.__service, self.__name),
                params=kwargs,
                headers=self.__http_headers,
            )

        if "application/json" in response.__dict__["headers"]["Content-Type"]:
            return response.json()
        return response
