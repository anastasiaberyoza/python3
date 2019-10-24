import unittest
import string_to_array

class TestStringMethods(unittest.TestCase):
    
    def test_normal_string(self):
        s = 'ad b c d'
        self.assertEqual(string_to_array.str_to_arr(s), ['ad', 'b', 'c', 'd'])
        
    def test_empty_string(self):
        s = ''
        self.assertEqual(string_to_array.str_to_arr(s), [])

    def test_no_spaces_string(self):
        s = 'abv'
        self.assertEqual(string_to_array.str_to_arr(s), ['abv'])

    def test_digital_string(self):
        s = '123'
        self.assertEqual(string_to_array.str_to_arr(s), [])

    def test_delimiters_string(self):
        s = 'ad_b+c-d'
        self.assertEqual(string_to_array.str_to_arr(s), ['ad', 'b', 'c', 'd'])
        
if __name__ == '__main__':
    unittest.main()
