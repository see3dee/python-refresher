# # positional args
# def print_individual_args(value1, value2):
#     print(f"{value1}, {value2}")
#
#
# print_individual_args({'key1': 2, 'key2': 5}, [2, 't', 5, 'h'])
#
#
# # Keyword args
# def print_individual_kwargs(value1=5, value2=7):
#     print(f"{value1}, {value2}")
#
#
# print_individual_kwargs(value1=2, value2=9)
#
# def create_dictionary(*args):
#     dict = {}
#     for i, arg in enumerate(args):
#         print(i, arg)
#         dict[i] = arg
#         print(dict)
#
#
# create_dictionary(2, 5, 8, 'cat', {'key1': 2, 'key2': 7})
#
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# print_kwargs(dog='pet', cat='coco', rat={3: 'pop'})


