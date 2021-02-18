class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def max_score(self):
        return max(self.grades)


student1 = Student("Rolf", (90, 89, 78, 67, 67))
student2 = Student("Tom", (94, 69, 78, 97, 67))

print(f"{student1.name}'s average grade is {student1.average()}")
print(f"{student1.name}'s highest score is {student1.max_score()}")

print(f"{student2.name}'s average grade is {student2.average()}")
print(f"{student2.name}'s highest score is {student2.max_score()}")


