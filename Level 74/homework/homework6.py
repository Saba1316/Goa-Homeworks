# Codewars 8 kyu: Fix the Bugs (Syntax) - My First Kata


def my_first_kata(a,b):
    #your code here
    if type(a) == int and type(b) == int:
        return a % b + b % a
    else:
        return False