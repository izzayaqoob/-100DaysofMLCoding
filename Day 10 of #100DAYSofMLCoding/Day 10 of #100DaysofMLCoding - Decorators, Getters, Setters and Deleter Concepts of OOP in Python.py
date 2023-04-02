# Property Decorators, Getters, Setters and Deleters in OOP Python
# Decorator allows to define a method that acts like an attribute
class Employee: 
    
# attributes
    raise_amount = 1.04

 # Methods

    def __init__(self, first, last):
      self.first = first
      self.last = last
     
    @property
    def email(self):
       return '{}.{}@email.com'.format(self.first, self.last)
    
    @property # getter
    def fullname(self):
       return '{}, {}'.format(self.first, self.last)
    
    @fullname.setter #setter and it uses the getter method name with property
    def fullname(self, name):
       first, last = name.split(' ')
       self.first = first
       self.lasy = last


    @fullname.deleter # deleter
    def fullname(self):
       print("Name Deleted...")
       self.first = None
       self.last = None

    
employee_1 = Employee('John', 'Smith')
employee_1.fullname = "Izza Yaqoob" # setter is called
print(employee_1.first)
print(employee_1.email)
print(employee_1.fullname)


del employee_1.fullname


