def distance(strand_a: str, strand_b: str) -> int:
    """
    Function to calculate the Hamming Distance between two DNA strands
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
