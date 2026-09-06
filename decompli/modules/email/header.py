# Module: header
# Pseudo-source reconstructed from bytecode (no decompiler)


def decode_header(header):
    """
    Decode a message header value without converting charset.
    
        Returns a list of (string, charset) pairs containing each of the decoded
        parts of the header.  Charset is None for non-encoded parts of the header,
        otherwise a lower-case string containing the name of the character set
        specified in the encoded string.
    
        header may be a string that may or may not contain RFC2047 encoded words,
        or it may be a Header object.
    
        An email.errors.HeaderParseError may be raised when certain decoding error
        occurs (e.g. a base64 decoding exception).
        
    """
    ...

def make_header(decoded_seq, maxlinelen, header_name, continuation_ws):
    """
    Create a Header from a sequence of pairs as returned by decode_header()
    
        decode_header() takes a header value string and returns a sequence of
        pairs of the format (decoded_string, charset) where charset is the string
        name of the character set.
    
        This function takes one of those sequence of pairs and returns a Header
        instance.  Optional maxlinelen, header_name, and continuation_ws are as in
        the Header constructor.
        
    """
    ...

def Header():
    """Header"""
    ...

def _ValueFormatter():
    """_ValueFormatter"""
    ...

def _Accumulator():
    """_Accumulator"""
    ...
