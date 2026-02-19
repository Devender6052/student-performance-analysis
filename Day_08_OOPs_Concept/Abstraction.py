# Hiding the implementation details of a class and only showing the essential features to the user
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.cluth=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started")

car1=car()
car1.start()