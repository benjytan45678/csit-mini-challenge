from pydantic import BaseModel


class HotelQueryModel(BaseModel):
    checkInDate: str
    checkOutDate: str
    destination: str
