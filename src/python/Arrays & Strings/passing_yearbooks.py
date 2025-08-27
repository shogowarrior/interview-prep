def findSignatureCounts(arr):
    n = len(arr)
    
    # Each yearbook will get at least 1 signature (from its owner)
    signatures = [1] * n
    
    # For each student, we'll identify which cycle they're in
    # If a student is in a cycle of length k, their yearbook will get k signatures
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            # Start a new cycle
            cycle = []
            current = i
            
            # Follow the cycle until we get back to the start
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = arr[current] - 1  # Convert to 0-indexed
            
            # Everyone in this cycle will get signatures from everyone in the cycle
            cycle_length = len(cycle)
            for student in cycle:
                signatures[student] = cycle_length
    
    return signatures

# Test cases
test1 = [2, 1]
print("Test 1:", findSignatureCounts(test1))  # Expected: [2, 2]

test2 = [1, 2]
print("Test 2:", findSignatureCounts(test2))  # Expected: [1, 1]

# Additional test case
test3 = [3, 1, 2]
print("Test 3:", findSignatureCounts(test3))  # Should form a cycle of length 3

# Another test case
test4 = [1, 3, 2]
print("Test 4:", findSignatureCounts(test4))  # Should have two cycles