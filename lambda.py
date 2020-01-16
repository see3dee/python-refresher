# add = lambda x, y: x + y
#
# sum = (add(5, 7))
# print(sum)
#
# # using lambda without naming it needs to occur in one line
#
# def double(x):
#     return x * 2


sequence = [1, 3, 5, 6, 9]
# doubled = [x * 2 for x in sequence if x > 5]  # !!! list comprehension is more Pythonic
# print(doubled)

# you CAN use the map function to accomplish the same thing more like other languages!
# doubled = list.map(double, sequence)
#  ^^using lambda^^
doubled = [(lambda x: x*2, sequence)]

print(doubled)

