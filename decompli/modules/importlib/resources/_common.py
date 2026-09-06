# Module: _common
# Pseudo-source reconstructed from bytecode (no decompiler)


def files(package):
    """
    
        Get a Traversable resource from a package
        
    """
    ...

def get_resource_reader(package):
    """
    
        Return the package's loader if it's a ResourceReader.
        
    """
    ...

def resolve(cand):
    ...

def get_package(package):
    """
    Take a package name or module object and return the module.
    
        Raise an exception if the resolved module is not a package.
        
    """
    ...

def from_package(package):
    """
    
        Return a Traversable object for the given package.
    
        
    """
    ...

def _tempfile(reader, suffix, *, _os_remove=None):
    ...

def as_file(path):
    """
    
        Given a Traversable object, return that object as a
        path on the local file system in a context manager.
        
    """
    ...

def _(path):
    """
    
        Degenerate behavior for pathlib.Path objects.
        
    """
    ...
