# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    transcribe (replace DNA sequence to RNA by replacing all 'T' to 'U') in an input sequence
    """
    if reverse:
        seq = [TRANSCRIPTION_MAPPING[nuc] for nuc in seq]
        seq = "".join(seq[::-1])

    else:
        seq = seq.replace("T", "U")

    return seq


def reverse_transcribe(seq: str) -> str:
    """
    transcribe an input sequence and reverse the sequence
    """
    return transcribe(seq, reverse=True)
