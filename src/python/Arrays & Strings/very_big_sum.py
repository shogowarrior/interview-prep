# https://www.hackerrank.com/challenges/a-very-big-sum/problem

def check_input(n, arr):
    """
    Check if the input is valid.
    """
    if len(arr) != n:
        return False
    if not all(isinstance(num, int) for num in arr):
        return False
    return True

if __name__ == '__main__':
    # Read the number of elements in the array
    n = int(input())
    if not isinstance(n, int) or n <= 0:
        print("Invalid input size")
        exit()
    
    # Read the array elements
    arr = list(map(int, input().rstrip().split()))
    if not check_input(n, arr):
        print("Invalid input")
        exit()
       
    # Calculate the sum of the array
    result = sum(arr)

    # Print the result
    print("Result:", result)