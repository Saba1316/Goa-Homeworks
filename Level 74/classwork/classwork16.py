# Codewars 8 kyu: Age Range Compatibility Equation



def dating_range(age):
    if age > 14:
        maximum = (age - 7) * 2
        minimum =  age / 2 + 7 
    else:
        maximum = age + 0.10 * age
        minimum = age - 0.10 * age
    return '{}-{}'.format(int(minimum), int(maximum))