class Person:
    def __init__(self, name, age, hair_clr, hgt_cm):
        self.name = name
        self.age = age
        self.hair_clr = hair_clr
        self.hgt_cm = hgt_cm

    def __str__(self):
        return f"{self.name} is {self.age} years old, has {self.hair_clr} hair and is {self.hgt_cm} centimeters tall!"


bob = Person("Steve", 45, "red", 165)
steve = Person("Bob", 34, "blonde", 180)
print(bob)
print(steve)
