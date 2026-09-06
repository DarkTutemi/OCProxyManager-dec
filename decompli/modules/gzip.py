# Module: gzip
# Pseudo-source reconstructed from bytecode (no decompiler)


def open(filename, mode, compresslevel, encoding, errors, newline):
    """
    Open a gzip-compressed file in binary or text mode.
    
        The filename argument can be an actual filename (a str or bytes object), or
        an existing file object to read from or write to.
    
        The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
        binary mode, or "rt", "wt", "xt" or "at" for text mode. The default mode is
        "rb", and the default compresslevel is 9.
    
        For binary mode, this function is equivalent to the GzipFile constructor:
        GzipFile(filename, mode, compresslevel). In this case, the encoding, errors
        and newline arguments must not be provided.
    
        For text mode, a GzipFile object is created, and wrapped in an
        io.TextIOWrapper instance with the specified encoding, error handling
        behavior, and line ending(s).
    
        
    """
    ...

def write32u(output, value):
    ...

def _PaddedFile():
    """_PaddedFile"""
    ...

def BadGzipFile():
    """BadGzipFile"""
    ...

def GzipFile():
    """GzipFile"""
    ...

def _read_exact(fp, n):
    """
    Read exactly *n* bytes from `fp`
    
        This method is required because fp may be unbuffered,
        i.e. return short reads.
        
    """
    ...

def _read_gzip_header(fp):
    """
    Read a gzip header from `fp` and progress to the end of the header.
    
        Returns last mtime if header was present or None otherwise.
        
    """
    ...

def _GzipReader():
    """_GzipReader"""
    ...

def _create_simple_gzip_header(compresslevel, mtime):
    """
    
        Write a simple gzip header with no extra fields.
        :param compresslevel: Compresslevel used to determine the xfl bytes.
        :param mtime: The mtime (must support conversion to a 32-bit integer).
        :return: A bytes object representing the gzip header.
        
    """
    ...

def compress(data, compresslevel, *, mtime=None):
    """
    Compress data in one shot and return the compressed string.
    
        compresslevel sets the compression level in range of 0-9.
        mtime can be used to set the modification time. The modification time is
        set to the current time by default.
        
    """
    ...

def decompress(data):
    """
    Decompress a gzip compressed string in one shot.
        Return the decompressed string.
        
    """
    ...

def main():
    ...
