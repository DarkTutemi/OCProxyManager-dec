# Module: cgitb
# Pseudo-source reconstructed from bytecode (no decompiler)


def reset():
    """Return a string that resets the CGI and browser to a known state."""
    ...

def small(text):
    ...

def strong(text):
    ...

def grey(text):
    ...

def lookup(name, frame, locals):
    """Find the value for a given name in the given environment."""
    ...

def scanvars(reader, frame, locals):
    """Scan one logical line of Python and look up values of variables used."""
    ...

def html(einfo, context):
    """Return a nice HTML document describing a given traceback."""
    ...

def text(einfo, context):
    """Return a plain text document describing a given traceback."""
    ...

def Hook():
    """Hook"""
    ...

def enable(display, logdir, context, format):
    """
    Install an exception handler that formats tracebacks as HTML.
    
        The optional argument 'display' can be set to 0 to suppress sending the
        traceback to the browser, and 'logdir' can be set to a directory to cause
        tracebacks to be written to files there.
    """
    ...
