print("----------------- this is the validation module -------------")

'this is a module '
def validatestr():
    mystr = input("Plz enter string")
    if mystr.isalpha():
        return mystr
    return validatestr()


import math
print(math.cos(math.pi))

# validatestr()