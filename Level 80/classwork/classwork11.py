# Codewars 7 kyu: Strong password?

def check_password(s):
    conditions = [len(s)>=8 and len(s) <=20, False, False, False, False]
    for letter in s:
        if letter.isupper():
            conditions[1] = True
        elif letter.islower():
            conditions[2] = True
        elif letter.isnumeric():
            conditions[3] = True
        elif letter in '!@#$%^&*?':
            conditions[4] = True
        else:
            conditions.append(False)
    return 'valid' if all(conditions) else 'not valid'