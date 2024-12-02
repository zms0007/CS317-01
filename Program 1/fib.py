def fibonacci(n):
    # invalid input
    if n < 0:
        raise ValueError

    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive formula
    return fibonacci(n-1) + fibonacci(n-2)
