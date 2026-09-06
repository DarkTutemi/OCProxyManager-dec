"""Module: core.licensing

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

from datetime import datetime
from email.utils import parsedate_to_datetime
import sys
import threading
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from save_activation import key


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'Decrypts XOR obfuscated base64 strings.',
    90,
    '_o.<locals>.<genexpr>',
    '-',
    'Generates a unique hardware ID (same logic as OCReview).',
    'Derives a stable 32-byte AES key from the HWID.',
    300,
    'https://www.google.com',
    'https://www.cloudflare.com',
    'https://1.1.1.1',
    'Lấy giờ thực chuẩn quốc tế qua HTTP Date header (cache offset để tránh request mạng liên tục).',
    5.0,
    'utf-8',
    120,
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d',
    30.0,
    'Decrypts and verifies local activation file with Anti-Time-Rollback Protection and Thread-safe Caching.',
    'Decrypts and returns the full activation dict or None on failure.',
    '[LICENSE ERROR] Save failed: ',
    'Encrypts and saves activation data locally.',
    15,
    200,
    'Server returned status ',
    'Lỗi kết nối máy chủ kích hoạt: ',
    'Triple Guard Protocol for PHP LicManager via cryptography package.',
    'không tồn tại',
    'hết hạn',
    'Kiểm tra bản quyền trực tuyến với server (Triple Guard).\n        Nếu key còn hạn -> tự động cập nhật lại hạn vào license.dat.\n        Nếu key hết hạn hoặc bị thu hồi trên server -> xóa license_file và trả về False.',
    '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuTseytj2wyss4tuDPiID\nO6zat04CPDzNcoKLkAROtn/bEB3ZbXMyt+DVg5/T4tsR2Oowx/TJrHniRT5MQAzd\nSLflgkfC+3ZnekPaCcniMvVbNw+30n7RCzUADT5s4lg1mej4JUlAuDKFW9RxvuaX\nXPvaI7ySwjaljeOAnQWk5h4oOl7Du6i6K7Pl8SAyE5N8/mTaMmD/h3hQ2fNdP9Rb\nZ0Ji/TWc8kok4otfPmRrS5AcC/aKyeSVRKbsYqJS0CPQIL3caO4/e79APerjqyuQ\n9UTBR5sPN57Xv61KUJ/YpwyKfhsqlvzhgI7wjiUWdSxseOqV9QVHMXxWK8yp2pi3\nQQIDAQAB\n-----END PUBLIC KEY-----',
)

_recovered_data_0 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', 'Accept': 'application/json'}

_recovered_data_1 = {0: 'Normal', 1: 'Premium', 2: 'Special'}


class LicenseManager:

    def __init__():
        # co_varnames (args+locals, order/split approximate): parsedate_to_datetime
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_hwid():
        # co_varnames (args+locals, order/split approximate): status
        pass  # native-compiled body — faithful op trace in the .nbc

    def _get_cipher_key():
        # co_varnames (args+locals, order/split approximate): lic_exp
        pass  # native-compiled body — faithful op trace in the .nbc

    def _get_reliable_network_time():
        # co_varnames (args+locals, order/split approximate): Cipher, algorithms, modes
        pass  # native-compiled body — faithful op trace in the .nbc

    def is_activated():
        # co_varnames (args+locals, order/split approximate): padding
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_activation_data():
        # co_varnames (args+locals, order/split approximate): ProxyPIA
        pass  # native-compiled body — faithful op trace in the .nbc

    def save_activation():
        # co_varnames (args+locals, order/split approximate): b
        pass  # native-compiled body — faithful op trace in the .nbc

    def fetch_from_server():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def verify_with_server(self):
        # co_varnames (args+locals, order/split approximate): app_name, base_dir, legacy_paths, leg, shutil
        pass  # native-compiled body — faithful op trace in the .nbc

