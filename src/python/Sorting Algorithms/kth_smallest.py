# Order statistic of an unsorted array

import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows  = [num for num in arr if num < pivot]
    highs = [num for num in arr if num > pivot]
    pivots = [num for num in arr if num == pivot]

    if k <= len(lows):
        return quickselect(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
    
arr = [3, 2, 1, 5, 4]
k = 3  # Find the 3rd smallest element
print(f"The {k} smallest element is: {quickselect(arr, k)}")