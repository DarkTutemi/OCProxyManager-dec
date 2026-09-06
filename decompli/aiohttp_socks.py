"""Module: aiohttp_socks

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

from _deprecated import SocksVer, SocksConnector, SocksConnectionError, SocksError
from connector import ProxyConnector, ChainProxyConnector, ProxyInfo
from python_socks import ProxyError, ProxyTimeoutError, ProxyConnectionError, ProxyType
from utils import open_connection, create_connection


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'aiohttp-socks',
    '0.8.4',
)

# const: 'environ'
# const: 'origin'
# const: 'has_location'
# const: 'submodule_search_locations'
# const: 'aiohttp-socks'
# const: '__title__'
# const: '0.8.4'
# const: '__version__'
# const: 'python_socks'
# const: 'ProxyError'
# const: 'ProxyTimeoutError'
# const: 'ProxyConnectionError'
# const: 'ProxyType'
# const: 'connector'
# const: 'ProxyConnector'
# const: 'ChainProxyConnector'
# const: 'ProxyInfo'
# const: 'utils'
# const: 'open_connection'
# const: 'create_connection'
# const: '_deprecated'
# const: 'SocksVer'
# const: 'SocksConnector'
# const: 'SocksConnectionError'
# const: 'SocksError'
# const: 'aiohttp_socks\\__init__.py'
# const: '<module aiohttp_socks>'
