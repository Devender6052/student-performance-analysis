# We use @property decorator on any method in the class to use the method as a property

class student:
    def __init__(self, phy, math, chem):
        self.phy=phy
        self.math=math
        self.chem=chem
        # self.percentage=str((self.math+self.chem+self.phy)/3) +"%"

    @property
    def percentage(self):
        return str((self.math+self.chem+self.phy)/3) +"%"
    
stu1=student(98,99,97)
print(stu1.percentage)

stu1.phy=89
print(stu1.percentage)
