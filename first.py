name = input("Apna name likho")
print("cha hal way ", name)
 


a = int(input("pehla number: "))
b = int(input("dosra number: "))

sum = a <= b
print("sum=", sum)



num = int(input("Number Likho "))

if num % 2 == 0:
    print("even Number hai")
else:
    print("Odd number hai")



num = int(input("Table ka number: "))

for i in range(1,11):
    print(num,"x", i,"=", num*i)


marks1 = int(input("Subject 1 Marks"))
marks2 = int(input("Subject 2 Marks"))
marks3 = int(input("Subject 3 Marks"))

Total = marks1 + marks2 + marks3
percentage = (Total / 300) * 100

print("Total Marks ", Total)
print("percentage", percentage)

#list 
numbers = [10,20,30,40]
print(numbers[3])

#Function
def greet(name):
    print("Assalam U Alaikum", name)

greet("Furqan")
greet("Faham")

#Simple Logic System

