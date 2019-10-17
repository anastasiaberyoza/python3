"""It is docstring of the module."""

def str_to_arr(string):
     
     """This function receives a string on input,
    and on output it gives an array of
    alphabetical chains in this string"""
     
    print ('Enter string')
    string = input()
    array = []
    for i, char in enumerate(string):
        if char.isalpha():
            # the first char can be the first alphabetical char in the string
            # if so, we assign it number
            # if the previous char is not alphabetical, then we assign to our char number
            if i == 0 or not string[i-1].isalpha():
                number = i
        # Here we check, whether the char is the last one in the string
        if (i+1)<=(len(string)-1):
            if char.isalpha():
               # if char is alphapetical, i is not 0 and the next char is not alphabetical,
               # then we add this substring to our array
                if i > 0 and not string[i+1].isalpha():
                    array.append(string[number:i+1])
    # If the last char in the string is alpha, then we add it too
    if char.isalpha():
        array.append(string[number:i+1])
    return (array)
print(str_to_arr(string))
