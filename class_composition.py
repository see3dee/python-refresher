class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def __str__(self):
        return f"weekly salary of {self.pay} with a yearly bonus of {self.bonus}"

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self, name, age, gender, pay, bonus ):
        self.name = name
        self.age = age
        self.gender = gender
        # for pay and bonus, we create a Salary object inside the Employee object
        self.obj_salary = Salary(pay, bonus)

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.gender} with a weekly pay of {self.obj_salary.pay}"

johnsal = Salary(1200, 500)
print(johnsal)

emp = Employee('Jim', 23, 'Male', 1200, 500)
print(emp)
print(f"{emp.name} has an annual salary of {emp.obj_salary.annual_salary()}")
