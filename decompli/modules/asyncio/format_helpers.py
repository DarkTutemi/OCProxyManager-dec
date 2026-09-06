# Module: format_helpers
# Pseudo-source reconstructed from bytecode (no decompiler)


def _get_function_source(func):
    ...

def _format_callback_source(func, args):
    ...

def _format_args_and_kwargs(args, kwargs):
    """
    Format function arguments and keyword arguments.
    
        Special case for a single parameter: ('hello',) is formatted as ('hello').
        
    """
    ...

def _format_callback(func, args, kwargs, suffix):
    ...

def extract_stack(f, limit):
    """
    Replacement for traceback.extract_stack() that only does the
        necessary work for asyncio debug mode.
        
    """
    ...
