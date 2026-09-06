# Module: bz2
# Pseudo-source reconstructed from bytecode (no decompiler)


def BZ2File():
    """BZ2File"""
    ...

def open(filename, mode, compresslevel, encoding, errors, newline):
    """
    Open a bzip2-compressed file in binary or text mode.
    
        The filename argument can be an actual filename (a str, bytes, or
        PathLike object), or an existing file object to read from or write
        to.
    
        The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or
        "ab" for binary mode, or "rt", "wt", "xt" or "at" for text mode.
        The default mode is "rb", and the default compresslevel is 9.
    
        For binary mode, this function is equivalent to the BZ2File
        constructor: BZ2File(filename, mode, compresslevel). In this case,
        the encoding, errors and newline arguments must not be provided.
    
        For text mode, a BZ2File object is created, and wrapped in an
        io.TextIOWrapper instance with the specified encoding, error
        handling behavior, and line ending(s).
    
        
    """
    ...

def compress(data, compresslevel):
    """
    Compress a block of data.
    
        compresslevel, if given, must be a number between 1 and 9.
    
        For incremental compression, use a BZ2Compressor object instead.
        
    """
    ...

def decompress(data):
    """
    Decompress a block of data.
    
        For incremental decompression, use a BZ2Decompressor object instead.
        
    """
    ...
