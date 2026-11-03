def calculate(a, b, operation):
    """Perform addition of two numbers."""
    if operation == "+":
        return a + b
    raise ValueError("Only addition (+) is supported.")
