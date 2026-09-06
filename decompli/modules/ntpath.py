# Module: ntpath
# Pseudo-source reconstructed from bytecode (no decompiler)


def _get_bothseps(path):
    ...

def normcase(s):
    """
    Normalize case of pathname.
    
            Makes all characters lowercase and all slashes into backslashes.
            
    """
    ...

def isabs(s):
    """Test whether a path is absolute"""
    ...

def join(path, *paths):
    ...

def splitdrive(p):
    """
    Split a pathname into drive/UNC sharepoint and relative path specifiers.
        Returns a 2-tuple (drive_or_unc, path); either part may be empty.
    
        If you assign
            result = splitdrive(p)
        It is always true that:
            result[0] + result[1] == p
    
        If the path contained a drive letter, drive_or_unc will contain everything
        up to and including the colon.  e.g. splitdrive("c:/dir") returns ("c:", "/dir")
    
        If the path contained a UNC path, the drive_or_unc will contain the host name
        and share up to but not including the fourth directory separator character.
        e.g. splitdrive("//host/computer/dir") returns ("//host/computer", "/dir")
    
        Paths cannot contain both a drive letter and a UNC path.
    
        
    """
    ...

def split(p):
    """
    Split a pathname.
    
        Return tuple (head, tail) where tail is everything after the final slash.
        Either part may be empty.
    """
    ...

def splitext(p):
    ...

def basename(p):
    """Returns the final component of a pathname"""
    ...

def dirname(p):
    """Returns the directory component of a pathname"""
    ...

def islink(path):
    """
    Test whether a path is a symbolic link.
        This will always return false for Windows prior to 6.0.
        
    """
    ...

def lexists(path):
    """Test whether a path exists.  Returns True for broken symbolic links"""
    ...

def ismount(path):
    """
    Test whether a path is a mount point (a drive root, the root of a
        share, or a mounted volume)
    """
    ...

def expanduser(path):
    """
    Expand ~ and ~user constructs.
    
        If user or $HOME is unknown, do nothing.
    """
    ...

def expandvars(path):
    """
    Expand shell variables of the forms $var, ${var} and %var%.
    
        Unknown variables are left unchanged.
    """
    ...

def normpath(path):
    """Normalize path, eliminating double slashes, etc."""
    ...

def _abspath_fallback(path):
    """
    Return the absolute version of a path as a fallback function in case
        `nt._getfullpathname` is not available or raises OSError. See bpo-31047 for
        more.
    
        
    """
    ...

def abspath(path):
    """Return the absolute version of a path."""
    ...

def _readlink_deep(path):
    ...

def _getfinalpathname_nonstrict(path):
    ...

def realpath(path, *, strict=None):
    ...

def relpath(path, start):
    """Return a relative version of a path"""
    ...

def commonpath(paths):
    """Given a sequence of path names, returns the longest common sub-path."""
    ...
