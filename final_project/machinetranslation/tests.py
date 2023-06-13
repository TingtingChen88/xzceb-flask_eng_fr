import unittest
from unittest import TestCase
from translator import english_to_french, french_to_english
class TestTranslator(unittest.TestCase):
    def test_english_to_french_translation(self):
        #Test translation of 'Hello' to French
        translation = english_to_french('Merci')
        self.assertEqual(translation, 'Thank you')
        #Test translation of 'Goodbye' to French
        translation = english_to_french('Hello')
        self.assertNotEqual(translation, 'Bonjour')  
    def test_french_to_english_translation(self):
        #Test translation of 'Bonjour' to English
        translation = french_to_english('Bonjour')
        self.assertEqual(translation, 'Hello')
        #Test translation of 'Merci' to English
        translation = french_to_english('Merci')
        self.assertNotEqual(translation, 'Goodbye')
if __name__ == '__main__':
    unittest.main()
