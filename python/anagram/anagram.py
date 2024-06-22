def find_anagrams(word, candidates):
    anagrams = []
    for item in candidates:
        if str(''.join(sorted(item.lower()))) == str(''.join(sorted(word.lower()))) and item.lower() != word.lower():
            anagrams.append(item)
    return anagrams
