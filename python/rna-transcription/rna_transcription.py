"""Function to make RNA transcription"""
from typing import Dict

def to_rna(dna_strand: str) -> str:
    """Function to make RNA transcription, from a given DNA string.
    
    :param dna_strand: str - Given DNA strand to transcript.
    :returns: str - Transcripted RNA.
    :raises: ValueError - There's an incorrect nucleotide in the input strand.
    :raises: TypeError - DNA strand must be a string.
    """
    if not isinstance(dna_strand, str):
        raise TypeError("DNA strand must be a string.")

    if dna_strand == "":
        return ""

    rna_transcription: Dict[str, str] = {
        "G" : "C",
        "C" : "G",
        "T" : "A",
        "A" : "U",
    }

    rna_strand = ""
    for letter in dna_strand:
        try:
            rna_strand += rna_transcription[letter]
        except KeyError as exc:
            raise ValueError(
                "There's an incorrect nucleotide in the input strand."
            ) from exc
    return rna_strand
