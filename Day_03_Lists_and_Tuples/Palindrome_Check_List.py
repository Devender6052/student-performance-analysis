list=[1,2,3,2,1]
listcp=list.copy()  #creating a copy of list
listcp.reverse()    #revrsing the copy list
if(list==listcp):
    print("List is valid palindrome")
else:

    print("Not a palindrome")
