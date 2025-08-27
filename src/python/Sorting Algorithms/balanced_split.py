def balanced_splits(arr):
    # Early return: can't split arrays with fewer than 2 elements
    if len(arr) < 2:
        return False

    # Step 1: Sort the array to make "strictly smaller" check easy
    arr.sort()

    # Step 2: Calculate total sum
    total_sum = sum(arr)

    # Step 3: If the total sum is odd, we can't split it evenly
    if total_sum % 2 != 0:
        return False

    # Step 4: Initialize running sum for the left half
    left_sum = 0

    # Step 5: Iterate through potential split points
    for i in range(len(arr) - 1):
        left_sum += arr[i]

        # Check if this split gives equal halves
        if left_sum * 2 == total_sum:
            # Ensure the max of left < min of right
            if arr[i] < arr[i + 1]:
                return True
            else:
                # Equal values violate the strictly smaller condition
                return False

    # Step 6: No valid split found
    return False
    
    

arr = [1, 5, 7, 1]
output = True
print(balanced_splits(arr))

arr = [12, 7, 6, 7, 6]
output = False
print(balanced_splits(arr))
