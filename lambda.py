# Lambda keyword to create anonymous functions
lambda x, y: x + y  # 1. lambda Keyword, 2. Parameters,  3. ":" , 4. Return Value
# you CAN name the anonymous function
add = lambda x, y: x + y
sum = (add(5, 7))
print(sum)

# using lambda without naming it needs to occur in one line
#
def double(x):
    return x * 2


sequence = [1, 3, 5, 6, 9]
doubled1 = [x * 2 for x in sequence if x > 5]  # !!! list comprehension is more Pythonic
doubled2 = [double(x) for x in sequence]  # !!! list comprehension is more Pythonic
print(doubled1)
print(doubled2)

# you CAN ALSO use the map function to accomplish the same thing more like other languages!
# And this is where the lambda expression is really useful!!
# doubled = list.map(double, sequence)
#  ^^using lambda^^
# doubled = list(map(double, sequence))
doubled = list(map(lambda x: x*2, sequence))

print(doubled)

