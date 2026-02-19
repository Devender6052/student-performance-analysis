# when the same operator is allowed to have different meaning according to the context
# operator overloading of (+) plus operator
print(1+2)
print("Apna"+"College")   # concatenate
print([4,3,5,7]+[1,4,3])  # merging

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show_num(self):
        print(self.real,"i +",self.img,"j")
    
    # Dunder Function of addition
    def __add__(self,number2):
        newReal=self.real+number2.real
        newimg=self.img+number2.img
        return complex(newReal,newimg)
    
    def __sub__(self,number2):
        newReal=self.real+number2.real
        newimg=self.img+number2.img
        return complex(newReal,newimg)
    


num1=complex(3,7)
num1.show_num()
num2=complex(1,9)
num2.show_num()
num3=num1+num2
# num3=num1.add(num2)
num3.show_num()