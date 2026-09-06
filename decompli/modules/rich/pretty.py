# Module: pretty
# Pseudo-source reconstructed from bytecode (no decompiler)


def _is_attr_object(obj):
    """Check if an object was created with attrs module."""
    ...

def _get_attr_fields(obj):
    """Get fields for an attrs object."""
    ...

def _is_dataclass_repr(obj):
    """
    Check if an instance of a dataclass contains the default repr.
    
        Args:
            obj (object): A dataclass instance.
    
        Returns:
            bool: True if the default repr is used, False if there is a custom repr.
        
    """
    ...

def _has_default_namedtuple_repr(obj):
    """
    Check if an instance of namedtuple contains the default repr
    
        Args:
            obj (object): A namedtuple
    
        Returns:
            bool: True if the default repr is used, False if there's a custom repr.
        
    """
    ...

def _ipy_display_hook(value, console, overflow, crop, indent_guides, max_length, max_string, max_depth, expand_all):
    ...

def _safe_isinstance(obj, class_or_tuple):
    """isinstance can fail in rare cases, for example types with no __class__"""
    ...

def install(console, overflow, crop, indent_guides, max_length, max_string, max_depth, expand_all):
    """
    Install automatic pretty printing in the Python REPL.
    
        Args:
            console (Console, optional): Console instance or ``None`` to use global console. Defaults to None.
            overflow (Optional[OverflowMethod], optional): Overflow method. Defaults to "ignore".
            crop (Optional[bool], optional): Enable cropping of long lines. Defaults to False.
            indent_guides (bool, optional): Enable indentation guides. Defaults to False.
            max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to None.
            max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
            max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
            expand_all (bool, optional): Expand all containers. Defaults to False.
            max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.
        
    """
    ...

def Pretty():
    """Pretty"""
    ...

def _get_braces_for_defaultdict(_object):
    ...

def _get_braces_for_deque(_object):
    ...

def _get_braces_for_array(_object):
    ...

def is_expandable(obj):
    """Check if an object may be expanded by pretty print."""
    ...

def Node():
    """Node"""
    ...

def _Line():
    """_Line"""
    ...

def _is_namedtuple(obj):
    """
    Checks if an object is most likely a namedtuple. It is possible
        to craft an object that passes this check and isn't a namedtuple, but
        there is only a minuscule chance of this happening unintentionally.
    
        Args:
            obj (Any): The object to test
    
        Returns:
            bool: True if the object is a namedtuple. False otherwise.
        
    """
    ...

def traverse(_object, max_length, max_string, max_depth):
    """
    Traverse object and generate a tree.
    
        Args:
            _object (Any): Object to be traversed.
            max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to None.
            max_string (int, optional): Maximum length of string before truncating, or None to disable truncating.
                Defaults to None.
            max_depth (int, optional): Maximum depth of data structures, or None for no maximum.
                Defaults to None.
    
        Returns:
            Node: The root of a tree structure which can be used to render a pretty repr.
        
    """
    ...

def pretty_repr(_object, *, max_width=None, indent_size=None, max_length=None, max_string=None, max_depth=None, expand_all=None):
    """
    Prettify repr string by expanding on to new lines to fit within a given width.
    
        Args:
            _object (Any): Object to repr.
            max_width (int, optional): Desired maximum width of repr string. Defaults to 80.
            indent_size (int, optional): Number of spaces to indent. Defaults to 4.
            max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to None.
            max_string (int, optional): Maximum length of string before truncating, or None to disable truncating.
                Defaults to None.
            max_depth (int, optional): Maximum depth of nested data structure, or None for no depth.
                Defaults to None.
            expand_all (bool, optional): Expand all containers regardless of available width. Defaults to False.
    
        Returns:
            str: A possibly multi-line representation of the object.
        
    """
    ...

def pprint(_object, *, console=None, indent_guides=None, max_length=None, max_string=None, max_depth=None, expand_all=None):
    """
    A convenience function for pretty printing.
    
        Args:
            _object (Any): Object to pretty print.
            console (Console, optional): Console instance, or None to use default. Defaults to None.
            max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to None.
            max_string (int, optional): Maximum length of strings before truncating, or None to disable. Defaults to None.
            max_depth (int, optional): Maximum depth for nested data structures, or None for unlimited depth. Defaults to None.
            indent_guides (bool, optional): Enable indentation guides. Defaults to True.
            expand_all (bool, optional): Expand all containers. Defaults to False.
        
    """
    ...

def BrokenRepr():
    """BrokenRepr"""
    ...

def StockKeepingUnit():
    """StockKeepingUnit"""
    ...

def Thing():
    """Thing"""
    ...
