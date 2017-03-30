def fib(n):
    # Calculate nth fibonacci number using DP algorithm
    prev, f = 0, 1
    for i in range(2, n + 1):
        prev, f = f, prev + f
    return f
