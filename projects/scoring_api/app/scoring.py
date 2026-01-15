def get_score(address: str, surface: float, number_rooms: int) -> float:
    score = surface * number_rooms * 1000 / number_rooms
    return score