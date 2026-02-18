# Constructor
# All classes have a function called __init__(), which is always executed when the object is being initiated

#creating class 
class Student:
    def __init__(self,Fullname,marks):                     # The self parameter is a reference to the current instance of the class, and is used to access variable that belongs to the class
        self.name=Fullname
        self.marks=marks
        print("Adding the new student details in database...")

s1=Student("Devender",98)
print(s1.name,s1.marks)
s2=Student("Gujjar",99)
print(s2.name,s2.marks)
