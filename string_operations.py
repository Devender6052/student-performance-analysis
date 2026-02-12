# #Escape sequence Character
# new line= \n
# tab space= \t
str="dev is a good boy"
str1='feature hai ki nahi'
str2='''Heloo baby.\nHow \tare you'''
print(str2)

# concatenation= sum of two strings
d='Hello'
b='Dev'
c=b+d
print(c)
print(len(str)) #length of the string

# we can't manipulate the string or character by using indexing but we can access
print(str[4])
# str[4]='a' (This is not valid)

# Slicing = accessing part of string
print(str1[3:8])
print(str[:8]) # str[0:8]
print(str[3:]) # str[3:len(str)]
