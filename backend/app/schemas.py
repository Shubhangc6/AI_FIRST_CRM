from pydantic import BaseModel
from datetime import date


class InteractionCreate(BaseModel):
    doctor_name: str
    hospital: str
    product: str
    meeting_date: date
    summary: str
    follow_up: date


class InteractionResponse(InteractionCreate):
    id: int

    class Config:
        from_attributes = True