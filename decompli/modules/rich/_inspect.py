# Module: _inspect
# Pseudo-source reconstructed from bytecode (no decompiler)


def _first_paragraph(doc):
    """Get the first paragraph from a docstring."""
    ...

def Inspect():
    """Inspect"""
    ...

def get_object_types_mro(obj):
    """Returns the MRO of an object's class, or of the object itself if it's a class."""
    ...

def get_object_types_mro_as_strings(obj):
    """
    
        Returns the MRO of an object's class as full qualified names, or of the object itself if it's a class.
    
        Examples:
            `object_types_mro_as_strings(JSONDecoder)` will return `['json.decoder.JSONDecoder', 'builtins.object']`
        
    """
    ...

def is_object_one_of_types(obj, fully_qualified_types_names):
    """
    
        Returns `True` if the given object's class (or the object itself, if it's a class) has one of the
        fully qualified names in its MRO.
        
    """
    ...
