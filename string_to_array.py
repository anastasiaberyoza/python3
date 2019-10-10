"""It docstring of the module."""
print ('Enter string')
string = input()
def str_to_arr(string):
     """This function receives a string on input,
    and on output it gives an array of
    alphabetical chains in this string"""
    array = []
    for i, char in enumerate(string):
        if char.isalpha():
            if i == 0 or not string[i-1].isalpha():
                number = i
        if (i+1)<=(len(string)-1):
            if char.isalpha():
                if i > 0 and not string[i+1].isalpha():
                    array.append(string[number:i+1])
    if char.isalpha():
        array.append(string[number:i+1])
    return (array)
print(str_to_arr(string))
