student_attendance = {"Rolf": 90, "Bob": 85, "Sara": 80}
# # use the items() method for dictionaries
print(student_attendance.items())
# # apply the list method to the items object to make a list
# print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)


stud_att = list(student_attendance.items())
for t2 in stud_att:
    print(t2)

professionals = [("Bob", 24, "Artist"), ("Steve", 45, "Carpenter"), ("Sara", 45, "Engineer")]

for name, age, profession in professionals:
    print(f'{name} is {age} years old and is a {profession}')

