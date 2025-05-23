class Employee:
    company : "HP"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"This is the name {self.name} and this is the salary {self.salary}"
    
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)



e = Employee("Ranveer",34000)
print(e.name,e.salary)
print(str(e))
print(repr(e))
print(len(e))