# Module: types
# Pseudo-source reconstructed from bytecode (no decompiler)


def _f():
    ...

def _cell_factory():
    ...

def _g():
    ...

async def _c():
    ...

async def _ag():
    ...

def _C():
    """_C"""
    ...

def new_class(name, bases, kwds, exec_body):
    """Create a class object dynamically using the appropriate metaclass."""
    ...

def resolve_bases(bases):
    """Resolve MRO entries dynamically as specified by PEP 560."""
    ...

def prepare_class(name, bases, kwds):
    """
    Call the __prepare__ method of the appropriate metaclass.
    
        Returns (metaclass, namespace, kwds) as a 3-tuple
    
        *metaclass* is the appropriate metaclass
        *namespace* is the prepared class namespace
        *kwds* is an updated copy of the passed in kwds argument with any
        'metaclass' entry removed. If no kwds argument is passed in, this will
        be an empty dict.
        
    """
    ...

def _calculate_meta(meta, bases):
    """Calculate the most derived metaclass."""
    ...

def DynamicClassAttribute():
    """DynamicClassAttribute"""
    ...

def _GeneratorWrapper():
    """_GeneratorWrapper"""
    ...

def coroutine(func):
    """Convert regular generator function to a coroutine."""
    ...
