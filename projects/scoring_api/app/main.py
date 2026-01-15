
from typing import Union

from fastapi import FastAPI

from scoring import *

app = FastAPI()

@app.get("/score")
def score(address: str, surface: float, number_rooms: int):
    score = get_score(address, surface, number_rooms)
    return {"score": score, "address": address}
