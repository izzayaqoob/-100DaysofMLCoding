


# Dictionary is also a dat structure used in python, and it holds the key-pair values in the memory.
# Dictionary is ordered, changeable and do not allow duplicates
# dictionary syntax:

# dictionary_name = {key: value,
# key: value, and so on so forth}
# Its indication is culry braces {} with the values in the form of key : value.

result = {
"Maths" : 56,
"Physics" : 89,
"Chemistry" : 90,
"Urdu" : 67,
"Computer Science" : 99,
}
# this is the dictionary of result in which for each key (subject name), the subject marks are stored (value).
print("Result Dictionary:  ",result,'\n')

# Some other important functions of dictionary:
## one item means one key-value pair in dictionary


#copy()	Returns a copy of the dictionary

print("Getting the specified key: ",result.get("Maths"),'\n')	#Returns the value of the specified key

print("Getting Items (key-value pair) in a list:  ",result.items(),'\n')	#Returns a list containing a tuple for each key value pair

print("Getting keys from dictionary: ",result.keys(),'\n')	#Returns a list containing the dictionary's keys

print("Getting values from dictionary: ",result.values(),'\n')	#Returns a list of all the values in the dictionary

print("Removing last item from: ",result.popitem(),'\n')	#Removes the last inserted key-value pair permanently

print("Dictionary after popping the last item: ",result,'\n')

new_pair = {"Data Science", 100}

print("Updating the dictionary with new pair: ", result.update(new_pair),'\n')	#Updates the dictionary with the specified key-value pairs

# result.pop("Maths") function will remove the element with the specified key (Maths)
