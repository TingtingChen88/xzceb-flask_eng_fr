"""
This module provides translation functions
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate the given English text to French
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text
def french_to_english(french_text):
    """
    Translate the given French text to Englsih
    """
    englsih_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(englsih_text)
    return englsih_text
