class MyClass:
    def __init__(self, name):
        self.name = name

    def method(self):
        return f'instance method called, {self}, named: {self.name}'

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

#  Call the classmethod directly - not the instance.
print(MyClass.classmethod())


#  Now, instantiate a new object 'obj_1' with self.name = 'Bob'
obj_1 = MyClass('Bob')
#  Call the instance method against the new instance (2 ways)
print(obj_1.method())
print(MyClass.method(obj_1))
#  Call the new object's (instance) method
print(obj_1.staticmethod())

print(obj_1.classmethod())  # The classmethod only has access to the object's class.

