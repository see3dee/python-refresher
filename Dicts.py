friends_ages = {"Rolf": 30, "Bob": 45, "Sara": 50}

for friend in friends_ages:
    print(f"{friend} is {friends_ages[friend]} years old")

print(friends_ages)
print(friends_ages.items())
flist = (list(friends_ages.items()))
for f in flist:
    print(f)

print(friends_ages.values())
print(friends_ages.keys())

for friend, age in friends_ages.items():
    print(f"{friend} is {age} years old")

if "John" in friends_ages:
    print("John attended the school")
else:
    print("John did not attend")

ave_age = sum(friends_ages.values()) / len(friends_ages)
print(f"The average age of my friends is {ave_age}")

# lsit of