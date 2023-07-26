from pydantic import BaseModel


class FlightQueryModel(BaseModel):
    departureDate: str
    returnDate: str
    destination: str
