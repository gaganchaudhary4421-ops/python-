class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")
e1=Employee("Manager","HR",50000)
e1.showDetails()
print("Employee class is created successfully")
