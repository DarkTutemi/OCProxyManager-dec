# Module: quopri
# Pseudo-source reconstructed from bytecode (no decompiler)


def needsquoting(c, quotetabs, header):
    """
    Decide whether a particular byte ordinal needs to be quoted.
    
        The 'quotetabs' flag indicates whether embedded tabs and spaces should be
        quoted.  Note that line-ending tabs and spaces are always encoded, as per
        RFC 1521.
        
    """
    ...

def quote(c):
    """Quote a single character."""
    ...

def encode(input, output, quotetabs, header):
    """
    Read 'input', apply quoted-printable encoding, and write to 'output'.
    
        'input' and 'output' are binary file objects. The 'quotetabs' flag
        indicates whether embedded tabs and spaces should be quoted. Note that
        line-ending tabs and spaces are always encoded, as per RFC 1521.
        The 'header' flag indicates whether we are encoding spaces as _ as per RFC
        1522.
    """
    ...

def encodestring(s, quotetabs, header):
    ...

def decode(input, output, header):
    """
    Read 'input', apply quoted-printable decoding, and write to 'output'.
        'input' and 'output' are binary file objects.
        If 'header' is true, decode underscore as space (per RFC 1522).
    """
    ...

def decodestring(s, header):
    ...

def ishex(c):
    """Return true if the byte ordinal 'c' is a hexadecimal digit in ASCII."""
    ...

def unhex(s):
    """Get the integer value of a hexadecimal number."""
    ...

def main():
    ...
