# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class
class Account:
    def __init__(self, acc_no, Pass):
        self.acc_no=acc_no
        self.__Pass=Pass      #by using double underscore(__) in front of the attribute it makes them private attribute you can't access outside the class
    
    def reset_pass(self):
        print(self.__Pass)

acc1=Account("123450","abcde")

print(acc1.acc_no)
# print(acc1.Pass)  -> It shows error because now pass is private attribute
print(acc1.reset_pass())