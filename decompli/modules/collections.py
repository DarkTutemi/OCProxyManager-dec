# Module: collections
# Pseudo-source reconstructed from bytecode (no decompiler)


def _OrderedDictKeysView():
    """_OrderedDictKeysView"""
    ...

def _OrderedDictItemsView():
    """_OrderedDictItemsView"""
    ...

def _OrderedDictValuesView():
    """_OrderedDictValuesView"""
    ...

def _Link():
    """_Link"""
    ...

def OrderedDict():
    """OrderedDict"""
    ...

def namedtuple(typename, field_names, *, rename=None, defaults=None, module=None):
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    
        
    """
    ...

def _count_elements(mapping, iterable):
    """Tally elements from the iterable."""
    ...

def Counter():
    """Counter"""
    ...

def ChainMap():
    """ChainMap"""
    ...

def UserDict():
    """UserDict"""
    ...

def UserList():
    """UserList"""
    ...

def UserString():
    """UserString"""
    ...
