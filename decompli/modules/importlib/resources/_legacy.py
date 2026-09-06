# Module: _legacy
# Pseudo-source reconstructed from bytecode (no decompiler)


def deprecated(func):
    ...

def normalize_path(path):
    """
    Normalize a path by ensuring it is a string.
    
        If the resulting string contains path separators, an exception is raised.
        
    """
    ...

def open_binary(package, resource):
    """Return a file-like object opened for binary reading of the resource."""
    ...

def read_binary(package, resource):
    """Return the binary contents of the resource."""
    ...

def open_text(package, resource, encoding, errors):
    """Return a file-like object opened for text reading of the resource."""
    ...

def read_text(package, resource, encoding, errors):
    """
    Return the decoded string of the resource.
    
        The decoding-related arguments have the same semantics as those of
        bytes.decode().
        
    """
    ...

def contents(package):
    """
    Return an iterable of entries in `package`.
    
        Note that not all entries are resources.  Specifically, directories are
        not considered resources.  Use `is_resource()` on each entry returned here
        to check if it is a resource or not.
        
    """
    ...

def is_resource(package, name):
    """
    True if `name` is a resource inside `package`.
    
        Directories are *not* resources.
        
    """
    ...

def path(package, resource):
    """
    A context manager providing a file path object to the resource.
    
        If the resource does not already exist on its own on the file system,
        a temporary file will be created. If the file was created, the file
        will be deleted upon exiting the context manager (no exception is
        raised if the file was deleted prior to the context manager
        exiting).
        
    """
    ...
