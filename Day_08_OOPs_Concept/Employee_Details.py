class Employee:
    def __init__(self,Role,Department,salary):
        self.Role=Role
        self.Department=Department
        self.salary=salary

    def showDetails(self):
        print("Employee details are role",self.Role)
        print("Department",self.Department)
        print("salary",self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age

e1= Employee("accountant","Finance","80,000")
e1.showDetails()