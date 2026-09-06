# Module: ansi
# Pseudo-source reconstructed from bytecode (no decompiler)


def _AnsiToken():
    """_AnsiToken"""
    ...

def _ansi_tokenize(ansi_text):
    """
    Tokenize a string in to plain text and ANSI codes.
    
        Args:
            ansi_text (str): A String containing ANSI codes.
    
        Yields:
            AnsiToken: A named tuple of (plain, sgr, osc)
        
    """
    ...

def AnsiDecoder():
    """AnsiDecoder"""
    ...

def read(fd):
    ...
