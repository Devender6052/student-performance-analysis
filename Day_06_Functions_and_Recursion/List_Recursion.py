marks =[10,20,30,98,40,89]
def printu(list,index):
    if(index==len(list)):
        return
    print(list[index])
    printu(list,index+1)
    
printu(marks,0)
