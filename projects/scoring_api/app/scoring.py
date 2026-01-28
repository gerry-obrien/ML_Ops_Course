def score_apartment(surface: float, rooms: int) -> float:

    perfect_size = 100.0 
    perfect_room_count = 4
    
    size_score = min(surface / perfect_size, 1.0)
    room_score = min(rooms / perfect_room_count, 1.0)

    final_result = (size_score + room_score) / 2
    
    return round(final_result, 2)