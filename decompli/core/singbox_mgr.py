"""Module: core.singbox_mgr

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import json
import logging
import os
from pathlib import Path
import signal
import subprocess
import time
from com_at import com_port
from local_port import proxy_type, socks
from net_connections import inet
from rasdial import rasdial_profile
from core.licensing import LicenseManager


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'Config directory: ',
    'Resource directory: ',
    '-',
    'wg-',
    '0.0.0.0',
    'ovpn-out-',
    'ocproxy-tun-',
    '/32',
    '0.0.0.0/0',
    25,
    1420,
    '.json',
    'utf-8',
    'Đã sinh config cho port ',
    ': ',
    '[SECURITY] Khởi động proxy port ',
    ' bị từ chối. Bản quyền không hợp lệ.',
    'Lỗi bản quyền: Vui lòng kích hoạt phần mềm.',
    '-c',
    'Start proxy port ',
    ' ',
    'Unknown error',
    'Proxy port ',
    ' terminated: ',
    'Sing-box port ',
    ' died: ',
    ' started, PID ',
    'Start sing-box proxy. wait_ms: giây chờ process ổn định (giảm khi chạy batch).',
    'Đã kill process PID ',
    ' giữ port ',
    '/F',
    '/PID',
    'port ',
    'PID ',
    'taskkill PID ',
    ' (',
    ') thất bại',
    'Đã dừng proxy ',
    'Proxy ',
    ': process không tồn tại',
    'Timeout dừng proxy ',
    'Lỗi dừng proxy ',
    'Đã batch-kill ',
    ' proxy processes',
    'Batch taskkill lỗi: ',
    ', fallback từng cái',
    '\n        Dừng nhiều proxy cùng lúc bằng 1 lệnh taskkill duy nhất (Windows)\n        thay vì gọi subprocess lặp lại N lần.\n        ',
    'sing-box.exe',
    'Không tìm thấy sing-box.exe. Vui lòng tải từ https://github.com/SagerNet/sing-box/releases và đặt vào thư mục v2/',
    '10.0.0.2/32',
    'Đã xóa config port ',
    'Lỗi xóa config port ',
    3,
    'http-in',
    'socks-out',
    'Đã sinh config bridge cho port ',
    '[SECURITY] Khởi động bridge port ',
    'Start bridge port ',
    'Bridge port ',
    'Sing-box bridge port ',
    'Start sing-box bridge. wait_ms=0 mặc định để batch launch không bị chặn.',
    'Đã xóa config bridge port ',
    'Lỗi xóa config bridge port ',
    'dcom-',
    'direct-out',
    'Đã sinh config Dcom proxy cho port ',
    '[SECURITY] Khởi động Dcom proxy port ',
    'Start Dcom proxy port ',
    'Dcom proxy port ',
    'Sing-box Dcom proxy port ',
    'Đã xóa config Dcom proxy port ',
    'Lỗi xóa config Dcom proxy port ',
    'Quản lý Sing-box core - mỗi proxy = 1 process riêng',
)

_recovered_data_0 = {'log': {'level': 'warn'}, 'dns': {'servers': [{'tag': 'dns-server', 'type': 'local'}], 'final': 'dns-server', 'strategy': 'prefer_ipv4'}, 'inbounds': [], 'endpoints': [], 'outbounds': [], 'route': {'rules': []}}

_recovered_data_1 = {'surfshark': '10.14.0.2/32', 'nordvpn': '10.5.0.2/32', 'protonvpn': '10.2.0.2/32'}

_recovered_data_2 = {'rules': [{'inbound': ['http-in'], 'outbound': 'socks-out'}]}

_recovered_data_3 = {'type': 'direct', 'tag': 'direct-out'}


class SingBoxManager:

    def __init__():
        # co_varnames (args+locals, order/split approximate): auth_user
        pass  # native-compiled body — faithful op trace in the .nbc

    def _generate_proxy_config():
        # co_varnames (args+locals, order/split approximate): username
        pass  # native-compiled body — faithful op trace in the .nbc

    def start_proxy():
        # co_varnames (args+locals, order/split approximate): auth_pass
        pass  # native-compiled body — faithful op trace in the .nbc

    def stop_proxy():
        # co_varnames (args+locals, order/split approximate): password
        pass  # native-compiled body — faithful op trace in the .nbc

    def _ensure_port_killed():
        # co_varnames (args+locals, order/split approximate): LicenseManager
        pass  # native-compiled body — faithful op trace in the .nbc

    def _ensure_proxy_stopped():
        # co_varnames (args+locals, order/split approximate): OCProxy
        pass  # native-compiled body — faithful op trace in the .nbc

    def _kill_process():
        # co_varnames (args+locals, order/split approximate): app_name
        pass  # native-compiled body — faithful op trace in the .nbc

    def stop_many_proxies():
        # co_varnames (args+locals, order/split approximate): stdout, stderr, env, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

    def stop_all_proxies():
        # co_varnames (args+locals, order/split approximate): capture_output, timeout, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

    def restart_proxy():
        # co_varnames (args+locals, order/split approximate): proxy_type, http
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_pid():
        # co_varnames (args+locals, order/split approximate): interface_name
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_all_pids():
        # co_varnames (args+locals, order/split approximate): rotate_mode
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_proxy_count():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def is_proxy_alive(self):
        # co_varnames (args+locals, order/split approximate): config_dir, resource_dir
        pass  # native-compiled body — faithful op trace in the .nbc

    def _find_singbox(self):
        # co_varnames (args+locals, order/split approximate): port, psutil, killed, conn, proc
        pass  # native-compiled body — faithful op trace in the .nbc

    def _get_default_local_ip(self):
        # co_varnames (args+locals, order/split approximate): port, pid
        pass  # native-compiled body — faithful op trace in the .nbc

    def _is_pid_alive(self):
        # co_varnames (args+locals, order/split approximate): paths, p
        pass  # native-compiled body — faithful op trace in the .nbc

    def delete_config(self):
        # co_varnames (args+locals, order/split approximate): bridge, port, upstream, parts, socks_ip, socks_port, socks_user, socks_pass, auth_user, auth_pass, users, config, config_path, f
        pass  # native-compiled body — faithful op trace in the .nbc

    def _generate_bridge_config(self):
        # co_varnames (args+locals, order/split approximate): dcom, port, ptype, inbound_tag, auth_user, auth_pass, users, outbound, interface_name, dcom_mgr, config, config_path, f
        pass  # native-compiled body — faithful op trace in the .nbc

    def start_bridge(self):
        # co_varnames (args+locals, order/split approximate): proxy, port, ptype, inbound_tag, wg_tag, peer_ip, config, user, password, users, inbound_type, outbound_tag, tun_interface_name, outbound_entry, config_path, f
        pass  # native-compiled body — faithful op trace in the .nbc

    def delete_bridge_config():
        # co_varnames (args+locals, order/split approximate): proxy, provider, defaults
        pass  # native-compiled body — faithful op trace in the .nbc

    def _generate_dcom_config():
        # co_varnames (args+locals, order/split approximate): pid, psutil
        pass  # native-compiled body — faithful op trace in the .nbc

    def start_dcom_proxy(self):
        # co_varnames (args+locals, order/split approximate): pid, port, label, result, success, e
        pass  # native-compiled body — faithful op trace in the .nbc

    def delete_dcom_config(self):
        # co_varnames (args+locals, order/split approximate): port, config_path, e
        pass  # native-compiled body — faithful op trace in the .nbc

