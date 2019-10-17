"""This module provides function that tokenizes the given string"""

def str_to_arr(string):     
    """This function receives a string on input,
    and on output it gives an array of
    alphabetical chains in this string"""
     
    array = []
    for i, char in enumerate(string):
        if char.isalpha():
            # the first char can be the first alphabetical char in the string
            # if the previous char is not alphabetical, then 
            # we remember the current char as the first in the alphabetical chain
            if i == 0 or not string[i-1].isalpha():
                number = i
        # Here we check, whether the char is the last one in the string
        if (i+1)<=(len(string)-1):
            if char.isalpha():
               # if char is alphapetical, i is not 0 and the next char is not alphabetical,
               # then we add this substring to our array
                if i > 0 and not string[i+1].isalpha():
                    array.append(string[number:i+1])
    # 
    # So we check if the last char in our string is alpha
    if char.isalpha():
        array.append(string[number:i+1])
    return (array)
print ('Enter string')
string = input()
print(str_to_arr(string))
