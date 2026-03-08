marks = int(input("Enter The Marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Your Grade is : ", grade) 

#Nesting In Conditional Statements

age = int(input("Enter The Age : "))

if(age >= 20):
    if(age >= 70):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")

#Even Odd Program

num = int(input("Enter the Number : "))

if(num%2 == 0):
    print("Even Number")
else:
    print("Odd Number")

#Finding Greadest Number
a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))
c = int(input("Enter third Number : "))
d = int(input("Enter fourth Number : "))

if(a > b and a > c and a > d ):
    print("First Number is Largest :", a)
elif(b >= c):
    print("Second Number is Largest :", b)
elif(c >= d):
    print("Third Number is Largest :", c)
else:
    print("fourth Number is Largest :", d)

#find the multiple number

x = int(input("Enter Number : "))

if(x % 8 == 0):
    print("Multiple with 8 ")
else:
    print("Nothing multiple 8")