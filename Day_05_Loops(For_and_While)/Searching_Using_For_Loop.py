tuple=(1,3,4,5,23,98,67,45,100,85)
x=int(input("Enter the no. you want to find in this tuple :"))
idx=0
for val in tuple:
    if(val==x):
        print("Element found in tuple at index ",idx)
        break
    idx+=1
else:
    print("Element not found")