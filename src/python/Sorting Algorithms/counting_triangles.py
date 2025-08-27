
def count_distinct_triangles(arr):
    unique_triangles = set()
    for triangle in arr:
        # Sort side lengths to get a canonical form
        sorted_triangle = tuple(sorted(triangle))
        unique_triangles.add(sorted_triangle)
    return len(unique_triangles)



arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
output = 2
print(count_distinct_triangles(arr))

arr = [[8, 4, 6], [100, 101, 102], [84, 93, 173]]
output = 3
print(count_distinct_triangles(arr))

arr = [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
output = 1
print(count_distinct_triangles(arr))