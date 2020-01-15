"""This module tokenizes the given string."""

import unicodedata

class Token(object):
    """All the substrings taken from the string belong to the class 'Token'.
    Our attributes:
        token: the token itself.
        firstchar: the position of the first character.
        tp: the type of the token ('Alpha', 'Digit', 'Space', 'Punctuation', 'Unknown Flying Object').
    What it returns: the token, its type and position of the first character.   
    """
    def __init__(self, token, firstchar, tp):
        """Initializes the attributes of 'Token' class."""
        self.token = token
        self.firstchar = firstchar
        self.tp = tp

    def __repr__(self):
        """Returns the object representation."""
        return self.token + ": " + str(self.firstchar) + str(self.tp)

class Tokenizer(object):
    """This class contains the methods for text tokenization."""
    
    @staticmethod
    def get_type(char):
        """Returns the type of the character."""
        if char.isalpha():
            return "Alpha"
        if char.isdigit():
            return "Digit"
        if char.isspace():
            return "Space"
        if unicodedata.category(char)[0] == 'P':
            return "Punctuation"
        else:
            return "Unknown Flying Object"

    def tokenize_all_substrings(self, string):
        """This function extracts tokens of different types.
        Arguments:
            a string (str) to be divided into substrings; entered by a user.
        Returns:
            the list of the substrings; each with its type and position
            of the first character.
        """
        if len(string) == 0:
            return []
        array = []
        firstchar = 0
        tp = self.get_type(string[0])
        for j, s in enumerate(string):
            current_tp = self.get_type(s)
            # if the category of one character is not the same
            # with the category of the one preceding to it,
            # we take the preceding character as the last character of the token
            # and add the token to our array
            if current_tp != self.get_type(string[j-1]) and j > 0:
                token = string[firstchar:j]
                t = Token(token, firstchar, tp)
                array.append(t)
                firstchar = j
                tp = current_tp

        # checking the last token of the string;
        # in case all the characters of the string are of the same type,
        # we also check them here and add them to the array.
        if firstchar < len(string):
            token = string[firstchar:]
            t = Token(token, firstchar, tp)
            array.append(t)

        return array
    
    def tokenize(self, string):
        """This function takes a string and returns the list of alphabetical substrings.
        
        Its arguments: a string (str) to be divided into alphabetical substrings;
        What it returns: the list of alphabetical substrings.
            
        """
        array = []
        i = 0
        for j, s in enumerate(string):
            # in case we see a character that is alphabetical
            # but the preceding one is not
            # the 'word' (i.e. an alphabetical substring)
            # begins with that alphabetical character
            if s.isalpha():
                if not string[j-1].isalpha():
                    i = j
                    
            # in case we see a character that is not alphabetical
            # (and its index is greater than 0):
            # if the preceding one is also not, we look further
            # if the preceding one is, it equals to the the end of the 'word'
            if not s.isalpha() and j > 0:
                if string[j-1].isalpha():
                    array.append(string[i:j])
                    i = j + 1
                if not string[j-1].isalpha():
                    i = j + 1

        # checking if we have reached the end of the string
        # if we have not, we keep on looking for the 'words'
        # up to the end of the string and add them to the list
        if i < len(string):
            array.append(string[i:])
    
        return array

def tokenize(string):
    """This function takes a string and returns the list of alphabetical substrings.
        
    Its arguments: a string (str) to be divided into alphabetical substrings;
    What it returns: the list of alphabetical substrings.
            
    """
    array = []
    i = 0
    for j, s in enumerate(string):
        # in case we see a character that is alphabetical
        # but the preceding one is not
        # the 'word' (i.e. an alphabetical substring)
        # begins with that alphabetical character
        if s.isalpha():
            if not string[j-1].isalpha():
                i = j
                    
        # if we see a char that is not alphabetical
        # (and its index is more than 0):
        # if the preceding char is also not, we go on 
        # if the preceding char is, it equals to the the end of the 'word'
        if not s.isalpha() and j > 0:
            if string[j-1].isalpha():
                array.append(string[i:j])
                i = j + 1
            if not string[j-1].isalpha():
                i = j + 1

    # Here we check whether we have reached the end of the string
    # if we have not, we go on looking for the 'words'
    # up to the end of the string and add them to our array
    if i < len(string):
        array.append(string[i:])
    
    return array

def main():
    tokenizer = Tokenizer()
    string = input()
    print(tokenizer.tokenize(string))
    print(tokenize(string))
    print(tokenizer.tokenize_all_substrings(string))

if __name__ == '__main__':
    main()
