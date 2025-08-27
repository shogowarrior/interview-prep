from collections import defaultdict

def pair_sums(arr, k):
    sums = defaultdict(int)
    match = 0
    for num in arr:
        complement = k - num
        ## This ensures only the ones matching the complement will get added
        # This is the key part of the algorithm
        # If the complement exists in the sums, it means we have found pairs that sum to k
        print(sums[complement])
        match += sums[complement]
        print(f"Num: {num}, Complement: {complement}, Matches: {match}")
        sums[num] += 1
        print(f"Updated sums: {dict(sums)}")
    return match

print(pair_sums([1, 2, 3, 4, 3], 6))
print(pair_sums([1, 5, 3, 3, 3], 6))