class car:
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stopped")
class ToyotaCar(car):
     def __init__(self,name,model):
         self.name = name
         self.model = model
car1 = ToyotaCar("Toyota", "Corolla")
car2 = ToyotaCar("Toyota", "Camry")
print(car1.name, car1.model)
print(car2.name, car2.model)
         