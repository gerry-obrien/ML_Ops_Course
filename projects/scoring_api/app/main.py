from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.scoring import score_apartment

app = FastAPI(title="Lab 2 - Apartment Scoring API")

class ApartmentIn(BaseModel):
    address: str = Field(..., description="The full address of the apartment")
    surface: float = Field(..., gt=0)
    rooms: int = Field(..., ge=1)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score")
def score(apartment: ApartmentIn):
    s = score_apartment(
        surface=apartment.surface,
        rooms=apartment.rooms
    )
    return {
        "address": apartment.address,
        "score": s
    }