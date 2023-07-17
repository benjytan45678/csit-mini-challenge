from flask import Blueprint, jsonify

from app.database import db

hotels_api_v1 = Blueprint(
    name="hotels_api_v1",
    import_name="hotels_api_v1",
    url_prefix="/api/v1/hotels",
)


@hotels_api_v1.route("/", methods=["GET"])
def get_hotels():
    collection = db.get_collection("hotels")
    projection = {"city": 1, "hotelName": 1, "price": 1, "_id": 0}
    documents = collection.find({}, projection)
    return jsonify(list(documents))
