# Task 4: Use a while loop and make a game similar to the second task again. The numbers will be from 1 to 10 inclusive, and until the user enters the correct number, write that it is wrong, if he enters it correctly, write that it is correct.

guess = int(input("Enter your guess: "))
num = 6

while num != 6:
    print("Your guess is not right.")
