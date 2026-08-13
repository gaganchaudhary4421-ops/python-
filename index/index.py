#class and instance Attributes
class student:
    school="ABC_School"
    name = "Anonymous"#class attribute
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def Avg(self):
        sum = 0
        for i in self.marks:
            sum +=i
        print("Average marks of",self.name,"is",sum/len(self.marks))
s1 = student("Amit",[90,98,37])
s1.Avg()
#Learning Static Methods