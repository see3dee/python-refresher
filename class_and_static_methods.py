class ClassTest:
    def instance_method(self):
        print(f" Instance Method has been called: {self}")  # An 'instance method' appears in a class AND uses the
        # instantiated self object as a first parameter!

#  class methods are decorated to indicate
    @classmethod
    def class_method(cls):
        print(f"Called the class method: {cls} ")

    @staticmethod
    def static_method():
        print(f"Static method called")

print(f" This is the class: {ClassTest}")
# Now, create a 1st instance of type ClassTest and label it 'obj_1'.
obj_1 = ClassTest()
print(f" This is the 1st object: {obj_1}")

# Now, create a 2nd instance of type ClassTest and label it 'obj_1'.
obj_2 = ClassTest()
print(f" This is the 2nd instance: {obj_2}")
print(" ")

# 2 Ways to call the instance or object method:
# Instance methods can only be called for an object or instance.
obj_1.instance_method()
ClassTest.instance_method(obj_1)
print(" ")
obj_2.instance_method()
ClassTest.instance_method(obj_2)
print(" ")
ClassTest.class_method()
print(" ")
ClassTest.static_method()

