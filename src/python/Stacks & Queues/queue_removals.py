def queue_removals(arr, x):

    i = 0
    while i <= x:
        # Step 1:
        popped = arr[:x]
        max_num = max(popped)
        popped = [num-1 for num in popped if num != max_num]

def queue_removals(arr, x):
    output = []
    original_arr = arr.copy()  # To keep track of the original indices
    
    for i in range(x):
        # Step 1: Pop x elements from the front of the queue
        popped = arr[:x]
        arr = arr[x:]
        
        # Step 2: Find the maximum element and its original index
        max_num = max(popped)
        max_index = popped.index(max_num)  # The first occurrence of the max_num
        
        # Record the index of the element with the max value in the original array
        original_index = original_arr.index(popped[max_index]) + 1  # 1-based index
        output.append(original_index)
        
        # Step 3: Decrement the remaining elements and add them back to the queue
        for num in popped:
            if num != max_num:
                if num > 0:
                    arr.append(num - 1)
            else:
                arr.append(num)
    
    return output





arr = [1, 2, 2, 3, 4, 5]
x = 5
output = [5, 6, 4, 1, 2]