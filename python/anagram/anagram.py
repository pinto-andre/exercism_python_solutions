"""Function to find anagrams"""
from typing import List
def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """Function to find anagrams
    :param word: str - given word to find anagrams
    :param candidates: List[str] - List of possible anagrams
    :raises: TypeError - word must be a string
    :raises: TypeError - Only lists of strings are accepted
    :returns: List[str] - list with anagrams
"""
    if not isinstance(word, str):
        raise TypeError('word must be a string')

    if not all(isinstance(item, str) for item in candidates):
        raise TypeError('All items in the list must be strings')

    anagrams = []
    for item in candidates:
        if str(''.join(sorted(item.lower()))) == str(''.join(sorted(word.lower()))) and item.lower() != word.lower():
            anagrams.append(item)
    return anagrams
