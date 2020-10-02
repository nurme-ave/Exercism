"""
Determine if a sentence is a pangram.
A pangram is a sentence using every letter of the
alphabet at least once. The best known English pangram is:

  The quick brown fox jumps over the lazy dog.
"""

from string import ascii_lowercase


def is_pangram(sentence):
    collect_letters = sorted(set([letter for letter in sentence.lower() if letter in ascii_lowercase]))
    collect_letters = "".join(collect_letters)

    return collect_letters == ascii_lowercase
  
