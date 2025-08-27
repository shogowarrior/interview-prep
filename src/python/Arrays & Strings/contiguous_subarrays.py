def count_subarrays(arr):
    """
    For each index i, count the number of contiguous subarrays that:
    1. Have arr[i] as the maximum element
    2. Either start or end at index i
    
    Time Complexity: O(N) where N is the length of the input array
        - For each element, we potentially scan left and right, but each element is visited at most twice
    Space Complexity: O(N) for the result array
    
    Args:
        arr: List[int] - A non-empty list of unique integers
        
    Returns:
        List[int] - An array where each index i contains the count of valid subarrays
    """
    n = len(arr)
    
    # Arrays to store how many subarrays end at or start from each index
    left = [1] * n   # At minimum, each element forms a subarray with itself
    right = [1] * n

    # -----------------------------
    # LEFT PASS: count elements to the LEFT of each index (including i)
    # where arr[i] is the maximum in those subarrays
    # -----------------------------
    stack = []  # Will store indices in decreasing order of values
    for i in range(n):
        # Pop elements smaller than current one
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        
        if stack:
            # Distance from previous greater element
            left[i] = i - stack[-1]
        else:
            # No greater element to the left
            left[i] = i + 1

        stack.append(i)

    # -----------------------------
    # RIGHT PASS: count elements to the RIGHT of each index (including i)
    # where arr[i] is the maximum in those subarrays
    # -----------------------------
    stack = []  # Clear and reuse stack for right pass
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        if stack:
            # Distance to next greater element on the right
            right[i] = stack[-1] - i
        else:
            # No greater element to the right
            right[i] = n - i

        stack.append(i)

    # -----------------------------
    # Combine results:
    # Total subarrays = left + right - 1 (to avoid double-counting [i])
    # -----------------------------
    result = [left[i] + right[i] - 1 for i in range(n)]
    return result


# Test with the given example
arr = [3, 4, 1, 6, 2]
output = count_subarrays(arr)
print(f"Input array: {arr}")
print(f"Output: {output}")

# Let's verify with the example explanation
expected = [1, 3, 1, 5, 1]
print(f"Expected output: {expected}")
print(f"Is our output correct? {'Yes' if output == expected else 'No'}")

# Let's do a detailed check of the example
print("\nDetailed verification for each index:")

# Index 0: arr[0] = 3
# Subarrays that end at index 0 and have 3 as the maximum: [3]
# Subarrays that start at index 0 and have 3 as the maximum: [3]
# Total: 1 + 1 - 1 = 1 (subtracting 1 to avoid double-counting [3])

# Index 1: arr[1] = 4
# Subarrays that end at index 1 and have 4 as the maximum: [4], [3,4]
# Subarrays that start at index 1 and have 4 as the maximum: [4], [4,1]
# Total: 2 + 2 - 1 = 3 (subtracting 1 to avoid double-counting [4])

# Index 2: arr[2] = 1
# Subarrays that end at index 2 and have 1 as the maximum: [1]
# Subarrays that start at index 2 and have 1 as the maximum: [1]
# Total: 1 + 1 - 1 = 1 (subtracting 1 to avoid double-counting [1])

# Index 3: arr[3] = 6
# Subarrays that end at index 3 and have 6 as the maximum: [6], [1,6], [4,1,6], [3,4,1,6]
# Subarrays that start at index 3 and have 6 as the maximum: [6], [6,2]
# Total: 4 + 2 - 1 = 5 (subtracting 1 to avoid double-counting [6])

# Index 4: arr[4] = 2
# Subarrays that end at index 4 and have 2 as the maximum: [2]
# Subarrays that start at index 4 and have 2 as the maximum: [2]
# Total: 1 + 1 - 1 = 1 (subtracting 1 to avoid double-counting [2])

# Add an additional test case
arr2 = [2, 5, 3, 4, 1]
expected2 = [1, 5, 1, 3, 1]
output2 = count_subarrays(arr2)
print(f"Input array: {arr2}")
print(f"Output: {output2}")
print(f"Expected output: {expected2}")
print(f"Is our output correct? {'Yes' if output2 == expected2 else 'No'}")