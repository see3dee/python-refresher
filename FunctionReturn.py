# Functions return None by default (unless a return is defined for that function)
def newadd(x, y):  # Read 1st
    print(x + y)  # Read 3rd (Prints result)


newadd(5, 13)  # Read 2nd
result = newadd(5, 13)  # Read 4th (Prints result again since function was called)
print(result)  # Read 5th  # prints "None" the value of the function after it is execute - no return defined!!


def add(x,y):
    if (x+y) >= 10:
        print(f"Looks like x + y is greater or equal to 10: {x + y}")
        return x + y
    else:
        print(f"Looks like x + y is less than 10: {x + y}")
        return x + y


add(6, 5)

