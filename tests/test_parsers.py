# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/blank.fa
    """

    fasta_file = 'data/test.fa'
    fa_parser = FastaParser(fasta_file)
    file_lines = [line for line in fa_parser]

    seq0 = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    assert file_lines[0][1] == seq0, "Something is wrong - panic!"
    
    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in 
    if a fastq file is read, the first item is None
    """
    fasta_file = 'data/test.fa'
    fa_parser = FastaParser(fasta_file)
    file_lines = [line for line in fa_parser]

    assert file_lines[0][0] != None, "This is not a fasta file"
    pass
    

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    
    fastq_file = 'data/test.fq'
    fq_parser = FastqParser(fastq_file)
    file_lines = [line for line in fq_parser]

    seq0 = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    assert file_lines[0][1] == seq0, "Something is wrong - panic!"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in.
    If this is a fasta file, the first line is None
    """

    fastq_file = 'data/test.fq'
    fq_parser = FastqParser(fastq_file)
    file_lines = [line for line in fq_parser]

    assert file_lines[0][0] != None, "This is not a fastq file"

