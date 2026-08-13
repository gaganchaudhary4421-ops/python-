#class and instance Attributes
class student:
    school="ABC_School"
    name = "Anonymous"#class attribute
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1 = student("Amit",90)
s1.hello()