balance = 5000
correct_pin = "1223"
attempts = 0

# 🔐 PIN Attempts System
while attempts < 3:
    pin = input("Apna 4 digit PIN dalo: ")

    if pin == correct_pin:
        print("Login Successful ✅")

        # 🔁 ATM Menu Loop
        while True:
            print("\n--- ATM Menu ---")
            print("1. Balance Check")
            print("2. Cash Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = input("Option select karo (1/2/3/4): ")

            if choice == "1":
                print("Aap ka balance hai:", balance)

            elif choice == "2":
                amount = int(input("Kitni raqam nikalni hai: "))
                if amount <= balance:
                    balance -= amount
                    print("Raqam nikal gayi ✅")
                    print("Naya balance:", balance)
                else:
                    print("Insufficient balance ❌")

            elif choice == "3":
                amount = int(input("Kitni raqam jama karni hai: "))
                balance += amount
                print("Raqam jama ho gayi ✅")
                print("Naya balance:", balance)

            elif choice == "4":
                print("Shukriya! ATM use karne ke liye 🙏")
                break

            else:
                print("Ghalat option ❌")

        break  # PIN sahi ho gaya to attempts loop se bahar

    else:
        attempts += 1
        print("Ghalat PIN ❌ | Attempts left:", 3 - attempts)

# 🔒 Agar 3 attempts khatam
if attempts == 3:
    print("Account Block ho gaya 🔒")
