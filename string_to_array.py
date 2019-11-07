"""This module provides function that tokenizes the given string"""

def str_to_arr(string):     
    """This function receives a string on input,
    and on output it gives an array of
    alphabetical chains in this string"""
     
    array = []
    number = 0
    if len(string) == 0:
        array = []
    else:
        for i, char in enumerate(string):
            if char.isalpha():
                # the first char can be the first alphabetical char in the string
                # if the previous char is not alphabetical, then 
                # we remember the current char as the first in the alphabetical chain
                if ((i == 0) or not (string[i-1].isalpha())):
                    number = i
                # if char is non-alpha nd its index is more than 0 and the previous one is alpha
                # Therefore it is the end of the alphabetical substring
                # If the previous character is non-alpha as well, we move on
            if not char.isalpha():
                if ((i > 0) and (string[i-1].isalpha())):
                    array.append(string[number:i])
                else:
                    number = i + 1
        # The part below adds the last alphabetical substring in the array
        # if the current char is alphabetical, it means that there is no char after it
        # But our cycle needs the next non-alpha char so as to add the aplhabetical substring
        if char.isalpha():
            array.append(string[number:i+1])
    return (array)
print ('Enter string')
string = input()
print(str_to_arr(string))

