
# Inheritance in Python

# Employee Class

class Employee: 
    # attributes
    raise_amount = 1.04
    number_of_employees = 0
 
 # Methods
 # Constructor
    def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'
      Employee.number_of_employees += 1

# Implementation of Regular methods
# A regular method automatically takes object or instance as its first argument called as self. 
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
      self.pay = int(self.pay * self.raise_amount)
      return self.pay


emp_1 = Employee('Park', 'Mochi', 700000)
emp_2 = Employee('Test','Employee', 100000)
print(emp_1.email)
print(emp_2.email)

# Inherting Developer Class from Employee Class
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, programming_lang):   
      super().__init__(first, last, pay) # letting Employee class handle first name, last name and pay for restricting the code from duplication
      self.programming_lang = programming_lang


print(help(Developer)) # contains all the information about the Developer Class

# every class in python inherits default from object class
# method resolution order means when a subclass object is created and some function or constructor is called,
# at first order, interpreter will check the required thing in the original class, in case of absence of the required thing, the inheritance chain is checked


dev_1 = Developer('Yashma', 'Sahar', 783678, 'Python' )
dev_2= Developer('Test', 'Developer', 56748, 'Java' )

print('Developer 1 email: ', dev_1.email)
print('Developer 1 programming language: ',dev_1.programming_lang)


# Inherting Manager Class from Employee Class
class Manager(Employee):
   def __init__(self, first, last, pay, employees = None):   
      super().__init__(first, last, pay) 
      if employees is None:
         self.employees = []
      else:
         self.employees = employees

   def add_emp(self, emp):
      if emp not in self.employees:
         self.employees.append(emp)

   def remove_emp(self, emp):
      if emp in self.employees:
         self.employees.remove(emp)
    
   def print_emps(self):
      for emp in self.employees:
         print('-->', emp.fullname())
    


manager_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(manager_1.email)

manager_1.add_emp(dev_2)

manager_1.print_emps()

manager_1.remove(dev_1)

manager_1.print_emps()

isinstance()   # tells that whether the object is instance of the class or not

print(isinstance(manager_1, Employee))
print(isinstance(manager_1, Developer))

print(issubclass(Manager, Developer))  # tells whether the class is subclass of the other or not
