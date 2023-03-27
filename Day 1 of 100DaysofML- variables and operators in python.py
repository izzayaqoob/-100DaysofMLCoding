

# In Python, variables are defined without specifying the datatypes. Datatype of the variable is assigned
# automatically when a variable is created, according to its assigned value.

number_of_courses = 7    #intger type variable
height = 5.5             #float type variable
course_name = "Data Science"  #String type variable
is_enrolled = True             #bool type variable


# Printing the Values of Variables with the Print statement

# In print statement,  arguments are separated by a comma
print("Number of Courses:  ", number_of_courses) # in this, a string is concatenated with the value of a variable, separated by comma
print("Course name is:  ", course_name)
print("My height:  ", height)
print("Is Enrolled in Courses?  ", is_enrolled)

print('\n')

# Printing the Datatypes of the above variables, assigned in Python
print("number_of_courses variable datatype:  ",type(number_of_courses))
print('\n')
print("height variable datatype:  ",type(height))
print('\n')
print("Course_name variable datatype:  ",type(course_name))
print('\n')
print("is_enrolled variable datatype:  ",type(is_enrolled))
print('\n')



# Operators in Python

# Arithmetic Operators:   (+, -, /, *, %)
# Other operators:    (+= (for increment), or, nor, and, a**b (means a power b / exponent operators), a//b (for getting
# interger value when a number gets divided by other / integer Quotient)))

a = 16 #int variable
b = 9 #int variable

print("Applying Arithmetic operators:\n")

print(a+b)   #addition
print(a-b) #subtraction
print(a/b)  #a divided by b
print(a*b)  # a multiply b
print(a**b)  #(a power b)
print(a%b)  #a modulus b (remainder)
print(a//b)  #integer quotient (16/9 = 1.7777 while 16//9 means only taking value before point i.e. 1)
print('\n')

print("Applying AND/OR operators:\n")
# AND operator:
if a>3 and b<=9:
    print("Pass")
else: 
    print("Fail")

# OR operator:
if a>30 or b>90:
    print("Pass")
else: 
    print("Fail")
print('\n')