# Module: punycode
# Pseudo-source reconstructed from bytecode (no decompiler)


def segregate(str):
    """3.1 Basic code point segregation"""
    ...

def selective_len(str, max):
    """Return the length of str, considering only characters below max."""
    ...

def selective_find(str, char, index, pos):
    """
    Return a pair (index, pos), indicating the next occurrence of
        char in str. index is the position of the character considering
        only ordinals up to and including char, and pos is the position in
        the full string. index/pos is the starting position in the full
        string.
    """
    ...

def insertion_unsort(str, extended):
    """3.2 Insertion unsort coding"""
    ...

def T(j, bias):
    ...

def generate_generalized_integer(N, bias):
    """3.3 Generalized variable-length integers"""
    ...

def adapt(delta, first, numchars):
    ...

def generate_integers(baselen, deltas):
    """3.4 Bias adaptation"""
    ...

def punycode_encode(text):
    ...

def decode_generalized_number(extended, extpos, bias, errors):
    """3.3 Generalized variable-length integers"""
    ...

def insertion_sort(base, extended, errors):
    """3.2 Insertion unsort coding"""
    ...

def punycode_decode(text, errors):
    ...

def Codec():
    """Codec"""
    ...

def IncrementalEncoder():
    """IncrementalEncoder"""
    ...

def IncrementalDecoder():
    """IncrementalDecoder"""
    ...

def StreamWriter():
    """StreamWriter"""
    ...

def StreamReader():
    """StreamReader"""
    ...

def getregentry():
    ...
