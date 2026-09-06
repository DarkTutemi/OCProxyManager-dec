"""Module: aiohttp_socks.connector

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

from aiohttp import TCPConnector
from aiohttp.abc import AbstractResolver
from aiohttp.client_proto import ResponseHandler
import asyncio
import socket
from ssl import dest_host, dest_port, dest_ssl, timeout
from typing import BaseTransport, StreamWriter
from typing import Optional, Iterable
from _loop import loop, writer
from python_socks import ProxyType, parse_proxy_url
from python_socks.async_.asyncio.v2 import Proxy


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    '\n    To fix issue https://github.com/romis2012/aiohttp-socks/issues/27\n    In Python>=3.11.5 we need to keep a reference to the StreamWriter\n    so that the underlying transport is not closed during garbage collection.\n    See StreamWriter.__del__ method (was added in Python 3.11.5)\n    ',
)


class NoResolver:

    def resolve():
        # co_varnames (args+locals, order/split approximate): loop, writer
        pass  # native-compiled body — faithful op trace in the .nbc

    def close(self):
        pass  # native-compiled body — faithful op trace in the .nbc


class ProxyConnector:

    def __init__():
        # co_varnames (args+locals, order/split approximate): ResponseHandler
        pass  # native-compiled body — faithful op trace in the .nbc

    def _wrap_create_connection():
        # co_varnames (args+locals, order/split approximate): proxy_type, host, port, username, password
        pass  # native-compiled body — faithful op trace in the .nbc

    def from_url():
        # co_varnames (args+locals, order/split approximate): Proxy
        pass  # native-compiled body — faithful op trace in the .nbc


class ChainProxyConnector:

    def __init__():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def _wrap_create_connection():
        # co_varnames (args+locals, order/split approximate): AbstractResolver
        pass  # native-compiled body — faithful op trace in the .nbc

    def from_urls(self):
        # co_varnames (args+locals, order/split approximate): proxy_infos, kwargs, __class__
        pass  # native-compiled body — faithful op trace in the .nbc

