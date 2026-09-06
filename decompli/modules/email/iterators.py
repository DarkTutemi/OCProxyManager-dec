# Module: iterators
# Pseudo-source reconstructed from bytecode (no decompiler)


def walk(self):
    """
    Walk over the message tree, yielding each subpart.
    
        The walk is performed in depth-first order.  This method is a
        generator.
        
    """
    ...

def body_line_iterator(msg, decode):
    """
    Iterate over the parts, returning string payloads line-by-line.
    
        Optional decode (default False) is passed through to .get_payload().
        
    """
    ...

def typed_subpart_iterator(msg, maintype, subtype):
    """
    Iterate over the subparts with a given MIME type.
    
        Use `maintype' as the main MIME type to match against; this defaults to
        "text".  Optional `subtype' is the MIME subtype to match against; if
        omitted, only the main type is matched.
        
    """
    ...

def _structure(msg, fp, level, include_default):
    """A handy debugging aid"""
    ...
