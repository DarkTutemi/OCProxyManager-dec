"""Module: core.ipv6.ipv6_manager

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import concurrent.futures
import ctypes
from pathlib import Path
import sys
from detect_interface_and_prefix import force_iface


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    '📦 [Auto-Migration] Đã chuyển ',
    ' vào data/',
    '^Interface\\s+(\\d+):\\s+(.+)$',
    '/64',
    'IPv6Manager.get_available_interfaces.<locals>.<lambda>',
    'Không có IPv6 Public',
    'Quét và trả về danh sách tất cả card mạng khả dụng trên hệ thống cùng dải IPv6 phát hiện được',
    'utf-8',
    'Sử dụng custom prefix IPv6 từ file: ',
    ' trên card ',
    'Lỗi đọc custom prefix: ',
    'IPv6Manager.detect_interface_and_prefix.<locals>.<lambda>',
    3,
    4,
    "Đã phát hiện Card mạng '",
    "' với prefix IPv6 ",
    ' (nguồn: ',
    ')',
    'Lỗi lưu custom interface: ',
    'Lưu card mạng được chọn vào cấu hình cố định',
    4294967295,
    'Lỗi flush manual IPv6: ',
    'Dọn dẹp sạch sẽ toàn bộ các IP gán Manual rác cũ trên card mạng.',
    'Chưa phát hiện dải IPv6',
    'Win32 add IPv6 fail, fallback netsh: ',
    'Gán IPv6 ',
    ' thất bại: ',
    '⚡ [Win32 Native] Đã gán siêu tốc ',
    ' địa chỉ IPv6 vào card mạng!',
    'Win32 API gán IPv6 lỗi: ',
    ', fallback sang netsh pool...',
    'IPv6Manager.add_addresses_batch.<locals>._add_single_netsh',
    '⚡ [netsh Pool] Đã gán ',
    'Gán đồng loạt hàng loạt địa chỉ IPv6 vào card mạng qua Win32 Native API siêu tốc (<0.5ms/IP)',
    '⚡ [Win32 Native] Đã dọn dẹp ',
    ' địa chỉ IPv6 trên card mạng',
    'Win32 API xóa IPv6 lỗi: ',
    'IPv6Manager.remove_addresses_batch.<locals>._del_single_netsh',
    '⚡ [netsh Pool] Đã dọn dẹp ',
    'Xóa đồng loạt hàng loạt địa chỉ IPv6 trên card mạng qua Win32 Native API siêu tốc',
    'Lỗi lưu custom prefix: ',
    134217728,
    23,
    16,
    'Không thể khởi tạo Win32 IP Helper API: ',
)


class IPv6Manager:

    def __init__():
        # co_varnames (args+locals, order/split approximate): capture_output, text, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_available_interfaces():
        # co_varnames (args+locals, order/split approximate): strict
        pass  # native-compiled body — faithful op trace in the .nbc

    def detect_interface_and_prefix():
        # co_varnames (args+locals, order/split approximate): public, temporary, dhcp, other
        pass  # native-compiled body — faithful op trace in the .nbc

    def save_custom_interface():
        # co_varnames (args+locals, order/split approximate): key
        pass  # native-compiled body — faithful op trace in the .nbc

    def _get_interface_luid():
        # co_varnames (args+locals, order/split approximate): c
        pass  # native-compiled body — faithful op trace in the .nbc

    def _win32_add_ipv6():
        # co_varnames (args+locals, order/split approximate): x
        pass  # native-compiled body — faithful op trace in the .nbc

    def _win32_del_ipv6():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def flush_all_manual_addresses(self):
        # co_varnames (args+locals, order/split approximate): data_dir, Path, base_dir, legacy_configs_dir, fname, legacy_file, target_file, shutil
        pass  # native-compiled body — faithful op trace in the .nbc

    def generate_addresses():
        # co_varnames (args+locals, order/split approximate): addr, res
        pass  # native-compiled body — faithful op trace in the .nbc

    def add_address(self):
        pass  # native-compiled body — faithful op trace in the .nbc

    def add_addresses_batch():
        # co_varnames (args+locals, order/split approximate): addr
        pass  # native-compiled body — faithful op trace in the .nbc

    def remove_address(self):
        # co_varnames (args+locals, order/split approximate): result, output, line, m
        pass  # native-compiled body — faithful op trace in the .nbc

    def remove_addresses_batch(self):
        # co_varnames (args+locals, order/split approximate): luid, res, line, parts, idx
        pass  # native-compiled body — faithful op trace in the .nbc

    def cleanup_all(self):
        # co_varnames (args+locals, order/split approximate): addr_str, luid, prefix_len, row, ip_obj, i, b, res
        pass  # native-compiled body — faithful op trace in the .nbc

    def _find_active_interface_name(self):
        # co_varnames (args+locals, order/split approximate): addr_str, luid, row, ip_obj, i, b, res
        pass  # native-compiled body — faithful op trace in the .nbc

    def save_custom_prefix(self):
        # co_varnames (args+locals, order/split approximate): address, luid, e, result
        pass  # native-compiled body — faithful op trace in the .nbc

