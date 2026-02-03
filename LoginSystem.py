# Correct username and password faiza
correct_username = "faizan"
correct_password = "43215"

#taking data username or password
username = input("Enter your username ")
password = input("Enter your password ")

# Logic Check
if username == correct_username or password == correct_password:
    print("Login Succesfully")
    print("Welcome", username)

else:
    print("Login failed")
    print("Wrong username or password")

