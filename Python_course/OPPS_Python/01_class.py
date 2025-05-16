#class : Class is a blueprint or a template. Form for a exam that contains name, age , electives, father 's name etc

#Object: Specific instance created from the template. Eg data created for Ranveer

class Employee:
    company = "HP"
    def get_salary(self):        # self is important because self is a way to reference the object of the class which is being created.
        return 34000

e1 = Employee()
print(e1.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)

