# Module: encodings
# Pseudo-source reconstructed from bytecode (no decompiler)


def CodecRegistryError():
    """CodecRegistryError"""
    ...

def normalize_encoding(encoding):
    """
     Normalize an encoding name.
    
            Normalization works as follows: all non-alphanumeric
            characters except the dot used for Python package names are
            collapsed and replaced with a single underscore, e.g. '  -;#'
            becomes '_'. Leading and trailing underscores are removed.
    
            Note that encoding names should be ASCII only.
    
        
    """
    ...

def search_function(encoding):
    ...

def _alias_mbcs(encoding):
    ...
