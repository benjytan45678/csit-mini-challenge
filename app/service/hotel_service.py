from app.database import db
from app.util import formulate_date


def read_hotel(check_in_date: str, check_out_date: str, destination: str):
    check_in_datetime = formulate_date(check_in_date)
    check_out_datetime = formulate_date(check_out_date)

    aggregate_pipeline = [
        {
            "$match": {
                "city": destination,
                "date": {
                    "$gte": check_in_datetime,
                    "$lte": check_out_datetime,
                },
            }
        },
        {
            "$group": {
                "_id": "$hotelName",  # Group by hotel name
                "City": {"$first": "$city"},
                "Check In Date": {"$first": check_in_date},
                "Check Out Date": {"$first": check_out_date},
                "Hotel": {"$first": "$hotelName"},
                "Price": {"$sum": "$price"},
            }
        },
        {
            "$project": {
                "_id": 0,  # Exclude the _id field from the result
                "City": 1,
                "Check In Date": 1,
                "Check Out Date": 1,
                "Hotel": 1,
                "Price": 1,
            }
        },
        {"$sort": {"Price": 1}},
    ]

    available_hotels = list(db["hotels"].aggregate(aggregate_pipeline))
    return available_hotels
