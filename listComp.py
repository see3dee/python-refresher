# Simple
numbers = [1, 3, 5]
doubled = [num*2 for num in numbers]
print(doubled)

# With filter
friends = ["Rolf", "Bob", "Sara", "Smith", "Lucy"]
starts_s = [f for f in friends if f.startswith('S')]

print(friends)
print(starts_s)

print("friends: ", id(friends), "starts_s: ", id(starts_s))
print(f"friends:  {id(friends)} starts_s:  {id(starts_s)}")

emptydict = {}

print(emptydict)
print(type(emptydict))

emptyset = set()
print(emptyset)
print(type(emptyset))


