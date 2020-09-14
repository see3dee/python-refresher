# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades']  # Change this!
    print(f"The sum is equal to: {sum(grades)}")
    print(f"The number of grades is: {len(grades)}")
    return sum(grades) / len(grades)

print(average_grade(student))


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list

student_list = [{
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
}, {
    'name': 'James',
    'school': 'Computing',
    'grades': (67, 89, 98)
}, {
    'name': 'Bob',
    'school': 'Computing',
    'grades': (66, 67, 68)
}]
def average_grade_all_students(s_list):
    total = 0
    count = 0
    for student in s_list:
        total = total + sum(student['grades'])
        count = count + len(student['grades'])
    return total / count

average_grade_all_students(student_list)
print(average_grade_all_students(student_list))




