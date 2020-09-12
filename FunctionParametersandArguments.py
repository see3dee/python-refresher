def add(x, y):  # Function with 2 parameters "x" and "y", created as variables when executed.
    result = x + y
    print(result)


# Call the function and supply ARGUMENTS: "4" and "5"
add(4, 5)
# Each ARGUMENT provides a value for each PARAMETER
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")


say_hello("Bob", "Smith")  # function with POSITIONAL argument inputs


say_hello(name="Bob", surname="Smith")  # function with Keyword or NAMED argument inputs (order does not matter now)
say_hello(surname="Smith", name="Bob")  # function with Keyword or NAMED argument inputs (order does not matter now)


#  Arguments can be POSITIONAL or can be NAMED - using Named arguments can make the code more readable.
def divide(dividend, divisor):
    if divisor != 0:
        print(f" Your result is {dividend/divisor}")
    else:
        print(f"you fool, you can't divide by {divisor}!!")


divide(5, 0)  # Positional Arguments provided
divide(divisor=5, dividend=0)  # Named or KeyWord Arguments provided


#  Default Parameter Values
def add2(x, y=5):  # "x" is a Required Parameter and "y" is an Optional Parameter
    if y == 5:
        print(f"Since y is optional and will default to 5, your total is {x + y}")
    else:
        print(f"Since you entered a value for y, your total is {x + y}")


add2(4)
add2(5, 6)



