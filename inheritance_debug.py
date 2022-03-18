"3- the 2 classes have constructors"
'interpreter check if the class contain __init__ method not , if it contains the constructor ? it will be called if not it will check if the parent class has constructor and call it.'
# class Person:
#     def __init__(self,name):
#         self.name =name
#
# class Employee(Person):
#     def __init__(self):
#         print("Employee created")
#
# # e = Employee("Ahmed")
# e =  Employee()
# print("test")

class AA:
    def __init__(self, var1=1):
        print("AA constructor called")
        self.var1 = var1

class BB:
    def __init__(self, var2=2):
        print("BB constructor called")
        self.var2 = var2


class CC(AA, BB):
    def __init__(self):
        super().__init__()  # calling the AA Constructor
        BB.__init__(self,"cc value")

newobj = CC()
print(newobj.var1)
print(newobj.var2)