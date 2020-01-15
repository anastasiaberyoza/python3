import unittest
import tok0

class TestTokenizeAllSubstrings(unittest.TestCase):

    def setUp(self):
        self.x = tok0.Tokenizer()

    def test_list_output(self):
        string = 'мама washed the 345 раму'
        result = self.x.tokenize_all_substrings(string)
        self.assertIsInstance(result, list)

    def test_empty_input(self):
        string = ''
        result = self.x.tokenize_all_substrings(string)
        self.assertEqual(result, [])

    def test_nonalphabetical_string(self):
        string = '!123-45.67?'
        result = self.x.tokenize_all_substrings(string)
        self.assertEqual(result[0].token, '!')
        self.assertEqual(result[0].firstchar, 0)
        self.assertEqual(result[0].tp, 'Punctuation')
        self.assertEqual(result[1].token, '123')
        self.assertEqual(result[1].firstchar, 1)
        self.assertEqual(result[1].tp, 'Digit')
        self.assertEqual(result[6].token, '?')
        self.assertEqual(result[6].firstchar, 10)
        self.assertEqual(result[6].tp, 'Punctuation')

    def test_alphabetical_string(self):
        string = 'мамамылараму'
        result = self.x.tokenize_all_substrings(string)
        self.assertEqual(result[0].token, 'мамамылараму')
        self.assertEqual(result[0].firstchar, 0)
        self.assertEqual(result[0].tp, 'Alpha')

    def test_nonalphabetic_ending(self):
        string = 'some alphabetic string??? алфавитная цепочка'
        result = self.x.tokenize_all_substrings(string)
        self.assertEqual(result[0].token, 'some')
        self.assertEqual(result[0].firstchar, 0)
        self.assertEqual(result[0].tp, 'Alpha')
        self.assertEqual(result[5].token, '???')
        self.assertEqual(result[5].firstchar, 22)
        self.assertEqual(result[5].tp, 'Punctuation')
        self.assertEqual(result[7].token, 'алфавитная')
        self.assertEqual(result[7].firstchar, 26)
        self.assertEqual(result[7].tp, 'Alpha')

    def test_all_types_string(self):
        string = '1a/.P я'
        result = self.x.tokenize_all_substrings(string)
        self.assertEqual(result[0].token, '1')
        self.assertEqual(result[0].firstchar, 0)
        self.assertEqual(result[0].tp, 'Digit')
        self.assertEqual(result[2].token, '/.')
        self.assertEqual(result[2].firstchar, 2)
        self.assertEqual(result[2].tp, 'Punctuation')
        self.assertEqual(result[3].token, 'P')
        self.assertEqual(result[3].firstchar, 4)
        self.assertEqual(result[3].tp, 'Alpha')
        self.assertEqual(result[4].token, ' ')
        self.assertEqual(result[4].firstchar, 5)
        self.assertEqual(result[4].tp, 'Space')
        self.assertEqual(result[5].token, 'я')
        self.assertEqual(result[5].firstchar, 6)
        self.assertEqual(result[5].tp, 'Alpha')
        
class TestTokenize(unittest.TestCase):

    def setUp(self):
        self.x = tok0.Tokenizer()

    def test_list_output(self):
        string = 'some alphabetic string'
        result = self.x.tokenize(string)
        self.assertIsInstance(result, list)

    def test_empty_input(self):
        string = ''
        result = self.x.tokenize(string)
        self.assertEqual(result, [])

    def test_nonalphabetical_string(self):
        string = '/999-99-99/'
        result = self.x.tokenize(string)
        self.assertEqual(result, [])

    def test_alphabetical_string(self):
        # tests not only strings consisting purely of alphabetical characters,
        # but also alphabetical strings with spaces and punctuation marks
        string = 'somealphabeticstring'
        result = self.x.tokenize(string)
        self.assertEqual(result, ['somealphabeticstring'])
        string = 'some - alphabetic - string'
        result = self.x.tokenize(string)
        self.assertEqual(result, ['some', 'alphabetic', 'string'])
        
    def test_nonalphabetical_ending(self):
        string = 'some alphabetic string   '
        result = self.x.tokenize(string)
        self.assertEqual(result, ['some', 'alphabetic', 'string'])

    def test_nonalphabetical_beginning(self):
        string = '   some alphabetic string'
        result = self.x.tokenize(string)
        self.assertEqual(result, ['some', 'alphabetic', 'string'])

class TestFuncTokenize(unittest.TestCase):
    
    def test_list_output(self):
        string = 'some alphabetic string'
        result = tok0.tokenize(string)
        self.assertIsInstance(result, list)

    def test_empty_input(self):
        string = ''
        result = tok0.tokenize(string)
        self.assertEqual(result, [])

    def test_nonalphabetical_string(self):
        string = '/999-99-99/'
        result = tok0.tokenize(string)
        self.assertEqual(result, [])

    def test_alphabetical_string(self):
        string = 'somealphabeticstring'
        result = tok0.tokenize(string)
        self.assertEqual(result, ['somealphabeticstring'])
        string = 'some - alphabetic - string'
        result = tok0.tokenize(string)
        self.assertEqual(result, ['some', 'alphabetic', 'string'])
        
    def test_nonalphabetical_beginning(self):
        string = 'some alphabetic string   '
        result = tok0.tokenize(string)
        self.assertEqual(result, ['some', 'alphabetic', 'string'])

    def test_nonalphabetical_ending(self):
        string = '   some alphabetic string'
        result = tok0.tokenize(string)
        self.assertEqual(result, ['some', 'alphabetic', 'string'])

if __name__ == '__main__':
    unittest.main()
