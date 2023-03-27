
# Python List is the data structure, used to store multiple data items with different data types. List items
# are indexed like arrays, starting from 0. Certain functions are associated with lists to carry out 
# many tasks.
# Lists are declared using square brackets and items are inserted within the territory of the brackets.
# Example of List with same data type of itmes i.e. String

my_courses = ["Physics", "Maths", "Computer Science", "Urdu", "English"]

my_courses.append("Chemistry")  # append function in list adds the item at the last index of list

print(my_courses,'\n') # Chemistry is added at the last index, as seen in the list items 

my_courses.insert(2,'Arabic') # insert functions takes the first argument as the position of the new item to be 
# inserted, and next argument is the value to be inserted at the certain defined place in the list

print(my_courses,'\n')

my_courses.pop()  # Pop function is to remove or pop the last item from the list, as done in stack. In this case,
# Chemistry value will be popped off, because it is at the last index.

print(my_courses,'\n')

# Example of Lists with Different data types

student_record = ["Jiminah", 13, '13-10-1995', 30000, "Paid"] # name, roll_no, DOB, Fee, Fee_status

# List items are also accessed with the index number

print(student_record[0],'\n')   # printing the 0th index value of the list

# Copying the list to another list using list_name.copy() function

std= student_record.copy()
print('Copied list items:  ',std,'\n')