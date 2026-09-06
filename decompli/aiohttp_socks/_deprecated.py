"""Module: aiohttp_socks._deprecated

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import warnings
from connector import ProxyConnector
from python_socks import ProxyError, ProxyConnectionError, ProxyType


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'SocksConnector is deprecated. Use ProxyConnector instead.',
)


class SocksConnector:

    def __init__():
        # co_varnames (args+locals, order/split approximate): stacklevel
        pass  # native-compiled body — faithful op trace in the .nbc

    def from_url():
        # co_varnames (args+locals, order/split approximate): object
        pass  # native-compiled body — faithful op trace in the .nbc

