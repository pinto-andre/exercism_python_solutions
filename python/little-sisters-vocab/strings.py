"""Functions for creating, transforming, and adding prefixes to strings."""
from typing import List

def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un" + word


def make_word_groups(vocab_words: List[str]) -> str:
    """Transform a list containing a prefix and words into a string with the prefix 
    followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    words_with_prefixes = [vocab_words[0]]
    for word in vocab_words[1:]:
        words_with_prefixes.append(words_with_prefixes[0] + word)
    return " :: ".join(words_with_prefixes)


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    word_without_suffix = word[:-4]

    if word_without_suffix.endswith("i"):
        return word_without_suffix[:-1] + "y"
    return word_without_suffix


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.
    :raises: ValueError - index corresponds to an element inexistent in the sentence

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    try:
        result_sentence = sentence

        if result_sentence.endswith("."):
            result_sentence = sentence[:-1]
        return result_sentence.split()[index] + "en"
    except IndexError as excuse:
        raise ValueError("Index corresponds to an element inexistent in the sentence") from excuse
