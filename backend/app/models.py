from sqlalchemy import Column, Integer, String, Text, Date, DateTime
from sqlalchemy.sql import func
from .database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String(200))

    hospital = Column(String(200))

    product = Column(String(200))

    meeting_date = Column(Date)

    summary = Column(Text)

    follow_up = Column(Date)

    created_at = Column(DateTime(timezone=True), server_default=func.now())