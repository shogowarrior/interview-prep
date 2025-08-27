
if __name__ == '__main__':
    # Sample Input
    arr = [1, 2, 3, 4, 5]
    d = 2

    # Left Rotation
    n = len(arr)
    d = d % n
    rotated_arr = arr[d:] + arr[:d]

    # Output
    print(rotated_arr)