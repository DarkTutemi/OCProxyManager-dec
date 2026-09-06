# Module: protocol
# Pseudo-source reconstructed from bytecode (no decompiler)


def is_renderable(check_object):
    """Check if an object may be rendered by Rich."""
    ...

def rich_cast(renderable):
    """
    Cast an object to a renderable by calling __rich__ if present.
    
        Args:
            renderable (object): A potentially renderable object
    
        Returns:
            object: The result of recursively calling __rich__.
        
    """
    ...
