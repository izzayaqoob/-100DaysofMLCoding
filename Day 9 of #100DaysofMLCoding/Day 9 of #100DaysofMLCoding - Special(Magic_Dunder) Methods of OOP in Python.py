# Magic Methods and Operator Overloading in Python
# double underscore means Dunder and the methods surrounded by a dunder are called special methods

# if init is surrounded by double underscores, it means its being surrounded by dunder
# Employee Class

class Employee: 
    # attributes
    raise_amount = 1.04

 # Methods
 # Constructor
 # dunder init is also a special method
    def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'
    def fullname(self):
       return '{}, {}'.format(self.first, self.last)

# other magic or special methods surrounded by dunder are:
    def __repr__(self):   # unambigous representation of the object used for debugging or logging etc
       return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
   
    def __str__(self) : # meaningful representation of the object
       return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other): # combining pay of two objects by special add method
       return self.pay + other.pay
    
    def __len__(self): # for checking the length or number of characters of fullname of the object
       return len(self.fullname())
    
emp_1 = Employee('Park', 'Mochi', 700000)
emp_2 = Employee('Test','Employee', 100000)
print(emp_1)

print(emp_1.__repr__)
print(emp_1.__str__)

# dunder add for adding two intergers or strings
print(int.__add__(3,4))
print(str.__add__('Izza', 'Yaqoob'))

# adding two object pays
print(emp_1 + emp_2)

