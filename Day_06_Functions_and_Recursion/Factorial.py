j=int(input("Enter the no. :"))
def fact(n):
    facto=1
    while n>=1:
        facto*=n
        n-=1
    return facto

print("Factorial of no.",j," is :",fact(j)) 