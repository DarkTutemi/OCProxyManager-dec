# Module: install
# Pseudo-source reconstructed from bytecode (no decompiler)


def _load_sysconfig_schemes():
    ...

def _load_schemes():
    """
    
        Extend default schemes with schemes from sysconfig.
        
    """
    ...

def _get_implementation():
    ...

def _select_scheme(ob, name):
    ...

def _remove_set(ob, attrs):
    """
    
        Include only attrs that are None in ob.
        
    """
    ...

def _resolve_scheme(name):
    ...

def _load_scheme(name):
    ...

def _inject_headers(name, scheme):
    """
    
        Given a scheme name and the resolved scheme,
        if the scheme does not include headers, resolve
        the fallback scheme for the name and use headers
        from it. pypa/distutils#88
        
    """
    ...

def _scheme_attrs(scheme):
    """Resolve install directories by applying the install schemes."""
    ...

def _pypy_hack(name):
    ...

def install():
    """install"""
    ...
