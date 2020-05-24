import unittest
import tok
from tok import Tokenizer
from tok import Token

class TestTokenizerGenAlphaDigit(unittest.TestCase):  # class Tokenizer, method tokenize_gen_alpha_digit

    def setUp(self):
        self.t = Tokenizer()

    def test_empty_string(self):
        s = list(self.t.tokenize_gen_alpha_digit(''))
        self.assertEqual(len(s), 0)
        self.assertEqual(s, [])

    def test_no_spaces(self):
        s = list(self.t.tokenize_gen_alpha_digit('мамамылараму'))
        self.assertEqual(s, [Token('мамамылараму', 'alpha', 0, 12)])

    def test_first_alpha(self):
        s = list(self.t.tokenize_gen_alpha_digit('мама мыла'))
        self.assertEqual(s[0], Token("мама", "alpha", 0, 4))
        self.assertEqual(len(s), 4)

class TestTokenizerGen(unittest.TestCase):  

    def setUp(self):
        self.t = Tokenizer()

    def test_last_nonalpha(self):
        s = list(self.t.tokenize_gen('мамамылараму2'))
        self.assertEqual(len(s), 12)
        self.assertEqual(s[11], Token('мамамылараму', 'alpha', 0, 13))

    def test_first_alpha(self):
        s = list(self.t.tokenize_gen('я иду в кино'))
        self.assertEqual(s[0], Token("я", "alpha", 0, 1))
        self.assertEqual(len(s), 7)

    def test_empty_string(self):
        s = list(self.t.tokenize_gen(''))
        self.assertEqual(len(s), 0)
        self.assertEqual(s, [])

    def test_no_spaces(self):
        s = list(self.t.tokenize_gen('яидувкиноcinema'))
        self.assertEqual(s, [Token('яидувкиноcinema', 'alpha', 0, 15)])
        self.assertEqual(len(s), 1)

    def test_digital_string(self):
        s = list(self.t.tokenize_gen('012345'))
        self.assertEqual(len(s), 1)
        self.assertEqual(s, [Token('012345', 'digit', 0, 6)])
        
    def test_first_nonalpha(self):
        s = list(self.t.tokenize_gen('!!!!я иду в кино cinema'))
        self.assertEqual(len(s), 10)
        self.assertEqual(s[0], Token('!!!!', 'punct', 0, 4))

    def test_middle_nonapha(self):
        s = list(self.t.tokenize_gen('я иду в кино00000 111 00000cinema'))
        self.assertEqual(len(s), 13)
        self.assertEqual(s[7], Token('00000', 'digit', 12, 17))
        self.assertEqual(s[9], Token('111', 'digit', 18, 21))

          
if __name__ == '__main__':
    unittest.main()
