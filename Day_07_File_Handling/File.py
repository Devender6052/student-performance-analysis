f=open("Day 7(File handeling)\Dev.txt","r")
#sizedata =f.read(6)    #to read the only size 
data=f.read()          #to read entire data
line1=f.readline()     #to read one line at a time
print(data)
# print(line1)
print(type(data))
f.close()

# 'r' -> open for reading(default)
# 'w' -> open for writing, tuncating the file first
# 'x' -> create a new file and open it for writing
# 'a' -> open for writing, appending to the end of the file if it exists
# 'b' -> binary mode
# 't' -> text mode(default)
# '+' -> open a disk file for updating(reading and writing)
