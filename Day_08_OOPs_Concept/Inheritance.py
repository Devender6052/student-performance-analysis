# When one class(child/derived) drives the properties & methods of another class(parent/base)
# Types
# 1. Single inheritance           -> parent class -> child class 
# 2. Multi-level Inheritance      -> parent class -> child class -> grand child class
# 3. Multiple Inheritance         -> parent 1 class -> child class and Parent2-> same child class
class car: #Parent class of Maruti car and grandparent of Wagon_R
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class MarutiCar(car): # child class of Car and parent of Wagon_R
    def __init__(self,Brand):
        self.Brand=Brand

class Wagon_R(MarutiCar):
    def __init__(self, type):
        self.type=type

car1=Wagon_R("CNG")

print(car1.start())
print(car1.type)

# Multi Level inheritance
class A:
    varA="Welcome to class A"

class B:
    varB="Welcome to class B"

class C(A,B):
    Varc="Welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.Varc)