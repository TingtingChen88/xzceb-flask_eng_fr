"""
This module provides translation functions
"""

from deep_translator import GoogleTranslator

def english_to_french(english_text):
    """
    Translate the given English text to French
    """
    translator = GoogleTranslator(source='en', target='fr')
    french_translation = translator.translate(english_text)
    return french_translation
def french_to_english(french_text):
    """
    Translate the given French text to Englsih
    """
    translator = GoogleTranslator(source='fr', target='en')
    english_translation = translator.translate(french_text)
    return english_translation
