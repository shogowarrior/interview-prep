def insert_sort(arr):
    n = len(arr)
    num = arr[-1]
    i = n - 2

    while(i>=0 and arr[i]>num):
        arr[i+1] = arr[i]
        print(arr)
        i -=1
    arr[i+1] = num
    print(arr)

arr = [2, 4, 6, 8, 3]
print("input:", arr)
insert_sort(arr)