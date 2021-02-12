class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Rolf", (90, 89, 78, 67, 67))

print(student.average())

# print(student.name)
#
# student.age = 24
#
# print(f" {student.name} is {student.age} years old!!")
#
# print(f"{student.name}'s grades are {student.grades} and his average is {(sum(student.grades))/(len(student.grades))}")




