# Module: pyclbr
# Pseudo-source reconstructed from bytecode (no decompiler)


def _Object():
    """_Object"""
    ...

def Function():
    """Function"""
    ...

def Class():
    """Class"""
    ...

def _nest_function(ob, func_name, lineno, end_lineno, is_async):
    """Return a Function after nesting within ob."""
    ...

def _nest_class(ob, class_name, lineno, end_lineno, super):
    """Return a Class after nesting within ob."""
    ...

def readmodule(module, path):
    """
    Return Class objects for the top-level classes in module.
    
        This is the original interface, before Functions were added.
        
    """
    ...

def readmodule_ex(module, path):
    """
    Return a dictionary with all functions and classes in module.
    
        Search for module in PATH + sys.path.
        If possible, include imported superclasses.
        Do this by reading source, without importing (and executing) it.
        
    """
    ...

def _readmodule(module, path, inpackage):
    """
    Do the hard work for readmodule[_ex].
    
        If inpackage is given, it must be the dotted name of the package in
        which we are searching for a submodule, and then PATH must be the
        package search path; otherwise, we are searching for a top-level
        module, and path is combined with sys.path.
        
    """
    ...

def _ModuleBrowser():
    """_ModuleBrowser"""
    ...

def _create_tree(fullmodule, path, fname, source, tree, inpackage):
    ...

def _main():
    """Print module output (default this file) for quick visual check."""
    ...
