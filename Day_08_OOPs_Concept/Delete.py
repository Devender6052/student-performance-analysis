# del keyword
# used to delete object properties or object itself

class student:
    def __init__(self,name):
        self.name=name

stu1= student("Karan")
print(stu1.name)
del stu1.name
print(stu1.name)