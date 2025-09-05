def rotation(arr, d, is_left: True):

    n = len(arr)
    d = d % n
    if not is_left:
        d = n - d

    return arr[d:] + arr[:d]



if __name__ == '__main__':
    # Sample Input
    arr = [1, 2, 3, 4, 5]
    d = 2

    print(rotation(arr, d, True))
    print(rotation(arr, d, False))