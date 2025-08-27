from collections import Counter
from typing import List

# 1. Top K Booked Listings
# Problem:
# Airbnb wants to know which listings are most popular. Given a list of bookings with listing IDs, return the top K most frequently booked listing IDs.

def top_k_listings(bookings: List[int], k: int) -> List[int]:
    # Count frequency of each listing
    counter = Counter(bookings)
    
    # Return k most common elements (returns list of tuples, we only want the listing IDs)
    return [listing_id for listing_id, _ in counter.most_common(k)]

# Test
bookings = [1001, 1002, 1001, 1003, 1002, 1001, 1004]
k = 2
print(top_k_listings(bookings, k))  # Output: [1001, 1002]