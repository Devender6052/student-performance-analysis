# Methods : Methods are functions that belong to object

# Creating class 
class Student:
    def __init__(self,fullname):
        self.name=fullname

    def hello(self):
        print("hello",self.name)

# creating object
s1=Student("Karan")
s1.hello()