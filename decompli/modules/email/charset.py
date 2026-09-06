# Module: charset
# Pseudo-source reconstructed from bytecode (no decompiler)


def add_charset(charset, header_enc, body_enc, output_charset):
    """
    Add character set properties to the global registry.
    
        charset is the input character set, and must be the canonical name of a
        character set.
    
        Optional header_enc and body_enc is either Charset.QP for
        quoted-printable, Charset.BASE64 for base64 encoding, Charset.SHORTEST for
        the shortest of qp or base64 encoding, or None for no encoding.  SHORTEST
        is only valid for header_enc.  It describes how message headers and
        message bodies in the input charset are to be encoded.  Default is no
        encoding.
    
        Optional output_charset is the character set that the output should be
        in.  Conversions will proceed from input charset, to Unicode, to the
        output charset when the method Charset.convert() is called.  The default
        is to output in the same character set as the input.
    
        Both input_charset and output_charset must have Unicode codec entries in
        the module's charset-to-codec mapping; use add_codec(charset, codecname)
        to add codecs the module does not know about.  See the codecs module's
        documentation for more information.
        
    """
    ...

def add_alias(alias, canonical):
    """
    Add a character set alias.
    
        alias is the alias name, e.g. latin-1
        canonical is the character set's canonical name, e.g. iso-8859-1
        
    """
    ...

def add_codec(charset, codecname):
    """
    Add a codec that map characters in the given charset to/from Unicode.
    
        charset is the canonical name of a character set.  codecname is the name
        of a Python codec, as appropriate for the second argument to the unicode()
        built-in, or to the encode() method of a Unicode string.
        
    """
    ...

def _encode(string, codec):
    ...

def Charset():
    """Charset"""
    ...
