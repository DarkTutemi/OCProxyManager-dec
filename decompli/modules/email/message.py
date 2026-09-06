# Module: message
# Pseudo-source reconstructed from bytecode (no decompiler)


def _splitparam(param):
    ...

def _formatparam(param, value, quote):
    """
    Convenience function to format and return a key=value pair.
    
        This will quote the value if needed or if quote is true.  If value is a
        three tuple (charset, language, value), it will be encoded according
        to RFC2231 rules.  If it contains non-ascii characters it will likewise
        be encoded according to RFC2231 rules, using the utf-8 charset and
        a null language.
        
    """
    ...

def _parseparam(s):
    ...

def _unquotevalue(value):
    ...

def _decode_uu(encoded):
    """Decode uuencoded data."""
    ...

def Message():
    """Message"""
    ...

def MIMEPart():
    """MIMEPart"""
    ...

def EmailMessage():
    """EmailMessage"""
    ...
