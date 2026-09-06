# Module: sharedctypes
# Pseudo-source reconstructed from bytecode (no decompiler)


def _new_value(type_):
    ...

def RawValue(typecode_or_type, *args):
    """
    
        Returns a ctypes object allocated from shared memory
        
    """
    ...

def RawArray(typecode_or_type, size_or_initializer):
    """
    
        Returns a ctypes array allocated from shared memory
        
    """
    ...

def Value(typecode_or_type, *args, lock=None, ctx=None):
    """
    
        Return a synchronization wrapper for a Value
        
    """
    ...

def Array(typecode_or_type, size_or_initializer, *, lock=None, ctx=None):
    """
    
        Return a synchronization wrapper for a RawArray
        
    """
    ...

def copy(obj):
    ...

def synchronized(obj, lock, ctx):
    ...

def reduce_ctype(obj):
    ...

def rebuild_ctype(type_, wrapper, length):
    ...

def make_property(name):
    ...

def SynchronizedBase():
    """SynchronizedBase"""
    ...

def Synchronized():
    """Synchronized"""
    ...

def SynchronizedArray():
    """SynchronizedArray"""
    ...

def SynchronizedString():
    """SynchronizedString"""
    ...
