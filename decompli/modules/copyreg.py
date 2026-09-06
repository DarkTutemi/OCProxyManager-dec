# Module: copyreg
# Pseudo-source reconstructed from bytecode (no decompiler)


def pickle(ob_type, pickle_function, constructor_ob):
    ...

def constructor(object):
    ...

def pickle_complex(c):
    ...

def pickle_union(obj):
    ...

def _reconstructor(cls, base, state):
    ...

def _reduce_ex(self, proto):
    ...

def __newobj__(cls, *args):
    ...

def __newobj_ex__(cls, args, kwargs):
    """
    Used by pickle protocol 4, instead of __newobj__ to allow classes with
        keyword-only arguments to be pickled correctly.
        
    """
    ...

def _slotnames(cls):
    """
    Return a list of slot names for a given class.
    
        This needs to find slots defined by the class and its bases, so we
        can't simply return the __slots__ attribute.  We must walk down
        the Method Resolution Order and concatenate the __slots__ of each
        class found there.  (This assumes classes don't modify their
        __slots__ attribute to misrepresent their slots after the class is
        defined.)
        
    """
    ...

def add_extension(module, name, code):
    """Register an extension code."""
    ...

def remove_extension(module, name, code):
    """Unregister an extension code.  For testing only."""
    ...

def clear_extension_cache():
    ...
