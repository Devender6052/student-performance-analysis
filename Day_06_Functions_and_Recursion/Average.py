a=int(input("Enter the first no. :"))
b=int(input("Enter the first no. :"))
c=int(input("Enter the first no. :"))

def sum(i,j,k):
    return i+j+k

def Avg(i,j,k):
    sum1=sum(a,b,c)
    return sum1/3

print("Avg of three no. is :",Avg(a,b,c))