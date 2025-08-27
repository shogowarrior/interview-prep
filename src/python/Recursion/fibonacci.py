# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]  # Starting values for Fibonacci sequence
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Add the next number
    return fib_sequence

# Example usage
n = 10  # Number of Fibonacci numbers to generate
print(fibonacci(n))
