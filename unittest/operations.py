def sum(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def basic_operations(a, b, operation=''):
    if operation == 'sum':
        return a + b
    elif operation == 'multiply':
        return a * b
    elif operation == 'subtract':
        return a - b
    elif operation == 'divide':
        return a / b
    return 'Unknown operation'
