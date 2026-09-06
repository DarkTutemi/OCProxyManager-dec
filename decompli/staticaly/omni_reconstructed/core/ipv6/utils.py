"""Module: core.ipv6.utils

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import sys


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    65536,
    'Không còn port khả dụng',
    'Không đủ cổng khả dụng trong dải port',
    'Cấp phát hàng loạt N cổng liên tục siêu tốc (chỉ mất ~0.001s cho 1000 ports)',
    '0.0.0.0',
    '127.0.0.1',
)


class PortManager:

    def __init__(self):
        # co_varnames (args+locals, order/split approximate): start_port
        pass  # native-compiled body — faithful op trace in the .nbc

    def allocate(self):
        # co_varnames (args+locals, order/split approximate): port, s
        pass  # native-compiled body — faithful op trace in the .nbc

    def allocate_batch(self):
        # co_varnames (args+locals, order/split approximate): preferred_port, port
        pass  # native-compiled body — faithful op trace in the .nbc

    def release(self):
        # co_varnames (args+locals, order/split approximate): count, preferred_start, allocated, curr
        pass  # native-compiled body — faithful op trace in the .nbc

    def _is_port_free():
        # co_varnames (args+locals, order/split approximate): s, ip
        pass  # native-compiled body — faithful op trace in the .nbc

    def is_used(self):
        # co_varnames (args+locals, order/split approximate): port
        pass  # native-compiled body — faithful op trace in the .nbc

