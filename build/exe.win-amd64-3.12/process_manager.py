import string
from collections import Counter

def word_frequency(text):
    """Returns a dictionary with the frequency of each word in the text.

    Args:
        text (str): A block of text provided by the user.

    Returns:
        dict: A dictionary with words as keys and their frequency as values, sorted in ascending order.
    """
    if not text:
        return {}
    
    words = text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    word_count = Counter(words)
    return dict(sorted(word_count.items(), key=lambda x: x[1]))


def show_word_frequency(text, lang):
    """Displays the most frequent words in ascending order.

    Args:
        text (str): A block of text provided by the user.
        lang (str): The chosen language ('en' or 'pt').
    """
    frequency = word_frequency(text)
    
    for word, count in frequency.items():
        print(f"'{word}': {count}")