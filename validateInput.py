while True:
    print("Enter your age:")
    age=input()
    if age.isdecimal():
        break
    print("Please enter a new number for your age.")

while True:
    print("Select a new password (letters and numbers):")
    password = input()
    if password.isalnum():
        break
    print("Passwords that have only letters and numbers are safer")