# https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif

def quick_sort_1(arr):
    pivot = arr[0]

    left = []
    right = []
    middle = []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            middle.append(arr[i])
    return left + middle + right

arr = [4, 5, 3, 7, 2]
print(quick_sort_1(arr))



