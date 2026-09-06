# Module: timeit
# Pseudo-source reconstructed from bytecode (no decompiler)


def reindent(src, indent):
    """Helper to reindent a multi-line statement."""
    ...

def Timer():
    """Timer"""
    ...

def timeit(stmt, setup, timer, number, globals):
    """Convenience function to create Timer object and call timeit method."""
    ...

def repeat(stmt, setup, timer, repeat, number, globals):
    """Convenience function to create Timer object and call repeat method."""
    ...

def main(args, *, _wrap_timer=None):
    """
    Main program, used when run as a script.
    
        The optional 'args' argument specifies the command line to be parsed,
        defaulting to sys.argv[1:].
    
        The return value is an exit code to be passed to sys.exit(); it
        may be None to indicate success.
    
        When an exception happens during timing, a traceback is printed to
        stderr and the return value is 1.  Exceptions at other times
        (including the template compilation) are not caught.
    
        '_wrap_timer' is an internal interface used for unit testing.  If it
        is not None, it must be a callable that accepts a timer function
        and returns another timer function (used for unit testing).
        
    """
    ...
