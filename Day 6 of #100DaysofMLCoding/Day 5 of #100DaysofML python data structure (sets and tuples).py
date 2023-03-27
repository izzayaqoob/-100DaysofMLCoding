# Sets
# Python sets can store variables of multiple data types but cannot store mutable elements 
#(lists, dictionary and tuples). Sets are unordered (non-index), unchangeable and duplicate values are removed. Sets are also defined within curly braces {}.
set1 = {12, 56, 67, 67, 89} 
print("Set 1: ", set1,'\n')

set2 = {34,89,90,35,90,76}  #duplicate values would be removed
print("Set 2: ", set2,'\n')

print("Intersection of set1 and set2: ", set1.intersection(set2),'\n')

set1.add(123)
print("Set1 after adding an element: ",set1,'\n')

set3 = set1.copy() # copying set1 items to set3
print("Set3: ",set3,'\n')

set1.discard(89) 
print("Set1 after discarding 89 value: ", set1,'\n')

print("Difference of Set2 and Set3: ",set2.difference(set3),'\n')


# Tuples
# A tuple is a collection of objects which ordered and immutable. 
# Tuples are indexed, just like lists. 
# The differences between tuples and lists are, the tuples cannot be changed unlike lists.
# Tuples use parentheses as indication or for its definition.

vehicles_tuple = ('Audi', 'Corolla', 'Cultus','Balleno', 'Mehran', 'City', 'Balleno', 'Land Cruiser')

print("Tuple: ", vehicles_tuple,'\n')

print("Some other functions of tuples \n")

print("Getting tuple class item : ",vehicles_tuple.__class_getitem__('Corolla'),'\n')

print("Count of Balleno in tuple: ", vehicles_tuple.count("Balleno"),'\n') # returns the count of value (how many times it occurred in tuple)

index = vehicles_tuple.index('Cultus') # index function searches the tuple for a specified value and returns the position of where it was found

print("Position at which Cultus is saved in tuple: ", index, '\n')

# making another tuple
tuple2 = (0,4,5,8,9,0)

print("Tuple2: ",tuple2,'\n')
#adding two tuples

tuple3 = vehicles_tuple + tuple2
print("Tuple3 is the addition of vehicles_tuple and tuple2: ",tuple3,'\n')
# Tuples can not be updated!

# deleting tuple 2
del tuple2;





























