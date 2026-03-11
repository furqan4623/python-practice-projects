#Creating Lists 
marks = [85, 90, 40, 60, 80]
print(len(marks)) # Looking for Lenght of marks 
marks[0] = 65

# How to Slice in list
print(marks[0:3])
print(marks[-4:-2]) #Negative number slicing

# More builtin function in python for list
list = [50, 80, 60, 90]
list.append(100) # Add new Elements at the End 
print(list)

list.sort() # Sorts in Ascending order
print(list)

list.sort(reverse=True) # Sorts in Descending order
print(list)

list.reverse() # For reverse using
print(list)

list.insert(0, 40) # inser more element 
print(list)

list.remove(80) # Remove method in list for exact value not index value
print(list)

list.pop(2) # Remove the index value
print(list)

# Now I am start second most powerfull list with is refer by tuple and tuple is immutable function it is not change the value in indexing

