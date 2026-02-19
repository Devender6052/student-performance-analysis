# super() method is used to access methods of the parent class

class car: 
    def __init__(self, type):
        self.type=type

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class MarutiCar(car): 
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

car1= MarutiCar("Wagon R", "Electric")
print(car1.type)