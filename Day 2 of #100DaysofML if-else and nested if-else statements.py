
# Python is case and indentation sensitive language. Brackets are mainly not used for separation in python,
# but indentation is used to separate stataments.

# If-Else Statement
print('Checking whether is the number is even or odd using if-else statament')
a=90
if a%2==0:
    print(a, " is an even number!")
else: 
    print(a, " is odd even number!")
    
print('\n')

# Nested If-Else Statement alongwith use of AND operation
print('Checking the grade of a student through marks using nested if-else statament')

marks = int(input("Enter your marks:  ")) # taking input from user and converting it into integer, because
# by default, user input will be in string

if marks>90:
    print("Student got A+ grade with ",marks, 'marks!')
elif marks>80 and marks<=90:
    print("Student got A- grade with ",marks, 'marks!')
elif marks>70 and marks<=80:
    print("Student got B grade with ",marks, 'marks!')
elif marks>60 and marks<=70:
    print("Student got C grade with ",marks, 'marks!')
elif marks>50 and marks<=60:
    print("Student got D grade with ",marks, 'marks!')
elif marks>40 and marks<=50:
    print("Student got E grade with ",marks, 'marks!')
else:
    print("Fail")