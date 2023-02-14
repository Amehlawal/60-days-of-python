#!/usr/bin/python3
# this exercise is taken from chapter 6 of automate the boring stuff with python
# it repeatedly asks for age and number of user until they provide valid input

while True:
    print("Enter your age:")
    age=input()
    if age.isdecimal():
        break
    print("Please enter a new number for your age.")

while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Passwords that have only letters and numbers are safer")
