# Praactice for list woth multiple data types

movies = [] # Create List
movies.append(input("Enter First Movie name : ")) # User Input in String
movies.append(input("Enter second Movie name : "))
movies.append(input("Enter third Movie name : "))

print(movies) #print value

# List copy method

list = [1, 2, 1]
list1 = [1, 2, 3]

copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("palindrome")
else:
    print("not a palindrome")

# Tuples Practice 

grade = ("A", "A", "B", "B", "C",)
print(grade.count("A")) #Counting the grade for elements chose


grade1 = ["D", "F", "B", "A", "C", "E"]
grade1.sort()
print(grade1)

