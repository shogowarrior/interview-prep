def getBillionUsersDay(growthRates):
    # Helper function to compute total users at time t
    def total_users(t):
        return sum(g ** t for g in growthRates)

    # Set initial search bounds
    low, high = 1, 2000  # 2000 is an upper estimate; could increase if needed
    target = 1_000_000_000  # 1. billion

    # Binary search to find the minimum t that reaches or exceeds 1 billion users
    while low < high:
        mid = (low + high) // 2
        if total_users(mid) >= target:
            high = mid  # Try smaller t
        else:
            low = mid + 1  # Need more time to reach the target

    return low


growthRates = [1.5]
output = 52
print(getBillionUsersDay(growthRates))

growthRates = [1.1, 1.2, 1.3]
output = 79
print(getBillionUsersDay(growthRates))

growthRates = [1.01, 1.02]
output = 1047
print(getBillionUsersDay(growthRates))