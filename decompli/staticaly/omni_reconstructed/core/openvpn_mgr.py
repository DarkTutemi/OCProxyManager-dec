"""Module: core.openvpn_mgr

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import concurrent.futures
import logging
from pathlib import Path
import sys
from _vm_stderr_file import cwd, stdout, stderr, creationflags
import alpine_root_2g.raw
import alpine_tiny.qcow2
import config.ovpn
from get_all_status import port
from qemu import name
import vpn_data.tar


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'Phân giải nhanh hostname sang IP số có cache tránh chậm mạng',
    255,
    '_fast_resolve_ip.<locals>.<genexpr>',
    'qemu-system-x86_64.exe',
    10485760,
    '📦 [MicroVM Engine] Đang tự động giải nén máy ảo lần đầu từ ',
    '...',
    '❌ [MicroVM Engine] Lỗi giải nén ',
    ': ',
    'Tự động giải nén qemu_engine từ file zip backup nếu thư mục binary chưa tồn tại hoặc thiếu DLL (1-Click Zero Config)',
    'Kiểm tra sự tồn tại của QEMU MicroVM binary',
    '-L',
    '-accel',
    'whpx,kernel-irqchip=off',
    '-nographic',
    '-nodefaults',
    '-serial',
    '-monitor',
    '-m',
    '64M',
    'Kiểm tra Windows Hypervisor Platform (WHPX) có khả dụng và chạy được không',
    '/api/health',
    200,
    'Kiểm tra Agent Controller bên trong MicroVM đã sẵn sàng chưa',
    10,
    'hostfwd=tcp::28888-:28888',
    'hostfwd=tcp::28889-:28889',
    'user,id=net0,',
    ',',
    1073741824,
    14,
    '1024M',
    '512M',
    '⚡ [MicroVM Engine] Cấu hình MicroVM: Accel=',
    ', vCPU=',
    ', RAM=',
    '-smp',
    '-drive',
    'file=',
    ',format=qcow2,if=virtio',
    ',format=raw,if=virtio',
    '-netdev',
    '-device',
    'virtio-net-pci,netdev=net0,romfile=',
    'utf-8',
    '[!] Không thể khởi động QEMU MicroVM: ',
    '[+] MicroVM Engine đã sẵn sàng sau ',
    's!',
    '[!] QEMU MicroVM process đã thoát bất thường (code ',
    '). Chi tiết: ',
    'N/A',
    '[!] Quá thời gian chờ MicroVM khởi động (',
    's)',
    '\n        Đảm bảo MicroVM Engine đã khởi động hoàn chỉnh trước khi gửi lệnh.\n        Có cơ chế polling thích ứng với mọi cấu hình máy tính (yếu / mạnh).\n        ',
    '\n',
    502,
    'dev tun',
    'proto ',
    'remote ',
    ' ',
    'redirect-gateway def1',
    'resolv-retry infinite',
    'persist-key',
    'persist-tun',
    'remote-cert-tls server',
    'verb 1',
    'mute 20',
    'fast-io',
    'reneg-sec 0',
    'data-ciphers AES-256-GCM:AES-128-GCM:AES-128-CBC:AES-256-CBC',
    'data-ciphers-fallback AES-128-CBC',
    '\n# --- Provider Certs ---',
    '\n# --- PIA Default Root CA & Security ---\ncipher aes-128-cbc\nauth sha1\ntls-client\nremote-cert-tls server\ncompress\nreneg-sec 0\n<ca>\n-----BEGIN CERTIFICATE-----\nMIIFqzCCBJOgAwIBAgIJAKZ7D5Yv87qDMA0GCSqGSIb3DQEBDQUAMIHoMQswCQYD\nVQQGEwJVUzELMAkGA1UECBMCQ0ExEzARBgNVBAcTCkxvc0FuZ2VsZXMxIDAeBgNV\nBAoTF1ByaXZhdGUgSW50ZXJuZXQgQWNjZXNzMSAwHgYDVQQLExdQcml2YXRlIElu\ndGVybmV0IEFjY2VzczEgMB4GA1UEAxMXUHJpdmF0ZSBJbnRlcm5ldCBBY2Nlc3Mx\nIDAeBgNVBCkTF1ByaXZhdGUgSW50ZXJuZXQgQWNjZXNzMS8wLQYJKoZIhvcNAQkB\nFiBzZWN1cmVAcHJpdmF0ZWludGVybmV0YWNjZXNzLmNvbTAeFw0xNDA0MTcxNzM1\nMThaFw0zNDA0MTIxNzM1MThaMIHoMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0Ex\nEzARBgNVBAcTCkxvc0FuZ2VsZXMxIDAeBgNVBAoTF1ByaXZhdGUgSW50ZXJuZXQg\nQWNjZXNzMSAwHgYDVQQLExdQcml2YXRlIEludGVybmV0IEFjY2VzczEgMB4GA1UE\nAxMXUHJpdmF0ZSBJbnRlcm5ldCBBY2Nlc3MxIDAeBgNVBCkTF1ByaXZhdGUgSW50\nZXJuZXQgQWNjZXNzMS8wLQYJKoZIhvcNAQkBFiBzZWN1cmVAcHJpdmF0ZWludGVy\nbmV0YWNjZXNzLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPXD\nL1L9tX6DGf36liA7UBTy5I869z0UVo3lImfOs/GSiFKPtInlesP65577nd7UNzzX\nlH/P/CnFPdBWlLp5ze3HRBCc/Avgr5CdMRkEsySL5GHBZsx6w2cayQ2EcRhVTwWp\ncdldeNO+pPr9rIgPrtXqT4SWViTQRBeGM8CDxAyTopTsobjSiYZCF9Ta1gunl0G/\n8Vfp+SXfYCC+ZzWvP+L1pFhPRqzQQ8k+wMZIovObK1s+nlwPaLyayzw9a8sUnvWB\n/5rGPdIYnQWPgoNlLN9HpSmsAcw2z8DXI9pIxbr74cb3/HSfuYGOLkRqrOk6h4RC\nOfuWoTrZup1uEOn+fw8CAwEAAaOCAVQwggFQMB0GA1UdDgQWBBQv63nQ/pJAt5tL\ny8VJcbHe22ZOsjCCAR8GA1UdIwSCARYwggESgBQv63nQ/pJAt5tLy8VJcbHe22ZO\nsqGB7qSB6zCB6DELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRMwEQYDVQQHEwpM\nb3NBbmdlbGVzMSAwHgYDVQQKExdQcml2YXRlIEludGVybmV0IEFjY2VzczEgMB4G\nA1UECxMXUHJpdmF0ZSBJbnRlcm5ldCBBY2Nlc3MxIDAeBgNVBAMTF1ByaXZhdGUg\nSW50ZXJuZXQgQWNjZXNzMSAwHgYDVQQpExdQcml2YXRlIEludGVybmV0IEFjY2Vz\nczEvMC0GCSqGSIb3DQEJARYgc2VjdXJlQHByaXZhdGVpbnRlcm5ldGFjY2Vzcy5j\nb22CCQCmew+WL/O6gzAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBDQUAA4IBAQAn\na5PgrtxfwTumD4+3/SYvwoD66cB8IcK//h1mCzAduU8KgUXocLx7QgJWo9lnZ8xU\nryXvWab2usg4fqk7FPi00bED4f4qVQFVfGfPZIH9QQ7/48bPM9R'  # ... (2174 chars total),
    '\n        Sinh file cấu hình .ovpn cho cổng proxy với giao thức TCP port 502 tương thích 100% MicroVM\n        ',
    10000,
    11200,
    'hostfwd_add net0 tcp::',
    '-:',
    '[+] Đã thêm dynamic hostfwd cho port ',
    'Dynamic hostfwd port ',
    'Đảm bảo cổng đã được forward qua QEMU Monitor nếu nằm ngoài dải tĩnh',
    '1198',
    3,
    '/api/port/add',
    45,
    '[+] Đã kết nối OpenVPN cho port ',
    '[!] Lỗi khởi chạy port ',
    ' (attempt ',
    '): ',
    1.5,
    '⚠️ Port ',
    ' kết nối chậm (',
    '), tự động thử lại lần ',
    ' sau ',
    '.1f',
    '[!] Lỗi kết nối port ',
    ' sau 3 lần thử: ',
    '[!] Exception start_openvpn_instance port ',
    '\n        Khởi chạy OpenVPN cho 1 port cụ thể thông qua MicroVM Agent Controller API\n        ',
    'OpenVPNManager._start_windows_listener.<locals>.listener_worker',
    'Lắng nghe cổng trên Windows và chuyển tiếp qua Multiplexer 28889 vào đúng namespace của MicroVM',
    '0.0.0.0',
    'OpenVPNManager._start_windows_listener.<locals>.listener_worker.<locals>.forward_conn',
    'Windows listener error port ',
    '>H',
    'OpenVPNManager._start_windows_listener.<locals>.listener_worker.<locals>.forward_conn.<locals>.pipe',
    '/api/port/delete',
    5,
    'Stop API call error port ',
    '\n        Dừng OpenVPN của 1 port và dọn sạch toàn bộ rác trong MicroVM\n        ',
    'OpenVPNManager.stop_many_openvpn_instances.<locals>.<lambda>',
    'Dừng song song nhiều cổng OpenVPN trong MicroVM siêu tốc',
    '/api/port/rotate',
    20,
    '[+] Đã xoay IP thành công cho port ',
    '[!] Lỗi xoay IP port ',
    '\n        Xoay đổi Endpoint lấy IP mới ngay lập tức cho 1 cổng proxy\n        ',
    'Kiểm tra cổng OpenVPN có đang chạy trong MicroVM không',
    '/api/port/status',
    'Lấy danh sách tất cả các cổng đang hoạt động từ MicroVM Agent',
    '/api/port/clean_all',
    'Xóa sạch 100% tất cả container, namespace, log và tunnels trong MicroVM',
    'Dừng tất cả các proxy và tắt MicroVM khi đóng ứng dụng',
    '\nOpenVPN Manager for OCProxy - Powered by Portable Zero-Dependency MicroVM Engine\nQuản lý vòng đời OpenVPN, Network Namespaces, Dynamic Add/Delete/Rotate qua Internal REST API\n',
    'http://127.0.0.1:28888',
    '\n    Quản lý Multi-OpenVPN không phụ thuộc WSL, không đụng bảng định tuyến Windows.\n    Sử dụng MicroVM Linux Engine độc lập và tương thích 100% với OCProxy API.\n    ',
)


class OpenVPNManager:

    def __init__():
        # co_varnames (args+locals, order/split approximate): stdout, stderr, text, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

    def _unpack_engine_if_needed():
        # co_varnames (args+locals, order/split approximate): timeout
        pass  # native-compiled body — faithful op trace in the .nbc

    def is_available():
        # co_varnames (args+locals, order/split approximate): stdout, stderr
        pass  # native-compiled body — faithful op trace in the .nbc

    def _is_whpx_supported():
        # co_varnames (args+locals, order/split approximate): success
        pass  # native-compiled body — faithful op trace in the .nbc

    def _is_agent_ready():
        # co_varnames (args+locals, order/split approximate): target, daemon
        pass  # native-compiled body — faithful op trace in the .nbc

    def ensure_engine_ready():
        # co_varnames (args+locals, order/split approximate): max_workers
        pass  # native-compiled body — faithful op trace in the .nbc

    def build_ovpn_config():
        # co_varnames (args+locals, order/split approximate): str, str
        pass  # native-compiled body — faithful op trace in the .nbc

    def _ensure_hostfwd():
        # co_varnames (args+locals, order/split approximate): p, cleanup_files
        pass  # native-compiled body — faithful op trace in the .nbc

    def start_openvpn_instance():
        # co_varnames (args+locals, order/split approximate): cleanup_files
        pass  # native-compiled body — faithful op trace in the .nbc

    def _start_windows_listener():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def _stop_windows_listener(self):
        # co_varnames (args+locals, order/split approximate): config_dir, binary_dir, base_dir
        pass  # native-compiled body — faithful op trace in the .nbc

    def _stop_all_windows_listeners(self):
        # co_varnames (args+locals, order/split approximate): port, s, e
        pass  # native-compiled body — faithful op trace in the .nbc

    def stop_openvpn_instance():
        # co_varnames (args+locals, order/split approximate): hostname, parts, ip
        pass  # native-compiled body — faithful op trace in the .nbc

    def stop_many_openvpn_instances(self):
        # co_varnames (args+locals, order/split approximate): timeout, r
        pass  # native-compiled body — faithful op trace in the .nbc

    def rotate_ip(self):
        # co_varnames (args+locals, order/split approximate): test_cmd, creation_flags, p, ret, out, err
        pass  # native-compiled body — faithful op trace in the .nbc

    def is_port_alive(self):
        # co_varnames (args+locals, order/split approximate): port, stop_event, listener_worker, t
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_all_status(self):
        # co_varnames (args+locals, order/split approximate): p, ev
        pass  # native-compiled body — faithful op trace in the .nbc

    def clean_all_containers(self):
        # co_varnames (args+locals, order/split approximate): port
        pass  # native-compiled body — faithful op trace in the .nbc

    def stop_all(self):
        # co_varnames (args+locals, order/split approximate): zlib_dll, base_dir, possible_zips, target_zip, z, zipfile, zf, e
        pass  # native-compiled body — faithful op trace in the .nbc

