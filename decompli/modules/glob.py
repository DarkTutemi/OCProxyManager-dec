# Module: glob
# Pseudo-source reconstructed from bytecode (no decompiler)


def glob(pathname, *, root_dir=None, dir_fd=None, recursive=None, include_hidden=None):
    """
    Return a list of paths matching a pathname pattern.
    
        The pattern may contain simple shell-style wildcards a la
        fnmatch. Unlike fnmatch, filenames starting with a
        dot are special cases that are not matched by '*' and '?'
        patterns by default.
    
        If `include_hidden` is true, the patterns '*', '?', '**'  will match hidden
        directories.
    
        If `recursive` is true, the pattern '**' will match any files and
        zero or more directories and subdirectories.
        
    """
    ...

def iglob(pathname, *, root_dir=None, dir_fd=None, recursive=None, include_hidden=None):
    """
    Return an iterator which yields the paths matching a pathname pattern.
    
        The pattern may contain simple shell-style wildcards a la
        fnmatch. However, unlike fnmatch, filenames starting with a
        dot are special cases that are not matched by '*' and '?'
        patterns.
    
        If recursive is true, the pattern '**' will match any files and
        zero or more directories and subdirectories.
        
    """
    ...

def _iglob(pathname, root_dir, dir_fd, recursive, dironly, include_hidden):
    ...

def _glob1(dirname, pattern, dir_fd, dironly, include_hidden):
    ...

def _glob0(dirname, basename, dir_fd, dironly, include_hidden):
    ...

def glob0(dirname, pattern):
    ...

def glob1(dirname, pattern):
    ...

def _glob2(dirname, pattern, dir_fd, dironly, include_hidden):
    ...

def _iterdir(dirname, dir_fd, dironly):
    ...

def _listdir(dirname, dir_fd, dironly):
    ...

def _rlistdir(dirname, dir_fd, dironly, include_hidden):
    ...

def _lexists(pathname, dir_fd):
    ...

def _isdir(pathname, dir_fd):
    ...

def _join(dirname, basename):
    ...

def has_magic(s):
    ...

def _ishidden(path):
    ...

def _isrecursive(pattern):
    ...

def escape(pathname):
    """
    Escape all special characters.
        
    """
    ...
