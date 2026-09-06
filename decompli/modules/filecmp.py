# Module: filecmp
# Pseudo-source reconstructed from bytecode (no decompiler)


def clear_cache():
    """Clear the filecmp cache."""
    ...

def cmp(f1, f2, shallow):
    """
    Compare two files.
    
        Arguments:
    
        f1 -- First file name
    
        f2 -- Second file name
    
        shallow -- treat files as identical if their stat signatures (type, size,
                   mtime) are identical. Otherwise, files are considered different
                   if their sizes or contents differ.  [default: True]
    
        Return value:
    
        True if the files are the same, False otherwise.
    
        This function uses a cache for past comparisons and the results,
        with cache entries invalidated if their stat information
        changes.  The cache may be cleared by calling clear_cache().
    
        
    """
    ...

def _sig(st):
    ...

def _do_cmp(f1, f2):
    ...

def dircmp():
    """dircmp"""
    ...

def cmpfiles(a, b, common, shallow):
    """
    Compare common files in two directories.
    
        a, b -- directory names
        common -- list of file names found in both directories
        shallow -- if true, do comparison based solely on stat() information
    
        Returns a tuple of three lists:
          files that compare equal
          files that are different
          filenames that aren't regular files.
    
        
    """
    ...

def _cmp(a, b, sh, abs, cmp):
    ...

def _filter(flist, skip):
    ...

def demo():
    ...
