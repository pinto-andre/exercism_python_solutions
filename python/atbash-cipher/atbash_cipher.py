PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"
NUMBERS = "0123456789"

def encode(plain_text: str) -> str:
    """
    Function used to enconde any string according to Atbash Cipher
    """
    # Prepare text: lowercase and filter out invalid characters
    use_text = "".join(char for char in plain_text.lower() if char in PLAIN + NUMBERS)

    # Initialize placeholder for encoded text
    placeholder = []

    # Encode each character using the CIPHER or keep NUMBERS as-is
    for char in use_text:
        if char in PLAIN:
            placeholder.append(CIPHER[PLAIN.index(char)])
        elif char in NUMBERS:
            placeholder.append(char)

    # Group into chunks of 5 characters
    grouped_placeholder = ["".join(placeholder[i:i+5]) for i in range(0, len(placeholder), 5)]

    # Return the encoded string
    return " ".join(grouped_placeholder).strip()  # Strip to remove trailing space


def decode(ciphered_text: str) -> str:
    """
    Function used to decode any string previously enconded according to Atbash Cipher
    """
    # Prepare text: lowercase and filter out invalid characters
    use_text = ciphered_text.replace(" ", "")

    # Initialize placeholder for encoded text
    placeholder = []

    # Encode each character using the CIPHER or keep NUMBERS as-is
    for char in use_text:
        if char in CIPHER:
            placeholder.append(PLAIN[CIPHER.index(char)])
        elif char in NUMBERS:
            placeholder.append(char)

    # Return the decoded string
    return "".join(placeholder)
