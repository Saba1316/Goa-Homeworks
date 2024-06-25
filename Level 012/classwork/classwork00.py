# Task 1: Write the if-else condition code: if the age entered by the user is less than 13, print "You are kid", if it is greater than 13 and less than 20, print "You are teenager", if it is greater than 20, print "You are grown up"

guess = int(input("Enter your age: "))
age = 7
if age < 13:
    print("You are kid")
guess = int(input("Enter your age: "))
age = 15
if age > 13 or age < 20:
    print("You are teenager")
guess = int(input("Enter your age: "))
age = 21
if age > 20:
    print("You are grown up")
