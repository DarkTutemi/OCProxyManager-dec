# Module: copy
# Pseudo-source reconstructed from bytecode (no decompiler)


def Error():
    """Error"""
    ...

def copy(x):
    """
    Shallow copy operation on arbitrary Python objects.
    
        See the module's __doc__ string for more info.
        
    """
    ...

def _copy_immutable(x):
    ...

def deepcopy(x, memo, _nil):
    """
    Deep copy operation on arbitrary Python objects.
    
        See the module's __doc__ string for more info.
        
    """
    ...

def _deepcopy_atomic(x, memo):
    ...

def _deepcopy_list(x, memo, deepcopy):
    ...

def _deepcopy_tuple(x, memo, deepcopy):
    ...

def _deepcopy_dict(x, memo, deepcopy):
    ...

def _deepcopy_method(x, memo):
    ...

def _keep_alive(x, memo):
    """
    Keeps a reference to the object x in the memo.
    
        Because we remember objects by their id, we have
        to assure that possibly temporary objects are kept
        alive by referencing them.
        We store a reference at the id of the memo, which should
        normally not be used unless someone tries to deepcopy
        the memo itself...
        
    """
    ...

def _reconstruct(x, memo, func, args, state, listiter, dictiter, *, deepcopy=None):
    ...
