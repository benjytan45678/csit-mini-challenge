from database import db
from util import formulate_date


def read_flight(departure_date: str, return_date: str, destination: str):
    departure_datetime = formulate_date(departure_date)
    return_datetime = formulate_date(return_date)

    departures = list(
        db["flights"].find(
            filter={
                "date": departure_datetime,
                "srccity": "Singapore",
                "destcity": destination,
            },
            projection=["airlinename", "price"],
        )
    )
    returns = list(
        db["flights"].find(
            filter={
                "date": return_datetime,
                "srccity": destination,
                "destcity": "Singapore",
            },
            projection=["airlinename", "price"],
        )
    )

    response = []

    for d in departures:
        for r in returns:
            hm = {
                "City": destination,
                "Departure Date": departure_date,
                "Departure Airline": d.get("airlinename", ""),
                "Departure Price": d.get("price", "NA"),
                "Return Date": return_date,
                "Return Airline": r.get("airlinename", ""),
                "Return Price": r.get("price", "NA"),
            }
            response.append(hm)

    return response
