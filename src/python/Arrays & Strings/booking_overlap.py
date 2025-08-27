# 2. Room Availability Overlap
# Problem:
# Given a list of booking time ranges for a room, determine if a new booking can be added without overlapping.

from typing import List, Tuple

def can_book(existing: List[Tuple[int, int]], new_booking: Tuple[int, int]) -> bool:
    start, end = new_booking
    for booking in existing:
        if start < booking[1] and end > booking[0]:
            return False
    return True

# Example usage:
existing = [(1, 5), (6, 10)]
new_booking = (5, 6)
result = can_book(existing, new_booking)  # Returns True