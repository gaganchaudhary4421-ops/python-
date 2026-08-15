class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def CalculatePercentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
stud1=student(98,77,67)
print(stud1.CalculatePercentage)
