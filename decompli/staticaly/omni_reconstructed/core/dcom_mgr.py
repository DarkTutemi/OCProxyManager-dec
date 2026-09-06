"""Module: core.dcom_mgr

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import asyncio
import logging
import socket
import sys
import urllib.parse
import urllib.request
from com_at import com_port
from custom import delay_seconds
from ensure_profile_isolated import rasdial_user
from findtext import SesInfo
import rasphone.pbk
from scan_com_ports import port


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'utf-8',
    '^\\[(.*)\\]\\s*$',
    'Lỗi đọc file ',
    ': ',
    'kết nối',
    'Quét tất cả profile kết nối Dial-up / Dcom thực tế (đã lọc bỏ VPN software).',
    'SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e96d-e325-11ce-bfc1-08002be10318}',
    'HARDWARE\\DEVICEMAP\\SERIALCOMM',
    'USB 3G/4G Modem',
    ' ➔ [Rasdial: ',
    ']',
    ' - ',
    'Lỗi quét cổng COM qua Registry: ',
    'Quét danh sách cổng COM của Modem / USB Dongle 4G-5G thực tế (kèm tên thiết bị Modem chính xác).',
    'Tra cứu card mạng (Rasdial profile) tương ứng với 1 cổng COM.',
    'http://',
    '/api/webserver/SesTokInfo',
    'Huawei/ZTE HiLink Dongle',
    'Quét các Gateway HiLink của Huawei/ZTE USB Dongle (chỉ nhận khi có API HiLink thực tế).',
    'Kiểm tra xem tên profile có phải là phần mềm VPN thương mại không.',
    'Thực hiện quét toàn diện: Rasdial Profiles + COM Ports + HiLink Gateways.',
    '[',
    'IpPrioritizeRemote=0',
    '\r\n',
    'Không thể cấu hình pbk tại ',
    '\n        Cấu hình Profile Rasdial độc lập (IpPrioritizeRemote=0):\n        Đảm bảo khi Dcom kết nối, Windows KHÔNG đổi Default Gateway của máy tính,\n        giúp máy tính chủ giữ nguyên mạng LAN/WiFi gốc, không bị đổi IP máy chủ.\n        ',
    'Đang ngắt kết nối Rasdial: ',
    '/disconnect',
    10,
    '192.168.8.1',
    b'AT+CFUN=0\r\n',
    'Lỗi khi ngắt kết nối Dcom: ',
    'Ngắt kết nối phần cứng mạng của Dcom khi tắt proxy hoặc xóa proxy khỏi hệ thống.',
    'Đang kết nối lại Rasdial: ',
    20,
    'Successfully connected',
    'đã kết nối',
    '✅ Đã kết nối thành công Rasdial: ',
    "Cảnh báo kết nối Rasdial '",
    "': ",
    'Lỗi khi kết nối lại Dcom: ',
    'Kết nối lại phần cứng mạng của Dcom khi bật lại switch proxy hoặc tạo mới.',
    "Get-NetIPAddress -InterfaceAlias '",
    "' -AddressFamily IPv4 -ErrorAction SilentlyContinue | ForEach-Object { New-NetRoute -InterfaceIndex $_.InterfaceIndex -DestinationPrefix '0.0.0.0/0' -NextHop '0.0.0.0' -RouteMetric 500 -ErrorAction SilentlyContinue | Out-Null }",
    '-NoProfile',
    '-Command',
    6,
    "⚡ Đã thiết lập Isolated Outbound Route (Metric 500) cho Dcom '",
    "'",
    'Không thể tạo route phụ cho Dcom: ',
    '\n        Cấp thêm tuyến định tuyến 0.0.0.0/0 (Metric 500) cho interface Dcom:\n        Giúp socket bind interface đi ra ngoài được Internet 4G/5G,\n        đồng thời Metric 500 cao hơn nhiều so với Ethernet (Metric 25) nên máy chủ vẫn dùng mạng LAN.\n        ',
    3.5,
    2.5,
    4.5,
    5.5,
    'Chờ ',
    's ngắt sóng để trạm BTS cấp IP mới...',
    'connected to',
    "Xoay IP Rasdial '",
    "' thành công",
    'Thử kết nối lại lần 2 cho ',
    '...',
    "' thành công (Lần 2)",
    'Lỗi kết nối lại',
    'Lỗi Rasdial: ',
    "Kết nối lại Rasdial profile '",
    "' sau khi reset sóng COM...",
    'Thực thi Custom Command: ',
    15,
    'Lỗi lệnh: ',
    'Chế độ xoay không hỗ trợ: ',
    'Lỗi xoay IP Dcom: ',
    'Lỗi ngoại lệ: ',
    '\n        Thực hiện xoay IP cho 1 Dcom dựa theo mode cấu hình.\n        Trả về: (thành_công: bool, thông_báo: str)\n        ',
    '/api/dialup/mobile-dataswitch',
    b'<?xml version="1.0" encoding="UTF-8"?><request><dataswitch>0</dataswitch></request>',
    b'<?xml version="1.0" encoding="UTF-8"?><request><dataswitch>1</dataswitch></request>',
    200,
    'Xoay IP HiLink (',
    ') thành công',
    'Đã gửi lệnh xoay IP tới HiLink (',
    ')',
    'Lỗi kết nối HiLink ',
    'Gửi lệnh đổi dữ liệu di động qua Web API của HiLink Huawei/ZTE.',
    '1',
    '0',
    'Bật hoặc tắt kết nối dữ liệu di động HiLink.',
    b'AT+CFUN=1\r\n',
    'Xoay IP qua cổng ',
    ' thành công',
    'Không thể gửi lệnh AT Command tới cổng ',
    'Gửi lệnh AT Command qua cổng Serial COM (AT+CFUN=0/1) với thời gian chờ chuẩn để ép đổi IP.',
    115200,
    'Gửi lệnh AT Command qua cổng COM Serial (tự động thử các cổng COM khả dụng nếu cổng chính đang bận).',
    '4G/5G Cellular',
    'Nhận diện tên nhà mạng từ tên profile kết nối.',
    134217728,
    '\n    Quản lý phần cứng Dcom / USB 4G-5G, quét thiết bị và tự động xoay IP\n    Hỗ trợ: Rasdial, HiLink Web API, Cổng COM (AT Command), Lệnh Custom Command.\n    ',
)

_recovered_data_0 = ['192.168.8.1', '192.168.9.1', '192.168.10.1', '192.168.100.1']

_recovered_data_1 = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

_recovered_data_2 = ['purevpn', 'nordvpn', 'expressvpn', 'surfshark', 'pia', 'proton', 'openvpn', 'wireguard', 'sstp', 'l2tp', 'ikev2', 'pptp', 'vpn', 'cisco', 'forticlient', 'anyconnect', 'tailscale', 'zerotier', 'softether', 'warp', '1.1.1.1']


class DcomManager:

    def __init__():
        # co_varnames (args+locals, order/split approximate): capture_output, text, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

    def scan_rasdial_profiles():
        # co_varnames (args+locals, order/split approximate): headers
        pass  # native-compiled body — faithful op trace in the .nbc

    def scan_com_ports():
        # co_varnames (args+locals, order/split approximate): capture_output, text, creationflags, timeout
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_interface_for_com():
        # co_varnames (args+locals, order/split approximate): hilink_ip
        pass  # native-compiled body — faithful op trace in the .nbc

    def scan_hilink_gateways():
        # co_varnames (args+locals, order/split approximate): enable
        pass  # native-compiled body — faithful op trace in the .nbc

    def _is_vpn_profile():
        # co_varnames (args+locals, order/split approximate): capture_output, creationflags, timeout
        pass  # native-compiled body — faithful op trace in the .nbc

    def full_scan():
        # co_varnames (args+locals, order/split approximate): delay_preset, default
        pass  # native-compiled body — faithful op trace in the .nbc

    def ensure_profile_isolated():
        # co_varnames (args+locals, order/split approximate): shell, capture_output, text, timeout, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

    def disconnect_dcom():
        # co_varnames (args+locals, order/split approximate): data, headers, method
        pass  # native-compiled body — faithful op trace in the .nbc

    def connect_dcom():
        # co_varnames (args+locals, order/split approximate): COM10, COM8, COM9, COM3, COM4, COM11
        pass  # native-compiled body — faithful op trace in the .nbc

    def setup_interface_isolated_route():
        # co_varnames (args+locals, order/split approximate): bool, str
        pass  # native-compiled body — faithful op trace in the .nbc

    def rotate_ip():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def _rotate_hilink(self):
        pass  # native-compiled body — faithful op trace in the .nbc

    def _set_hilink_data(self):
        # co_varnames (args+locals, order/split approximate): name, nl
        pass  # native-compiled body — faithful op trace in the .nbc

    def _rotate_com_at(self):
        # co_varnames (args+locals, order/split approximate): name, nl, vpn
        pass  # native-compiled body — faithful op trace in the .nbc

    def _send_at_command(self):
        # co_varnames (args+locals, order/split approximate): com_port, delay_seconds, ok1, ok2
        pass  # native-compiled body — faithful op trace in the .nbc

    def _detect_carrier_from_name(self):
        # co_varnames (args+locals, order/split approximate): gateway_ip, urllib, ET, base_url, session_id, token, req, resp, xml_str, root, headers, data_off, req_off, data_on, req_on, res_body, e
        pass  # native-compiled body — faithful op trace in the .nbc

