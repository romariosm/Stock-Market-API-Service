import json
from flask_jwt_extended import create_access_token, jwt_required

from flask import Blueprint, request, current_app, Response
from service.stock_service import stock_api
from stock.stock_validator import StockInfoValidator, AuthValidator
from stock.stock_formatter import StockFormatter


api = Blueprint("stock", __name__)
STOCK_FRECUENCY = "TIME_SERIES_DAILY_ADJUSTED"


@api.route("/auth", methods=["POST"])
def auth_user():
    """Sign up user to get access token"""

    data = request.get_json()
    email = data.get("email")
    auth_validator = AuthValidator(data)

    if not auth_validator.is_valid():
        return Response(
            "name, lastname and email are required or set a valid email", 400
        )
    try:
        access_token = create_access_token(identity=email)
    except Exception as e:
        current_app.logger.exception(e)
        return Response("There was an error with auth", 500)

    response = {"email": email, "access_token": access_token}
    return Response(json.dumps(response), content_type="application/json")


@api.route("/stock_info", methods=["GET"])
@jwt_required()
def get_stock_info():
    """Sign up user to get access token"""

    data = dict(request.args)
    stock_validator = StockInfoValidator(data)
    if not stock_validator.is_valid():
        return Response("symbol parameter is required", 400)
    result = stock_api.execute(
        function=STOCK_FRECUENCY,
        apikey=current_app.config["STOCK_API"],
        symbol=data["symbol"],
    )
    stock_formatter = StockFormatter(result)
    return Response(
        json.dumps(stock_formatter.get_response()), content_type="application/json"
    )


@api.route("/health", methods=["GET"])
def health_check():
    return "OK", 200
