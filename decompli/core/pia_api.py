"""Module: core.pia_api

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import logging
import random
import token
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519
from region_name import name
from server_public_key import server_key


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    '\n        Sinh cặp khóa Wireguard (private_key, public_key)\n        Sử dụng cryptography library (x25519 curve)\n        ',
    ':',
    8,
    401,
    'Sai Tên đăng nhập hoặc Mật khẩu PIA (',
    ')!',
    402,
    'Tài khoản PIA (',
    ') đã HẾT HẠN GÓI CƯỚC (Payment Required - 402)!',
    'Đã lấy token PIA qua API gốc cho user ',
    82800,
    'API gốc lấy token thất bại (',
    '), thử Meta Service...',
    3,
    'https://',
    ':443/authv3/generateToken',
    5,
    200,
    'Đã lấy token PIA qua Meta Service (',
    ') cho user ',
    'Lỗi khi lấy token PIA: ',
    '\n        Lấy token xác thực từ PIA API (Có cache 23h trong bộ nhớ)\n        ',
    'Đã lấy ',
    ' server ',
    ' cho quốc gia ',
    'Lỗi khi lấy server list: ',
    '\n        Lấy danh sách server từ PIA\n        \n        Args:\n            country: Mã quốc gia (ví dụ: "US", "DE", "UK"). Nếu None thì lấy tất cả.\n            protocol: Loại protocol ("wireguard" hoặc "openvpn")\n            \n        Returns:\n            Danh sách server có hỗ trợ protocol được chọn\n        ',
    ':1337/addKey',
    6.0,
    'Đã đăng ký key với server ',
    ', peer IP: ',
    409,
    'Conflict khi đăng ký key với server ',
    ', sinh key mới và retry (attempt ',
    ')',
    'Lỗi HTTP khi đăng ký key: ',
    'Timeout khi đăng ký key với ',
    ' (port 1337): ',
    'Không thể kết nối port 1337 server ',
    ': ',
    'Lỗi khi đăng ký Wireguard key với server ',
    'Không thể đăng ký key với server ',
    ' sau ',
    ' lần thử',
    '\n        Đăng ký public key với server PIA qua port 1337\n        Có retry nếu gặp lỗi 409 Conflict (key đã tồn tại)\n        \n        Args:\n            server_ip: IP của server PIA\n            token: Token xác thực\n            private_key: Private key Wireguard (sẽ thay đổi nếu retry)\n            public_key: Public key tương ứng\n            max_retries: Số lần retry tối đa khi gặp Conflict\n            \n        Returns:\n            Dict chứa server_public_key, server_port, peer_ip,\n            private_key (final), public_key (final)\n            \n        Raises:\n            Exception: Nếu đăng ký thất bại sau tất cả retries\n        ',
    'Đã lấy OpenVPN credentials cho user ',
    'Lỗi khi lấy OpenVPN credentials: ',
    '\n        Lấy thông tin OpenVPN credentials từ PIA\n        PIA không cần đăng ký riêng cho OpenVPN, dùng trực tiếp username/password\n        \n        Args:\n            username: Tên đăng nhập PIA\n            password: Mật khẩu PIA\n            \n        Returns:\n            Dict chứa username và password cho OpenVPN\n        ',
    'được chọn',
    '⚠️ Quốc gia ',
    ' chỉ có ',
    ' server WireGuard khả dụng. Hệ thống đã tự động bổ sung ',
    ' server từ các khu vực khác để đảm bảo 100% Unique IP không bị tranh chấp!',
    'PIAAPI.get_random_servers.<locals>.sort_key',
    '\n        Lấy ngẫu nhiên N server từ danh sách, ưu tiên server ít dùng nhất và đảm bảo Unique IP cho WireGuard\n        ',
    'https://www.privateinternetaccess.com/api/client/v2/token',
    'https://serverlist.piaservers.net/vpninfo/servers/v4',
    'Giao tiếp với API của Private Internet Access',
)

_recovered_data_0 = {'User-Agent': 'PIA-Proxy-Manager-v2'}


class PIAAPI:

    def generate_wireguard_keys():
        # co_varnames (args+locals, order/split approximate): encoding, format, encryption_algorithm
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_pia_token():
        # co_varnames (args+locals, order/split approximate): data, headers, timeout
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_server_list():
        # co_varnames (args+locals, order/split approximate): verify, timeout
        pass  # native-compiled body — faithful op trace in the .nbc

    def register_wireguard_key():
        # co_varnames (args+locals, order/split approximate): country
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_openvpn_credentials():
        # co_varnames (args+locals, order/split approximate): serialization
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_random_servers():
        # co_varnames (args+locals, order/split approximate): default_backend
        pass  # native-compiled body — faithful op trace in the .nbc

