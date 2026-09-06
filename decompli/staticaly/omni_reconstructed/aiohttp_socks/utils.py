"""Module: aiohttp_socks.utils

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import asyncio
import warnings
from python_socks import ProxyType, parse_proxy_url
from python_socks.async_.asyncio import Proxy


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'open_connection is deprecated. Use https://github.com/romis2012/python-socks directly instead.',
    'host and port must be specified',
    'create_connection is deprecated. Use https://github.com/romis2012/python-socks directly instead.',
    'protocol_factory must be specified',
    '127.0.0.1',
    1080,
)

# const: 'warnings'
# const: 'open_connection is deprecated. Use https://github.com/romis2012/python-socks directly instead.'
# const: 'DeprecationWarning'
# const: 'host and port must be specified'
# const: 'asyncio'
# const: 'get_event_loop'
# const: 'proxy_url'
# const: 'parse_proxy_url'
# const: 'Proxy'
# const: 'create'
# const: 'proxy_type'
# const: 'proxy_host'
# const: 'proxy_port'
# const: 'username'
# const: 'password'
# const: 'connect'
# const: 'open_connection'
# const: 'kwargs'
# const: 'create_connection is deprecated. Use https://github.com/romis2012/python-socks directly instead.'
# const: 'protocol_factory'
# const: 'protocol_factory must be specified'
# const: 'create_connection'
# const: 'origin'
# const: 'has_location'
# const: 'python_socks'
# const: 'ProxyType'
# const: 'python_socks.async_.asyncio'
# const: 'SOCKS5'
# const: '127.0.0.1'
# const: 'aiohttp_socks\\utils.py'
# const: '<module aiohttp_socks.utils>'
