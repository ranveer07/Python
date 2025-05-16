class Employee():

    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary} the bond is for {self.bond}.")


e1 = Employee(40000,"Ranveer",4)

e1.get_info()