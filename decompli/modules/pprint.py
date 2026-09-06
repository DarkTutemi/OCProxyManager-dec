# Module: pprint
# Pseudo-source reconstructed from bytecode (no decompiler)


def pprint(object, stream, indent, width, depth, *, compact=None, sort_dicts=None, underscore_numbers=None):
    """Pretty-print a Python object to a stream [default is sys.stdout]."""
    ...

def pformat(object, indent, width, depth, *, compact=None, sort_dicts=None, underscore_numbers=None):
    """Format a Python object into a pretty-printed representation."""
    ...

def pp(object, *args, sort_dicts=None, **kwargs):
    """Pretty-print a Python object"""
    ...

def saferepr(object):
    """Version of repr() which can handle recursive data structures."""
    ...

def isreadable(object):
    """Determine if saferepr(object) is readable by eval()."""
    ...

def isrecursive(object):
    """Determine if object requires a recursive representation."""
    ...

def _safe_key():
    """_safe_key"""
    ...

def _safe_tuple(t):
    """Helper function for comparing 2-tuples"""
    ...

def PrettyPrinter():
    """PrettyPrinter"""
    ...

def _recursion(object):
    ...

def _perfcheck(object):
    ...

def _wrap_bytes_repr(object, width, allowance):
    ...
