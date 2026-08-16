class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "Engineering", 60000)
engg1=Engineer("Elon Musk",40)
engg1.showDetails()
 
