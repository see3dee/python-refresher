# positional args
def print_individual_args(value1, value2):
    print(f"{value1}, {value2}")


print_individual_args({'key1': 2, 'key2': 5}, [2, 't', 5, 'h'])


# Keyword args
def print_individual_kwargs(value1=5, value2=7):
    print(f"{value1}, {value2}")


print_individual_kwargs(value1=2, value2=9)

def create_dictionary(*args):
    dict = {}
    for i, arg in enumerate(args):
        print(i, arg)
        dict[i] = arg
        print(dict)


create_dictionary(2, 5, 8, 'cat', {'key1': 2, 'key2': 7})

def print_args(*arg):
    for index, value in enumerate(args):
        print(f' here are your indexed, unpacked arguments: {index} : {value}')

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'Here are the key-value pairs of your unpacked kwargs: {key}: {value}')


# print_kwargs(dog='pet', cat='coco', rat={3: 'pop'})

def print_args_kwargs(*args, **kwargs):
    for index, value in enumerate(args):
        print(f' here are your indexed, unpacked arguments: {index} : {value}')
    for key, value in kwargs.items():
        print(f'Here are the key-value pairs of your unpacked kwargs: {key}: {value}')


print_args_kwargs(3, 2, 6, 'y', 'red', 'blue', {'key1': 'dog'}, dog='blue', cat=7, dict={1: 2, 3: 4, 5: 6})


# unpack and print a list
def print_3_things(val1, val2, val3):
    print(f'Value1 is: {val1}, Value2 is: {val2}, Value3 is: {val3}')


print_3_things('red', 'blue', 'yellow')
things = ['red', 'blue', 'yellow']
print(*things)




