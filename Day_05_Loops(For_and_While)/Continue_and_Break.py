# break : Used to terminate the loop when encountered
# continue : terminates execution at the current iteration and continues execution of the loop with the next iteration
i=1
while i<=10:
    if(i==6):
        break
    print(i)
    i+=1
print("loop ended")

# for printing odd no. using continue
j=0
while j<=20:
    if(j%2==0):
        j+=1
        continue #skip
    print(j)
    j+=1
print("Odd numbers printed")