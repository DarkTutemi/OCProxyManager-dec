# Module: zipfile
# Pseudo-source reconstructed from bytecode (no decompiler)


def BadZipFile():
    """BadZipFile"""
    ...

def LargeZipFile():
    """LargeZipFile"""
    ...

def _strip_extra(extra, xids):
    ...

def _check_zipfile(fp):
    ...

def is_zipfile(filename):
    """
    Quickly see if a file is a ZIP file by checking the magic number.
    
        The filename argument may be a file or file-like object too.
        
    """
    ...

def _EndRecData64(fpin, offset, endrec):
    """
    
        Read the ZIP64 end-of-archive records and use that to update endrec
        
    """
    ...

def _EndRecData(fpin):
    """
    Return data from the "End of Central Directory" record, or None.
    
        The data is a list of the nine items in the ZIP "End of central dir"
        record followed by a tenth item, the file seek offset of this record.
    """
    ...

def ZipInfo():
    """ZipInfo"""
    ...

def _gen_crc(crc):
    ...

def _ZipDecrypter(pwd):
    ...

def LZMACompressor():
    """LZMACompressor"""
    ...

def LZMADecompressor():
    """LZMADecompressor"""
    ...

def _check_compression(compression):
    ...

def _get_compressor(compress_type, compresslevel):
    ...

def _get_decompressor(compress_type):
    ...

def _SharedFile():
    """_SharedFile"""
    ...

def _Tellable():
    """_Tellable"""
    ...

def ZipExtFile():
    """ZipExtFile"""
    ...

def _ZipWriteFile():
    """_ZipWriteFile"""
    ...

def ZipFile():
    """ZipFile"""
    ...

def PyZipFile():
    """PyZipFile"""
    ...

def _parents(path):
    """
    
        Given a path with elements separated by
        posixpath.sep, generate all parents of that path.
    
        >>> list(_parents('b/d'))
        ['b']
        >>> list(_parents('/b/d/'))
        ['/b']
        >>> list(_parents('b/d/f/'))
        ['b/d', 'b']
        >>> list(_parents('b'))
        []
        >>> list(_parents(''))
        []
        
    """
    ...

def _ancestry(path):
    """
    
        Given a path with elements separated by
        posixpath.sep, generate all elements of that path
    
        >>> list(_ancestry('b/d'))
        ['b/d', 'b']
        >>> list(_ancestry('/b/d/'))
        ['/b/d', '/b']
        >>> list(_ancestry('b/d/f/'))
        ['b/d/f', 'b/d', 'b']
        >>> list(_ancestry('b'))
        ['b']
        >>> list(_ancestry(''))
        []
        
    """
    ...

def _difference(minuend, subtrahend):
    """
    
        Return items in minuend not in subtrahend, retaining order
        with O(1) lookup.
        
    """
    ...

def CompleteDirs():
    """CompleteDirs"""
    ...

def FastLookup():
    """FastLookup"""
    ...

def _extract_text_encoding(encoding, *args, **kwargs):
    ...

def Path():
    """Path"""
    ...

def main(args):
    ...
