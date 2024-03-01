"""Function that determines how a lackadaisical teenager answers."""


def response(hey_bob):
    """Function that determines how Bob responds"""
    stripped_hey_bob = hey_bob.strip()

    if stripped_hey_bob.endswith("?") and stripped_hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if stripped_hey_bob.endswith("?"):
        return "Sure."
    if stripped_hey_bob.isupper():
        return "Whoa, chill out!"
    if stripped_hey_bob == "":
        return "Fine. Be that way!"
    return "Whatever."
