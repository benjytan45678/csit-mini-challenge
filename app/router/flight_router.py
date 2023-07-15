from flask import Blueprint
from flask_pydantic import validate

from app.schema import FlightQueryModel
from app.service import read_flight

flight_api_v1 = Blueprint(
    name="flight_api_v1",
    import_name="flight_api_v1",
    url_prefix="/api/v1/flight",
)


@flight_api_v1.route("/", methods=["GET"])
@validate()
def get_flights(query: FlightQueryModel):
    response = read_flight(
        query.departureDate, query.returnDate, query.destination
    )
    return response
