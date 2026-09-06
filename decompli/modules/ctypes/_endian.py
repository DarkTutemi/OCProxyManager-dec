# Module: _endian
# Pseudo-source reconstructed from bytecode (no decompiler)


def _other_endian(typ):
    """
    Return the type with the 'other' byte order.  Simple types like
        c_int and so on already have __ctype_be__ and __ctype_le__
        attributes which contain the types, for more complicated types
        arrays and structures are supported.
        
    """
    ...

def _swapped_meta():
    """_swapped_meta"""
    ...

def _swapped_struct_meta():
    """_swapped_struct_meta"""
    ...

def _swapped_union_meta():
    """_swapped_union_meta"""
    ...

def BigEndianStructure():
    """BigEndianStructure"""
    ...

def BigEndianUnion():
    """BigEndianUnion"""
    ...

def LittleEndianStructure():
    """LittleEndianStructure"""
    ...

def LittleEndianUnion():
    """LittleEndianUnion"""
    ...
