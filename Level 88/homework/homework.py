# Codewars 7 kyu: 
# Initialize my name

def initialize_names(name):
    arr = name.split()
    if len(arr) == 1:
        return arr[0]
    new_name = arr[0] + " "
    for el in arr[1:-1]:
        new_name += el[0] + ". "
    new_name = new_name + arr[-1]
    return new_name