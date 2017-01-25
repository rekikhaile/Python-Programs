def combo_string(a,b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

print(combo_string('gutentag','hello'))

def combo_string(a,b):
    if len(a) < len(b):
        return a + b + a
    return b + a + b

print(combo_string('gutentag','hello'))
