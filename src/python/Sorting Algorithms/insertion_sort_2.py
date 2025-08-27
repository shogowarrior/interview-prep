# https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif

def insert_sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i] #j+1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        print(*arr)

arr = [3, 4, 7, 5, 6, 2, 1]
insert_sort(arr)

arr = [1, 4, 3, 5, 6, 2]
insert_sort(arr)