from datetime import datetime

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
