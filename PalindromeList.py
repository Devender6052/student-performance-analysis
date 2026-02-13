list=[1,2,3,2,1]
listcp=list.copy()
listcp.reverse()
if(list==listcp):
    print("List is valid palindrome")
else:
    print("Not a palindrome")