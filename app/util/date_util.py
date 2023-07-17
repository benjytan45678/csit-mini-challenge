from datetime import datetime, timedelta

from werkzeug.exceptions import BadRequest


def formulate_date(date: str):
    try:
        date_arr = date.split("-")
        if len(date_arr) != 3:
            raise BadRequest("Date is not properly formatted!")
        yyyy, mm, dd = [int(i) for i in date_arr]
        return datetime(yyyy, mm, dd, 0, 0)
    except:
        raise BadRequest("Date is not properly formatted!")


def get_days_between(date1: datetime, date2: datetime):
    try:
        diff = date2 - date1
        if diff.days < 0:
            raise Exception()
        else:
            return diff.days + 1
    except:
        raise BadRequest("checkOutDate should be after checkInDate!")


def add_days(date: datetime, number: int):
    new_date = date + timedelta(days=number)
    return new_date
