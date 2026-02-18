class Students:
    def __init__(self,name,marks):       #Marks in list form
        self.name=name
        self.marks=marks
    def avgMarks(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hello ",self.name,"your average marks is",sum/3)

s1=Students("Sneha",[88,89,97])
s1.avgMarks()

s1.name="ritik"
s1.avgMarks()