#  Using functions as variables to be passed around

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can NOT be zero, silly!")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)

print(result)
