def divide(dividend: int, divisor: int) -> float:
    return dividend / divisor


print("imports_module1.py is called ", __name__)
print("looks like this gets run after import")
print(3+4)


def python_name(__name__):
    if __name__ == __main__:
        print(f"imports_module python name is {__name__}" )
    elif str(__name__) == "imports_module1":
        print(f"imports_module python name is imports_module1")
