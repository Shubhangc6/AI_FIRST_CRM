from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine, get_db
from app.models import Interaction
from app.schemas import InteractionCreate, InteractionResponse
from typing import List
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI First CRM")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running"}


@app.post("/interactions")
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):
    new_interaction = Interaction(
        doctor_name=interaction.doctor_name,
        hospital=interaction.hospital,
        product=interaction.product,
        meeting_date=interaction.meeting_date,
        summary=interaction.summary,
        follow_up=interaction.follow_up,
    )

    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    return {
        "message": "Interaction Saved",
        "id": new_interaction.id
    }



@app.get("/interactions", response_model=List[InteractionResponse])
def get_interactions(db: Session = Depends(get_db)):
    interactions = db.query(Interaction).all()
    return interactions


@app.get("/interactions/{interaction_id}", response_model=InteractionResponse)
def get_interaction(interaction_id: int, db: Session = Depends(get_db)):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return {"message": "Interaction not found"}

    return interaction

@app.put("/interactions/{interaction_id}")
def update_interaction(
    interaction_id: int,
    updated: InteractionCreate,
    db: Session = Depends(get_db)
):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return {"message": "Interaction not found"}

    interaction.doctor_name = updated.doctor_name
    interaction.hospital = updated.hospital
    interaction.product = updated.product
    interaction.meeting_date = updated.meeting_date
    interaction.summary = updated.summary
    interaction.follow_up = updated.follow_up

    db.commit()

    return {"message": "Interaction Updated"}
@app.delete("/interactions/{interaction_id}")
def delete_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return {"message": "Interaction not found"}

    db.delete(interaction)
    db.commit()

    return {"message": "Interaction Deleted"}


