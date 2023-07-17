from flask import Blueprint, jsonify
from flask import Blueprint
from flask_pydantic import validate

from app.schema import HotelQueryModel
from app.service import read_hotel

hotel_api_v1 = Blueprint(
    name="hotel_api_v1",
    import_name="hotel_api_v1",
    url_prefix="/api/v1/hotel",
)


@hotel_api_v1.route("/", methods=["GET"])
@validate()
def get_hotel(query: HotelQueryModel):
    response = read_hotel(
        query.checkInDate, query.checkOutDate, query.destination
    )
    return response
