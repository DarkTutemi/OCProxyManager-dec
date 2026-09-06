# Module: warnings
# Pseudo-source reconstructed from bytecode (no decompiler)


def showwarning(message, category, filename, lineno, file, line):
    """Hook to write a warning to a file; replace if you like."""
    ...

def formatwarning(message, category, filename, lineno, line):
    """Function to format a warning the standard way."""
    ...

def _showwarnmsg_impl(msg):
    ...

def _formatwarnmsg_impl(msg):
    ...

def _showwarnmsg(msg):
    """Hook to write a warning to a file; replace if you like."""
    ...

def _formatwarnmsg(msg):
    """Function to format a warning the standard way."""
    ...

def filterwarnings(action, message, category, module, lineno, append):
    """
    Insert an entry into the list of warnings filters (at the front).
    
        'action' -- one of "error", "ignore", "always", "default", "module",
                    or "once"
        'message' -- a regex that the warning message must match
        'category' -- a class that the warning must be a subclass of
        'module' -- a regex that the module name must match
        'lineno' -- an integer line number, 0 matches all warnings
        'append' -- if true, append to the list of filters
        
    """
    ...

def simplefilter(action, category, lineno, append):
    """
    Insert a simple entry into the list of warnings filters (at the front).
    
        A simple filter matches all modules and messages.
        'action' -- one of "error", "ignore", "always", "default", "module",
                    or "once"
        'category' -- a class that the warning must be a subclass of
        'lineno' -- an integer line number, 0 matches all warnings
        'append' -- if true, append to the list of filters
        
    """
    ...

def _add_filter(*item, append=None):
    ...

def resetwarnings():
    """Clear the list of warning filters, so that no filters are active."""
    ...

def _OptionError():
    """_OptionError"""
    ...

def _processoptions(args):
    ...

def _setoption(arg):
    ...

def _getaction(action):
    ...

def _getcategory(category):
    ...

def _is_internal_frame(frame):
    """Signal whether the frame is an internal CPython implementation detail."""
    ...

def _next_external_frame(frame):
    """Find the next frame that doesn't involve CPython internals."""
    ...

def warn(message, category, stacklevel, source):
    """Issue a warning, or maybe ignore it or raise an exception."""
    ...

def warn_explicit(message, category, filename, lineno, module, registry, module_globals, source):
    ...

def WarningMessage():
    """WarningMessage"""
    ...

def catch_warnings():
    """catch_warnings"""
    ...

def _deprecated(name, message, *, remove=None, _version=None):
    """
    Warn that *name* is deprecated or should be removed.
    
        RuntimeError is raised if *remove* specifies a major/minor tuple older than
        the current Python version or the same version but past the alpha.
    
        The *message* argument is formatted with *name* and *remove* as a Python
        version (e.g. "3.11").
    
        
    """
    ...

def _warn_unawaited_coroutine(coro):
    ...

def _filters_mutated():
    ...
