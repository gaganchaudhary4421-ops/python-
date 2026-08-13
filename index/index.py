class car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False
    def Start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")
car1 = car()
car1.Start()