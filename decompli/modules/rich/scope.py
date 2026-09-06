# Module: scope
# Pseudo-source reconstructed from bytecode (no decompiler)


def render_scope(scope, *, title=None, sort_keys=None, indent_guides=None, max_length=None, max_string=None, max_depth=None, overflow=None):
    """
    Render python variables in a given scope.
    
        Args:
            scope (Mapping): A mapping containing variable names and values.
            title (str, optional): Optional title. Defaults to None.
            sort_keys (bool, optional): Enable sorting of items. Defaults to True.
            indent_guides (bool, optional): Enable indentation guides. Defaults to False.
            max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to None.
            max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
            max_depth (int, optional): Maximum depths of locals before truncating, or None to disable. Defaults to None.
            overflow (OverflowMethod, optional): How to handle overflowing locals, or None to disable. Defaults to None.
    
        Returns:
            ConsoleRenderable: A renderable object.
        
    """
    ...

def test(foo, bar):
    ...
