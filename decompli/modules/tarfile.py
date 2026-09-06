# Module: tarfile
# Pseudo-source reconstructed from bytecode (no decompiler)


def stn(s, length, encoding, errors):
    """
    Convert a string to a null-terminated bytes object.
        
    """
    ...

def nts(s, encoding, errors):
    """
    Convert a null-terminated bytes object to a string.
        
    """
    ...

def nti(s):
    """
    Convert a number field to a python number.
        
    """
    ...

def itn(n, digits, format):
    """
    Convert a python number to a number field.
        
    """
    ...

def calc_chksums(buf):
    """
    Calculate the checksum for a member's header by summing up all
           characters except for the chksum field which is treated as if
           it was filled with spaces. According to the GNU tar sources,
           some tars (Sun and NeXT) calculate chksum with signed char,
           which will be different if there are chars in the buffer with
           the high bit set. So we calculate two checksums, unsigned and
           signed.
        
    """
    ...

def copyfileobj(src, dst, length, exception, bufsize):
    """
    Copy length bytes from fileobj src to fileobj dst.
           If length is None, copy the entire content.
        
    """
    ...

def _safe_print(s):
    ...

def TarError():
    """TarError"""
    ...

def ExtractError():
    """ExtractError"""
    ...

def ReadError():
    """ReadError"""
    ...

def CompressionError():
    """CompressionError"""
    ...

def StreamError():
    """StreamError"""
    ...

def HeaderError():
    """HeaderError"""
    ...

def EmptyHeaderError():
    """EmptyHeaderError"""
    ...

def TruncatedHeaderError():
    """TruncatedHeaderError"""
    ...

def EOFHeaderError():
    """EOFHeaderError"""
    ...

def InvalidHeaderError():
    """InvalidHeaderError"""
    ...

def SubsequentHeaderError():
    """SubsequentHeaderError"""
    ...

def _LowLevelFile():
    """_LowLevelFile"""
    ...

def _Stream():
    """_Stream"""
    ...

def _StreamProxy():
    """_StreamProxy"""
    ...

def _FileInFile():
    """_FileInFile"""
    ...

def ExFileObject():
    """ExFileObject"""
    ...

def FilterError():
    """FilterError"""
    ...

def AbsolutePathError():
    """AbsolutePathError"""
    ...

def OutsideDestinationError():
    """OutsideDestinationError"""
    ...

def SpecialFileError():
    """SpecialFileError"""
    ...

def AbsoluteLinkError():
    """AbsoluteLinkError"""
    ...

def LinkOutsideDestinationError():
    """LinkOutsideDestinationError"""
    ...

def _get_filtered_attrs(member, dest_path, for_data):
    ...

def fully_trusted_filter(member, dest_path):
    ...

def tar_filter(member, dest_path):
    ...

def data_filter(member, dest_path):
    ...

def TarInfo():
    """TarInfo"""
    ...

def TarFile():
    """TarFile"""
    ...

def is_tarfile(name):
    """
    Return True if name points to a tar archive that we
           are able to handle, else return False.
    
           'name' should be a string, file, or file-like object.
        
    """
    ...

def main():
    ...
