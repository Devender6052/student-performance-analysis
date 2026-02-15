student1=["Dev",25230000,"three",95.6]
print(student1)

# str="Hello"
# str[0]="D"  # we can't update string becuase they are immutable

student1[0]='Karan'  # we can update coz list are mutable
print(student1)
print(len(student1))

#Slicing
#Ending index is not included
print(student1[1:2])
print(student1[:2])  # same as students1[0:2]
print(student1[2:])  # same as students1[2:len(students1)]
print(student1[-3:-1])


marks=[82,87,65,56,75,98]
# list Functions or methods

# list.append(element)   => adds one element at the end
# list.sort()            => sort the list in ascending order
# list.sort(reverse=True)=> sort the list in descending order
# list.reverse()         => Reverse the list
# list.insert(index,element) => insert the element at a specific index
# list.pop(index)            => delete that index sepcific element
# list.clear(element)        =>removes the first occurence of an element
print("Marks :",marks)
marks.append(88)
print("Marks after append:",marks)
marks.insert(2,30)
print("Marks after adding:",marks)
marks.reverse()
print("Marks after reverse :",marks)
marks.sort()
print("Marks after sorted :",marks)
marks.sort(reverse=True)
print("Marks after reverse sorted :",marks)
marks.pop(3)
print("Marks after removing 3rd index element:",marks)
