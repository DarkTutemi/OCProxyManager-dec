# Module: enum
# Pseudo-source reconstructed from bytecode (no decompiler)


def nonmember():
    """nonmember"""
    ...

def member():
    """member"""
    ...

def _is_descriptor(obj):
    """
    
        Returns True if obj is a descriptor, False otherwise.
        
    """
    ...

def _is_dunder(name):
    """
    
        Returns True if a __dunder__ name, False otherwise.
        
    """
    ...

def _is_sunder(name):
    """
    
        Returns True if a _sunder_ name, False otherwise.
        
    """
    ...

def _is_internal_class(cls_name, obj):
    ...

def _is_private(cls_name, name):
    ...

def _is_single_bit(num):
    """
    
        True if only one bit set in num (should be an int)
        
    """
    ...

def _make_class_unpicklable(obj):
    """
    
        Make the given obj un-picklable.
    
        obj should be either a dictionary, or an Enum
        
    """
    ...

def _iter_bits_lsb(num):
    ...

def show_flag_values(value):
    ...

def bin(num, max_bits):
    """
    
        Like built-in bin(), except negative values are represented in
        twos-compliment, and the leading bit always indicates sign
        (0=positive, 1=negative).
    
        >>> bin(10)
        '0b0 1010'
        >>> bin(~10)   # ~10 is -11
        '0b1 0101'
        
    """
    ...

def _dedent(text):
    """
    
        Like textwrap.dedent.  Rewritten because we cannot import textwrap.
        
    """
    ...

def _auto_null():
    """_auto_null"""
    ...

def auto():
    """auto"""
    ...

def property():
    """property"""
    ...

def _proto_member():
    """_proto_member"""
    ...

def _EnumDict():
    """_EnumDict"""
    ...

def EnumType():
    """EnumType"""
    ...

def Enum():
    """Enum"""
    ...

def ReprEnum():
    """ReprEnum"""
    ...

def IntEnum():
    """IntEnum"""
    ...

def StrEnum():
    """StrEnum"""
    ...

def pickle_by_global_name(self, proto):
    ...

def pickle_by_enum_name(self, proto):
    ...

def FlagBoundary():
    """FlagBoundary"""
    ...

def Flag():
    """Flag"""
    ...

def IntFlag():
    """IntFlag"""
    ...

def _high_bit(value):
    """
    
        returns index of highest bit, or -1 if value is zero or negative
        
    """
    ...

def unique(enumeration):
    """
    
        Class decorator for enumerations ensuring unique member values.
        
    """
    ...

def _power_of_two(value):
    ...

def global_enum_repr(self):
    """
    
        use module.enum_name instead of class.enum_name
    
        the module is the last module in case of a multi-module name
        
    """
    ...

def global_flag_repr(self):
    """
    
        use module.flag_name instead of class.flag_name
    
        the module is the last module in case of a multi-module name
        
    """
    ...

def global_str(self):
    """
    
        use enum_name instead of class.enum_name
        
    """
    ...

def global_enum(cls, update_str):
    """
    
        decorator that makes the repr() of an enum member reference its module
        instead of its class; also exports all members to the enum's module's
        global namespace
        
    """
    ...

def _simple_enum(etype, *, boundary=None, use_args=None):
    """
    
        Class decorator that converts a normal class into an :class:`Enum`.  No
        safety checks are done, and some advanced behavior (such as
        :func:`__init_subclass__`) is not available.  Enum creation can be faster
        using :func:`simple_enum`.
    
            >>> from enum import Enum, _simple_enum
            >>> @_simple_enum(Enum)
            ... class Color:
            ...     RED = auto()
            ...     GREEN = auto()
            ...     BLUE = auto()
            >>> Color
            <enum 'Color'>
        
    """
    ...

def EnumCheck():
    """EnumCheck"""
    ...

def verify():
    """verify"""
    ...

def _test_simple_enum(checked_enum, simple_enum):
    """
    
        A function that can be used to test an enum created with :func:`_simple_enum`
        against the version created by subclassing :class:`Enum`::
    
            >>> from enum import Enum, _simple_enum, _test_simple_enum
            >>> @_simple_enum(Enum)
            ... class Color:
            ...     RED = auto()
            ...     GREEN = auto()
            ...     BLUE = auto()
            >>> class CheckedColor(Enum):
            ...     RED = auto()
            ...     GREEN = auto()
            ...     BLUE = auto()
            >>> _test_simple_enum(CheckedColor, Color)
    
        If differences are found, a :exc:`TypeError` is raised.
        
    """
    ...

def _old_convert_(etype, name, module, filter, source, *, boundary=None):
    """
    
        Create a new Enum subclass that replaces a collection of global constants
        
    """
    ...
