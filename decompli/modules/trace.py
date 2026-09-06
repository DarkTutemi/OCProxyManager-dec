# Module: trace
# Pseudo-source reconstructed from bytecode (no decompiler)


def _Ignore():
    """_Ignore"""
    ...

def _modname(path):
    """Return a plausible module name for the path."""
    ...

def _fullmodname(path):
    """Return a plausible module name for the path."""
    ...

def CoverageResults():
    """CoverageResults"""
    ...

def _find_lines_from_code(code, strs):
    """Return dict where keys are lines in the line number table."""
    ...

def _find_lines(code, strs):
    """Return lineno dict for all code objects reachable from code."""
    ...

def _find_strings(filename, encoding):
    """
    Return a dict of possible docstring positions.
    
        The dict maps line numbers to strings.  There is an entry for
        line that contains only a string or a part of a triple-quoted
        string.
        
    """
    ...

def _find_executable_linenos(filename):
    """Return dict where keys are line numbers in the line number table."""
    ...

def Trace():
    """Trace"""
    ...

def main():
    ...
