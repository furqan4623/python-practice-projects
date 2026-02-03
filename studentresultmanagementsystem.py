#Given a Student Name
name = input("Write a Student Name: ")
print("Student Name:", name)


#Subject Marks
m1 = int(input("Physics Marks "))
m2 = int(input("Math Marks "))
m3 = int(input("Programming  Marks "))
m4 = int(input("Intro to Business Marks "))
m5 = int(input("Database Management Marks "))

#Finding Total
total = m1 + m2 + m3 + m4 + m5
print("Total Marks: ", total)

#Finding Percentage
percentage = (total / 500)* 100
print("Total Percentage: ", percentage)

#Grading Calculation 

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"

else:
    grade = "Fail"

print("Grade:", grade)


# All Program in Loop for Try again
while True:
    name = input("\nStudent ka naam likho: ")

    m1 = int(input("Physics  marks: "))
    m2 = int(input("Math 2 marks: "))
    m3 = int(input("Programming 3 marks: "))
    m4 = int(input("Intro to Business 4 marks: "))
    m5 = int(input("Database Management 5 marks: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    else:
        grade = "Fail"

    print("\n--- Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    again = input("\nKya dobara check karna hai? (yes/no): ")

    if again.lower() != "yes":
        break
