""" Set of functions to translate any string into pig latin. """
def translate_word(word: str) -> str:
    """
    Auxiliary function to process single words to pig latin
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Rule 1: Word starts with a vowel, 'xr', or 'yt'
    if word[0] in vowels or word[:2] == 'xr' or word[:2] == 'yt':
        return word + 'ay'

    # Rule 3: Word starts with 'qu'
    if word[:2] == 'qu':
        return word[2:] + word[:2] + 'ay'
    # Rule 3: Word starts with 'qu' with a preceding consonant
    if word[1:3] == 'qu':
        return word[3:] + word[0:3] + 'ay'

    # Rule 4: Word starts with consonants followed by 'y'
    if 'y' in word[1:] and word[0] != 't':
        idx = word.index('y')
        return word[idx:] + word[:idx] + 'ay'

    # Rule 2: Word starts with consonants
    for i, char in enumerate(word):
        if char in vowels:
            return word[i:] + word[:i] + 'ay'

    # If no vowels found (this shouldn't happen in case of valid input), 
    # just return the word with 'ay'
    return word + 'ay'


def translate(text: str) -> str:
    """
    Function to actually translate the problems input into pig latin, using the auxiliary function
    """
    # Check if the word contains spaces (i.e., it's multiple words)
    if ' ' not in text:
        # Single word translation
        return translate_word(text)
    else:
        # Multiple words translation
        words = text.split(' ')
        new_words = []
        for single_word in words:
            new_words.append(translate_word(single_word))
        return ' '.join(new_words)
    