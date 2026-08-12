#conditional Statements 
#OOPs
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

# Create an instance of the Person class
person = Person("Alice", 20)

# Check if the person is an adult
if person.is_adult():
    print(f"{person.name} is an adult.")
else:
    print("sbs")