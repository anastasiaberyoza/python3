import unittest
import string_to_array

class TestStringMethods(unittest.TestCase):
    def test_normal(self):
        s = 'ad b c d'
        self.assertEqual(string_to_array.str_to_arr(s), ['ad', 'b', 'c', 'd'])
        
    def test_with_delimiters(self):
        s = 'ad_b+c-d'
        self.assertEqual(string_to_array.str_to_arr(s), ['ad', 'b', 'c', 'd'])

    def test_spaces_only(self):
        s = '     ' #namely 5 spaces
        self.assertEqual(string_to_array.str_to_arr(s), [])

    def test_spaces_and_alpha(self):
        s = '     a' #5 spaces and alpha
        self.assertEqual(string_to_array.str_to_arr(s), ['a'])

    def test_spaces_and_number(self):
        s = '     1' #5 spaces and number
        self.assertEqual(string_to_array.str_to_arr(s), [])
        
    def test_empty(self):
        s = ''
        self.assertEqual(string_to_array.str_to_arr(s), [])

    def test_no_spaces(self):
        s = 'abv'
        self.assertEqual(string_to_array.str_to_arr(s), ['abv'])

    def test_only_numbers(self):
        s = '123'
        self.assertEqual(string_to_array.str_to_arr(s), [])
        
    def test_numbers_and_not_alpha(self):
        s = '123!@#%'
        self.assertEqual(newday.str_to_arr(s), [])
            
if __name__ == '__main__':
    unittest.main()
