# Raising and subsequently catching errors in python:

def divide(dividend: int, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError("You can not divide by zero, silly.")
    return dividend / divisor

grades = []
# grades = [1, 3, 5, 7, 9, 'A', 67, 78,]
# grades = [1, 3, 5, 7, 9, 67, 78,]


print("let's get the average of some integers in a list")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no integers in the list, silly!")
except TypeError:
    print("you can only enter integers silly!")
else:
    print(f"The average of the list of integers is: {average}")
finally:
    print("Thanks for playing")
