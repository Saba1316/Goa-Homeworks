# Task 6: Enter a number for the user and tell if it is odd or even. (hints: 10 % 2 = 0; 5 % 2 = 1).

number = int(input("Enter your number: "))

if number % 5 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")