tuple=(1,3,4,5,23,98,67,45,100,85)
x=int(input("Enter the no. you want to find in this tuple"))
i=0
while(i<len(tuple)):
    if(tuple[i]==x):
        print("Element found in tuple at index ",i)
        break
    i+=1
else:
    print("Element not found")