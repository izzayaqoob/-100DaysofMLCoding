

print('\nStudent Class and Instances (objects):')
# Class and Its instances
class Student:
   def __init__(self, name, rollno, fee, status) :
      self.name = name
      self.rollno = rollno
      self.fee = fee
      self.status = status


student_1 = Student('Izza', '13', 50000, 'Paid')

student_2 = Student('Jimin', '13', 15000, 'Paid')

print('Student 1 (instance 1) memory location: ',student_1)
print('Student 2 (instance 2) memory location: ',student_2)
print('Student 1 name: ',student_1.name)
print('Student 2 name: ',student_2.name)




print('\nEmployee Class, attributes and methods:')


class Employee: 
    # attributes
    raise_amount = 1.04
    number_of_employees = 0
 # Methods
    def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'
      Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
      self.pay = int(self.pay * self.raise_amount)
      return self.pay


emp_1 = Employee('Izza', 'Yaqoob', 700000)
emp_2 = Employee('Ramla','Kaleem', 100000)
print('Employee 1 pay: ',emp_1.pay)
print('Employee class total instances: ',Employee.number_of_employees)
print('Employee 2 pay: ',emp_2.pay)
print('Raised pay of Employee 2: ',Employee.apply_raise(emp_2))

