num=int(input("Enter a digit :"))
if(num%2==0):
    print("Your digit is Even")
else:
    print("Your digit is odd")

num1=int(input("Enter a first number :"))
num2=int(input("Enter a second number :"))
num3=int(input("Enter a third number :"))
if(num1>num2 and num1>num3):
    print(num1 ,"is greatest")
elif(num2>num1 and num2>num3):
    print(num2, "is greatest")
else:
    print(num3," is greatest")

num4=int(input("Enter the fourth number :"))
if(num4%7==0):
    print("The number is divisible by 7")
else:
    print("The no. is not divisible by 7")
