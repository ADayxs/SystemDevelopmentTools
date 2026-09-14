def add(a, b):
    """Return the sum of a and b."""
    return a + b

def divide(a, b):
    """Return a divided by b. Raises ValueError on zero divisor."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    """Return n! for non-negative integer n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
