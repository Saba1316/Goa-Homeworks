# Task 3: Use a for loop to sum the numbers from 1 to 1000 but omit the numbers in the range(500, 600) (i.e. do not add the numbers from five hundred to six hundred).

sum13 = 0

for i in range(1000):
    if i in range(500,600):
        pass
    else:
        sum13 = sum13 + i

print(sum13)

# The end of task 3.