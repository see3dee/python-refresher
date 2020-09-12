def hello():
    print("Hello!")

hello()

def user_age_in_seconds():
    user_age = int(input("Please enter your age: "))
    user_age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {user_age_seconds}")

user_age_in_seconds()


def add_2_numbers(x, y):  # a function with 2 PARAMETERS
    sum = x + y
    print(sum)


add_2_numbers(4, 5)
# Function with Arguments


def hello(name, surname):
    print(f"Hello {name} {surname}!!!")


hello("Bob", "Smith")

hello(surname="Smith", name="Bob")


# Order of operations
def add_friends():  # Read 1st - python creates a callable variable
    friends.append("Rolf") # NOT READ until called  # Read 4th


friends = []  # Read 2nd (Better to have global variables at the top...
# but as long as the variable exists BEFORE the function is called - it runs.
add_friends()  # Read 3rd
print(friends)  # Read 5th
