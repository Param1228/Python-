while True:
    First_Name = input("Enter your First name: ")
    if First_Name.isalpha():
        break
    else:
        print("❌ Please enter letters only!")

while True:
    Last_Name = input("Enter your Last name: ")
    if Last_Name.isalpha():
        break
    else:
        print("❌ Please enter letters only!")

print("✅ First Name:", First_Name)
print("✅ Last Name:", Last_Name)
