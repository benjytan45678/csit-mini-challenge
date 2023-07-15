from flask import Blueprint

from app.database import db

flights_api_v1 = Blueprint(
    name="flights_api_v1",
    import_name="flights_api_v1",
    url_prefix="/api/v1/flights",
)


@flights_api_v1.route("/", methods=["GET"])
def get_flights():
    a = db.list_collection_names()
    print(a)
    return {"message": "you are on flights"}
