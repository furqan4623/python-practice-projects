def greet(name):
    print("Assalam U Alaikum", name)

greet("Furqan")

#ADD two numbers 
def add(a,b):
    return a+b

result = add(5,4)
print(result)

#marks calculation functions

def get_marks():
    m1 = int(input("Subject 1: "))
    m2 = int(input("Subject 2: "))
    m3 = int(input("Subject 3: "))
    m4 = int(input("Subject 4: "))
    m5 = int(input("Subject 5: "))
    return m1, m2, m3, m4, m5


def calculate_result(m1, m2, m3, m4, m5):
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

    return total, percentage, grade


def show_result(name, total, percentage, grade):
    print("\n--- Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)


while True:
    name = input("Student name: ")

    m1, m2, m3, m4, m5 = get_marks()

    total, percentage, grade = calculate_result(m1, m2, m3, m4, m5)

    show_result(name, total, percentage, grade)

    again = input("Check another result? (yes/no): ")
    if again.lower() != "yes":
        break


