from app.database import db
from app.util import formulate_date, get_days_between, add_days


def read_hotel(checkInDate: str, checkOutDate: str, destination: str):
    checkIn_datetime = formulate_date(checkInDate)
    checkOut_datetime = formulate_date(checkOutDate)
    no_of_days = get_days_between(checkIn_datetime, checkOut_datetime)
    response = []

    available_hotels = list(
        db["hotels"]
        .find(
            filter={"city": destination},
            projection=["hotelName"],
        )
        .distinct("hotelName")
    )

    for hotel in available_hotels:
        total_cost = 0
        for day in range(no_of_days):
            current_date = add_days(checkIn_datetime, day)
            current_entry = list(
                db["hotels"].find(
                    filter={
                        "city": destination,
                        "hotelName": hotel,
                        "date": current_date,
                    }
                )
            )
            # if the hotel does not offer any days in between the checkInDate and checkOutDate
            if len(current_entry) == 0:
                break
            current_price = current_entry[0]["price"]
            total_cost += current_price
        res = {
            "City": destination,
            "Check In Date": checkInDate,
            "Check Out Date": checkOutDate,
            "Hotel": hotel,
            "Price": total_cost,
        }
        response.append(res)
    sorted_res = sorted(response, key=lambda x: int(x["Price"]))
    return sorted_res
