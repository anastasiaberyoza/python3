"""
This module contains different methods and a function for tokenizing a string of characters
"""
import unicodedata

class Token(object):
    """All the substrings taken from the string belong to the class 'Token'.
    Our attributes:
        token: the token itself.
        firstchar: the position of the first character.
        lastchar: the position of the last character
        category: type of the token
    """

    def __init__(self, t, cat, fchar, lchar):
        """Initializes the attributes of 'Token' class."""
        
        self.token = t
        self.category = cat
        self.firstchar = fchar
        self.lastchar = lchar

    def __repr__(self):
        """Returns the object representation."""
        return '\n{Token: ' + self.token + '; TokenType: ' + self.category + '; begin = ' + str(self.firstchar)+ '; end = ' + str(self.lastchar)+ '}'
    
class Tokenizer(object):
    """
    This class contains the methods for text tokenization.
    """
    def tokenize(self, string): 
        """ This method divides a string in a list of alphabetical substrings.
        @param string: a string 
        @return a list of alphabetical substrings (tokens)
        """
        listwords = []
        if len(string) == 0:
            return []
        else:
            for index, char in enumerate(string):
                # find the beginning of an alpha substring
                # it is either the first char in string
                # or the char that is alpha, but the previous one is not
                if char.isalpha() and (index == 0 or not string[index-1].isalpha()):
                    i = index
            
                # making sure that we didn't reach the last char of the string
                if (index+1) <= (len(string)-1):
            
                    # find the end of alpha substring and add it to list
                    if char.isalpha() and not string[index+1].isalpha():
                        listwords.append(string[i:index+1])
                
            # check the last char in the string
            # add to the list if it is alpha
            if char.isalpha():
                listwords.append(string[i:])

            return listwords

    @staticmethod
    def get_category(char):

        """ This method is used for determining categories of chars in the string """
        
        if char.isalpha():
            category = 'ALPHA'
        elif char.isdigit():
            category = 'DIGIT'
        elif char.isspace():
            category = 'SPACE'
        elif unicodedata.category(char)[0] == 'P':
            category = 'PUNCT'
        else:
            category = 'UNKNOWN FLYING OBJECT'
        return category

    def tokenize_categories(self, string):
        """
        This method tokenizes a string and
        adds token, its category, index of first and last char of substring in initial string
        it also creates an instance of class Token with attributes and prints it

        Its arguments: a string (str) to be divided into substrings; entered by a user.
        What it returns: the list of the substrings; each with its type and position
        of the first  and last character.
        """
        listwords2 = []
        if not isinstance(string, str):
            print('Error - input is not a string')
        if len(string) == 0:
            return []
        else:
            for index, char in enumerate(string):
                # determine category of char
                category = self.get_category(char)

                # find the beginning of an substring of one category
                # it is either the first char in string
                # or the char of one category, but the previous one of another
                # we save category after loops in order not to call get_category when it is unnecessary
                if index == 0:
                    i = index
                    prevcat = category
                # making sure that we didn't reach the last char of the string
                elif (index+1) < len(string):
                    # find the end of substring of one and add it to list
                    # to do so we compare categories of current and next chars
                    # if they are different - we have reached the last char of the category and we add the substring
                    if category != prevcat:
                        token = string[i:index]
                        t = Token(token, prevcat, i, index)
                        listwords2.append(t)
                        i = index
                        prevcat = category  # memorising the category

            # check the last char in the string if it wasn't checked before
            # it will be a char of another category
            # and also when all chars of the same category like 012345
            token = string[i:]
            index = index + 1  # because string[i:index] will stop slicing at index-1
            t = Token(token, category, i, index) 
            listwords2.append(t)
            
        return listwords2
    
    def tokenize_gen(self, string):
        
        """ This method generates instances of class Token
        @param string: a string
        @yield instances of class Token  - (substring, its category, first index, last index)
        """
        
        if len(string) == 0:
            return
        else:
            for index, char in enumerate(string):
                # determine category of char
                category = self.get_category(char)

                # find the beginning of an substring of one category
                # it is either the first char in string
                # or the char of one category, but the previous one of another
                # we save category after loops in order not to call get_category when it is unnecessary
                if index == 0:
                    i = index
                    prevcat = category
                # making sure that we didn't reach the last char of the string
                elif (index+1) < len(string):
                    # find the end of substring of one and add it to list
                    # to do so we compare categories of current and next chars
                    # if they are different - we have reached the last char of the category and we add the substring
                    if category != prevcat:
                        token = string[i:index]
                        t = Token(token, prevcat, i, index)
                        yield(t)
                        i = index
                        prevcat = category  # memorising the category

            # check the last char in the string if it wasn't checked before
            # it will be a char of another category
            # and also when all chars of the same category like 012345
            token = string[i:]
            index = index + 1  # because string[i:index] will stop slicing at index-1
            t = Token(token, category, i, index) 
            yield(t)

    def tokenize_gen_alpha_digit(self, string):
        """ This method generates instances of class Token only with category 'digit' or 'alpha'
        Its arguments: a string
        What it returns: instances of class Token  - substring, its category, first character, last character)
        """
        for token in self.tokenize_gen(string):
            if token.category == 'ALPHA' or token.category == 'DIGIT':
                yield token

    def __eq__(self, other):
        """ Compares two instances of class Token.
        If the attributes of the elements are equal,
        then the elements themselves are equal"""

        # Here we check whether we are dealing with an instance of class Token
        if isinstance(other, Token):
            # now we check that all attributes of these two elements are equal
            return (self.token == other.token and
                    self.category == other.category and
                    self.firstchar == other.firstchar and
                    self.lastchar == other.lastchar)
        # if the other element is not an instance of class Token, we can't compare them
        # NotImplemented is a special value which should be returned by the binary special methods
        # to indicate that the operation is not implemented with respect to the other type
        return NotImplemented


def main():
    t = Tokenizer()
    string = input()
    print("Your tokenized string:", t.tokenize(string))
    print("Generated tokens:", t.tokenize_categories(string))
    y = list(t.tokenize_gen(string))
    print("tokenize_gen:", y)
    x = list(t.tokenize_gen_alpha_digit(string))
    print("Only generated instances of alpha and digit:", x)

          
if __name__ == '__main__':
    main()
