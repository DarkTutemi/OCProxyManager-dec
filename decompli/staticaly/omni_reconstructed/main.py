"""Module: main

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import aiohttp
from contextlib import asynccontextmanager
import ctypes
import datetime
import logging.handlers
from pathlib import Path
import queue
import random
import requests
import sys
import urllib.parse
from _check_single_proxy import proxy_type, http
from _create_pia_proxies import provider
from _rotate_openvpn_proxy_and_start import db
from _select_servers_for_proxy import wireguard
from add_account import id
from aiohttp_socks import ProxyConnector
from check_time import scheme
from core.dcom_mgr import dcom_mgr
from core.ipv6.group_manager import GroupManager
from core.ipv6.ipv6_manager import IPv6Manager
from core.ipv6.utils import is_admin, PortManager
from core.licensing import LicenseManager, _o
from core.openvpn_mgr import openvpn_mgr
import core.pia_api
from core.provider_servers import ProviderServerRegistry
from core.settings import settings_mgr, get_data_dir
from core.singbox_mgr import SingBoxManager
from create_group import expansion_warning
from credentials import password
from fastapi import FastAPI, HTTPException, BackgroundTasks, WebSocket, WebSocketDisconnect, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from get_countries import vpn
from get_random_servers import server_usage, exclude_ips
from get_servers import country, vpn
from get_servers_regions import pia
from initializing import tcp
from is_proxy_alive import live, running
from middleware import http
from net_connections import inet
from net_if_addrs import loopback, wintun, nord, surfshark, vpn, mobi, viettel, vina, dcom
import pydantic.main
from quote import safe
from rotate_single_v6_proxy import group_name, port
from select_servers import vpn, server_usage, exclude_ips
from start_openvpn_instance import auth_file_override
import uvicorn.access


__all__ = [
    'dcom_id',
    'db',
    'dcoms',
    'dcom',
    'port',
    'e',
]

# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    '📦 [Auto-Migration] Đã di chuyển bản quyền ',
    ' -> data/license.dat',
    '📦 [Auto-Migration] Đã di chuyển cài đặt ',
    ' -> data/settings.json',
    '📦 [Auto-Migration] Đã gom ',
    ' -> data/',
    'Lỗi auto-migration: ',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe',
    '--app=',
    '--start-maximized',
    'Không thể mở qua ',
    ': ',
    'Lỗi mở trình duyệt: ',
    'Mở giao diện dưới dạng Cửa sổ App hoặc Trình duyệt mặc định.',
    8000,
    "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*--app=http://localhost:",
    "*' -or $_.CommandLine -like '*--app=http://127.0.0.1:",
    "*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }",
    '-NoProfile',
    '-Command',
    'Tự động đóng cửa sổ trình duyệt (Chrome/Edge App Mode) khi người dùng thoát app.',
    'Tự động mở trang Dashboard hoặc License khi server sẵn sàng (bỏ qua khi khởi động ngầm cùng Windows).',
    '--autostart',
    '--minimized',
    'http://localhost:',
    '/static/license.html',
    '🌐 Đang mở giao diện Dashboard tại: ',
    'Không thể tự động mở browser trên startup: ',
    'Đảm bảo mọi response HTTP không bị trình duyệt lưu cache',
    'no-cache, no-store, must-revalidate, max-age=0, proxy-revalidate',
    'Cache-Control',
    'no-cache',
    '0',
    'Giao diện Swagger UI Premium Dark Mode với Logo Thương Hiệu ở Top-Left và độ tương phản cao sắc nét',
    'Chạy ngầm định kỳ mỗi 5 phút kiểm tra hạn bản quyền.\n    Nếu hết hạn hoặc bị thu hồi trên Server -> tự động khóa app và dừng các proxy.',
    'License heartbeat check: ',
    'N/A',
    'Kích hoạt thất bại.',
    'Background worker: kiểm tra và thực hiện auto-rotate mỗi 5 giây',
    'Auto-rotate port ',
    ' (',
    '): không có account active',
    'Auto-rotate: đã xoay OpenVPN proxy port ',
    ' sang server ',
    'Auto-rotate OpenVPN port ',
    ': lỗi xoay: ',
    '_auto_rotate_worker.<locals>._do_pia_rotate',
    'Auto-rotate: đã xoay WireGuard PIA proxy port ',
    'Auto-rotate PIA port ',
    'Auto-rotate: đã xoay ',
    ' proxy port ',
    'Auto-rotate ',
    ' port ',
    'Auto rotate Dcom error ',
    'Auto-rotate worker error: ',
    'utf-8',
    'Lỗi đọc db.json: ',
    'Lỗi ghi db.json: ',
    '127.0.0.1',
    '\n    Lấy địa chỉ IPv4 LAN nội bộ thực tế của máy tính (ưu tiên dải 192.168.x.x / 172.x.x / 10.x trên Ethernet/Wi-Fi).\n    Không lấy IP của các card mạng ảo Dcom, WireGuard, NordLynx.\n    ',
    '_get_local_ip.<locals>.<genexpr>',
    '_get_active_account.<locals>.<lambda>',
    '(?i)PrivateKey\\s*=\\s*([A-Za-z0-9+/=]+)',
    'Trích xuất Private Key từ tài khoản (tương thích cả nhập key trực tiếp hoặc dán file .conf)',
    'Start proxy (hỗ trợ cả WireGuard qua Sing-box và OpenVPN qua MicroVM Engine)',
    'Stop sing-box hoặc openvpn process của 1 proxy',
    'Lỗi start proxy port ',
    'Start tất cả enabled proxies trong group, trả về PID đầu tiên',
    'Stop tất cả proxies trong group',
    'remote\\s+([^\\s]+)\\s+(\\d+)',
    'us-california.privacy.network',
    502,
    'Không thể đọc file ',
    'Đã chọn ',
    ' OpenVPN server chính thức từ PIA configs cho ',
    ' ',
    ' server từ gluetun cache cho ',
    ' WG server từ PIA live API cho country=',
    '_create_pia_proxies.<locals>.<lambda>',
    3,
    '/32',
    'Đã đăng ký PIA proxy #',
    ': port ',
    409,
    'Conflict với server ',
    ', retry ',
    'Đã thử ',
    ' lần với server ',
    ', bỏ qua',
    'Lỗi HTTP proxy #',
    'Lỗi proxy #',
    '_create_surfshark_proxies.<locals>.<lambda>',
    'Server ',
    ' không có wgpubkey, bỏ qua',
    51820,
    'Đã tạo Surfshark proxy #',
    '_create_nordvpn_proxies.<locals>.<lambda>',
    'Đã tạo NordVPN proxy #',
    '_create_protonvpn_proxies.<locals>.<lambda>',
    'Đã tạo ProtonVPN proxy #',
    'Lỗi đếm IPv6 stats: ',
    1073741824,
    1048576,
    'Lỗi system status: ',
    500,
    'get_system_status.<locals>.<genexpr>',
    'Lỗi lấy settings: ',
    'Lỗi đọc file log: ',
    'Lỗi xóa file log: ',
    'Gửi thông báo Windows Toast qua Tray Icon báo cho người dùng biết app vẫn đang chạy ngầm phục vụ Proxy.',
    'Đã cập nhật settings',
    'Settings updated: port=',
    ', auto_startup=',
    'Lỗi cập nhật settings: ',
    'Lỗi list accounts: ',
    '(?i)PrivateKey\\s*=\\s*([a-zA-Z0-9_\\-\\+/=]+)',
    'Đã thêm tài khoản: ',
    ' [',
    '] (',
    ')',
    'Lỗi thêm account: ',
    'Đã thêm tài khoản thành công',
    'Đã xóa tài khoản: ',
    'Đã xóa tài khoản ',
    'Lỗi xóa account: ',
    'Lỗi lấy countries: ',
    '|',
    'get_servers_regions.<locals>.<lambda>',
    'Lỗi lấy regions: ',
    'Lỗi server stats: ',
    99999,
    'Lỗi list groups: ',
    '🚀 [Background] Bắt đầu khởi tạo nhóm ',
    ' ports)...',
    24,
    6,
    50,
    25,
    '_bg_setup_and_start_group.<locals>.<lambda>',
    '✅ Đã xác thực thành công tài khoản PIA: ',
    '⚠️ Tài khoản PIA (',
    ') gặp lỗi (',
    '), tự động thử tài khoản tiếp theo...',
    "Tài khoản '",
    "' không tìm thấy Private Key hợp lệ!",
    "Không có tài khoản '",
    "' nào đang active!",
    '❌ Nhóm ',
    ' không lấy được token PIA. Đánh dấu Die.',
    'Giai đoạn 2: Hậu kiểm tra Real WAN IP & Quốc gia sau khi toàn bộ đường hầm đã kết nối xong',
    '_bg_setup_and_start_group.<locals>._async_paced_verify_group',
    '_bg_setup_and_start_group.<locals>._setup_single_proxy_task',
    '⏹️ [Background] Đã nhận lệnh dừng khởi tạo nhóm ',
    '. Dọn dẹp sạch sẽ toàn bộ cổng đã tạo...',
    '🛑 [Background] Đã dừng và giải phóng 100% cổng cho nhóm bị hủy: ',
    40,
    5,
    4,
    0.2,
    0.35,
    '✅ [Background] Hoàn tất kết nối toàn bộ nhóm ',
    ' ports)',
    'Lỗi background group setup ',
    '_bg_setup_and_start_group.<locals>.<genexpr>',
    '🔍 [WAN Check] Bắt đầu xác thực Real WAN IP cho nhóm ',
    2.0,
    0.5,
    20,
    '⏹️ [WAN Check] Đã dừng xác thực IP do nhóm ',
    ' bị hủy.',
    '_bg_setup_and_start_group.<locals>._async_paced_verify_group.<locals>._verify_item',
    '🎯 [WAN Check] Đã hoàn tất gán Real WAN IP cho toàn bộ nhóm ',
    '!',
    '⚠️ Port ',
    ' kết nối server ',
    ' lỗi, tự động thử server OpenVPN thay thế...',
    '_bg_setup_and_start_group.<locals>._setup_single_proxy_task.<locals>.<lambda>',
    ' server ',
    ' bị lỗi (',
    '), đang tự động xoay server khác và cấp key mới...',
    '✅ Đã xoay thành công port ',
    ' sang server thay thế: ',
    ' - ',
    'Thử IP ',
    ' lỗi (',
    '), thử IP tiếp theo...',
    'Không thể kết nối tới bất kỳ server WireGuard nào cho port ',
    'Thiếu Private Key cho tài khoản ',
    '❌ [Background] Lỗi setup port ',
    '_bg_setup_and_start_group.<locals>._setup_single_proxy_task.<locals>.<genexpr>',
    400,
    "Chưa cấu hình tài khoản active cho nhà cung cấp '",
    "'!",
    "' chưa có Private Key hợp lệ!",
    'Không tìm thấy server ',
    ") phù hợp cho quốc gia '",
    "'",
    'Đã tạo nhóm ',
    ' proxies) và chạy setup background',
    '📢 ',
    'Đã khởi tạo nhóm ',
    'Lỗi tạo group: ',
    'create_group.<locals>.<genexpr>',
    'delete_group.<locals>._delete_configs',
    'Đã dừng tất cả tiến trình và xóa hoàn toàn group: ',
    'Đã dừng và xóa group ',
    'Lỗi xóa group: ',
    'delete_group.<locals>.<genexpr>',
    '🛑 Đã nhận yêu cầu dừng khởi tạo nhóm: ',
    'Đã gửi lệnh dừng khởi tạo nhóm ',
    'Đã dừng group: ',
    'Đã dừng group ',
    'Lỗi dừng group: ',
    'stop_group.<locals>.<genexpr>',
    'Đã khởi động group: ',
    'Đã khởi động group ',
    'Lỗi khởi động group: ',
    'start_group.<locals>.<genexpr>',
    404,
    'Không tìm thấy proxy trên port ',
    'Đã xoay IP thành công cho cổng ',
    'Lỗi xoay IP port ',
    '⚠️  Proxy port ',
    ' die, restarting...',
    '✅ Restarted proxy port ',
    '❌ Không thể restart proxy port ',
    'check_group_live.<locals>.check_proxy',
    'Check group ',
    ' live',
    'Đã check group ',
    'Lỗi check group: ',
    '.json',
    'Không thể xóa ',
    'sing-box',
    '3proxy',
    'Lỗi khi dọn dẹp IPv6 rác: ',
    'Dọn dẹp hoàn tất',
    'Clean: ',
    ' configs, ',
    ' processes',
    'Lỗi clean: ',
    'Khôi phục cài đặt gốc: Tắt toàn bộ v4 & v6 & bridge proxies, diệt mọi tiến trình, xóa DB & configs về 0',
    'Đã kill ',
    ' bridge processes',
    'Lỗi kill bridges: ',
    'Lỗi clean OpenVPN MicroVM: ',
    'Lỗi reset IPv6: ',
    'Không thể xóa file tạm ',
    'Lỗi Factory Reset: ',
    'Đọc file app.log để hiển thị log lỗi/hoạt động lên giao diện',
    'Lỗi đọc log: ',
    'Không tìm thấy proxy port ',
    ':',
    'Lỗi get proxy status: ',
    '🔄 Bật proxy port ',
    ', PID ',
    '🔄 Tắt proxy port ',
    'Đã ',
    'bật',
    'tắt',
    'Lỗi toggle proxy: ',
    'Background task to check WAN IP asynchronously without blocking HTTP response',
    'Background WAN IP check port ',
    'Background check WAN IP error port ',
    'Đã xóa lẻ proxy port ',
    'Đã xóa proxy port ',
    'Lỗi xóa lẻ proxy port ',
    'Đã rotate proxy port ',
    'Lỗi rotate proxy: ',
    "Không tìm thấy group '",
    'Không có tài khoản ',
    ' nào active',
    'rotate_group.<locals>._rot_single',
    8,
    'Đã rotate ',
    " proxy trong group '",
    'Lỗi rotate group: ',
    'rotate_group.<locals>.<genexpr>',
    ' tự động xoay cho cổng ',
    'Lỗi toggle auto-rotate: ',
    'Bật/tắt auto-rotate cho tất cả proxy (áp dụng bộ lọc frontend)',
    ' tự động xoay cho tất cả proxy',
    'Lỗi global auto-rotate: ',
    '\n    Webhook tiện ích xoay IP một chạm cho mọi bên thứ ba (Automation, Bot, MMO Tool):\n    - Hỗ trợ: `/api/rotate?port=10000`\n    - Hỗ trợ: `/api/rotate?proxy=192.168.1.10:10000`\n    - Hỗ trợ: `/api/rotate?proxy=10000:user:pass`\n    Tự động tra cứu và điều hướng xoay đúng loại Proxy (IPv4 VPN, IPv6 Subnet, hay Dcom 4G/5G).\n    ',
    'Không tìm thấy cổng proxy ',
    ' trong hệ thống (IPv4, IPv6, Dcom)',
    'universal_rotate_proxy.<locals>.<genexpr>',
    'Đổi server cho proxy port ',
    ' bị từ chối/lỗi (',
    '), đang tự động đổi sang server ',
    ' khác...',
    '✅ Đã tự động đổi sang server PIA thay thế: ',
    '✅ Rotate proxy port ',
    ' → peer IP: ',
    'Rotate keys cho 1 proxy, start lại sing-box, trả về PID',
    'Xoay sang server OpenVPN mới và khởi chạy lại tunnel trong MicroVM với cơ chế Auto-Fallback nếu server bị lỗi',
    '🔄 Đang kết nối server OpenVPN mới cho port ',
    ')...',
    ' sang server OpenVPN: ',
    '⚠️ Server ',
    ' không phản hồi tốt, tự động chuyển sang server thay thế khác cho port ',
    '...',
    '❌ Không thể kết nối OpenVPN cho port ',
    ' sau khi thử các server thay thế',
    'Port ',
    ': không tìm thấy server nào để rotate, thử random',
    ': đổi sang server ',
    ': server mới không có wgpubkey, giữ nguyên',
    'Rotate cho provider dùng key tĩnh (NordVPN, Surfshark, ProtonVPN).\n    Chỉ cần đổi server, không cần register key mới.',
    'Stop tất cả proxy trong group, start lại enabled proxies, trả về PID đầu tiên',
    '_restart_group_proxies.<locals>.<genexpr>',
    200,
    'Check 1 proxy — hỗ trợ đầy đủ xác thực tài khoản và kiểm tra WAN IP chống rò rỉ IP Host.',
    '_check_single_proxy.<locals>._try_check',
    'http://api.ipify.org?format=json',
    'http://ip-api.com/json/?fields=status,query,country,countryCode',
    'https://api.myip.com',
    '-',
    'Proxy port ',
    ' is live - IP: ',
    ' check live status: die',
    'socks5://',
    '@127.0.0.1:',
    'socks5://127.0.0.1:',
    'http://127.0.0.1:',
    '⏹️ Đã dừng khôi phục proxy theo yêu cầu!',
    'Khôi phục tất cả enabled proxies và SOCKS bridges trong nền (Non-blocking FastAPI startup)',
    'Đang khôi phục hệ thống (0/',
    '⏳ Đang khởi động MicroVM OpenVPN Engine...',
    'Đang khôi phục proxy port ',
    '✅ Tự động cấp key mới và khôi phục proxy port ',
    ' → PID ',
    '❌ Không thể cấp key mới cho port ',
    '✅ Tự động cấu hình và khôi phục proxy ',
    '❌ Lỗi cấu hình ',
    '✅ Đã khôi phục proxy port ',
    '⚠️ Không thể kết nối lại port ',
    ', đánh dấu die',
    '❌ Không thể khôi phục proxy port ',
    'Đang khôi phục SOCKS bridge port ',
    '✅ Đã khôi phục bridge port ',
    '❌ Không thể khôi phục bridge port ',
    "Đang khôi phục nhóm IPv6 '",
    "' (",
    "✅ Đã khôi phục nhóm IPv6 '",
    "❌ Không thể khôi phục nhóm IPv6 '",
    "': ",
    'Lỗi kiểm tra khôi phục IPv6: ',
    '🏁 Auto-recovery hoàn tất: ',
    ' items khôi phục thành công',
    'Hoàn tất khôi phục ',
    ' proxy!',
    'Lỗi auto-recovery: ',
    'Lỗi khôi phục: ',
    'async_auto_recover_groups.<locals>.<genexpr>',
    ' đang được sử dụng, đang giải phóng...',
    'Đã kill PID ',
    ' giữ port ',
    '/F',
    '/PID',
    ' giải phóng sau ',
    'Không thể giải phóng port ',
    '@',
    'http://ip-api.com/json/',
    '?fields=status,country,countryCode',
    'Kiểm tra chuỗi có phải IP hợp lệ không (tránh nhận nginx HTML làm IP).',
    '\n    Test 1 proxy bên ngoài siêu tốc:\n    - Timeout tùy biến (mặc định 6.5s total / 4.5s connect).\n    - 1-Shot query ip-api.com lấy đồng thời IP thật + Quốc gia + Mã cờ trong 1 request duy nhất.\n    - Phân luồng chính xác theo scheme (HTTP / SOCKS5).\n    ',
    'Lỗi định dạng',
    1.5,
    '_test_single_custom_proxy.<locals>._probe_with_session',
    '_test_single_custom_proxy.<locals>._try_socks5',
    '_test_single_custom_proxy.<locals>._try_http',
    'Không kết nối',
    'http://',
    'check_live_proxies_batch.<locals>._sem_check',
    '\n    Full-duplex WebSocket endpoint kiểm tra Live Proxy siêu tốc:\n    - Client gửi danh sách proxy kèm số luồng (ví dụ 100 luồng) và loại proxy (auto/http/socks5) qua Socket.\n    - Server kích hoạt 100 worker song song trong nền.\n    - Kết quả từng proxy được bắn tức thời qua WebSocket về giao diện (Zero Latency).\n    ',
    'websocket_check_live.<locals>.worker',
    'WebSocket check-live error: ',
    'Lỗi quét danh sách card mạng: ',
    "🔄 Đang chuyển đổi card mạng IPv6 sang '",
    "'. Xóa toàn bộ cấu hình cũ...",
    'Lỗi xóa nhóm ',
    ' khi đổi card mạng: ',
    "Không thể kích hoạt card mạng '",
    "Đã chuyển sang card mạng '",
    "' thành công!",
    'Lỗi chuyển card mạng: ',
    "Đã tạo nhóm IPv6 '",
    ') với ',
    ' proxies',
    "Nhóm '",
    "' không tồn tại",
    "Đã xóa nhóm IPv6 '",
    "' đang tắt, hãy bật trước khi xoay",
    "Đã xoay IP cho tất cả proxy trong nhóm '",
    "' thành công",
)

_recovered_data_0 = {'status': 'success', 'message': 'Kích hoạt bản quyền thành công!'}

_recovered_data_1 = {'us': ['us_'], 'ca': ['ca_'], 'au': ['au_', 'australia'], 'uk': ['uk_'], 'gb': ['uk_'], 'de': ['de_', 'germany'], 'dk': ['dk_', 'denmark'], 'es': ['es_', 'spain'], 'fi': ['fi_', 'finland'], 'it': ['it_', 'italy'], 'jp': ['jp_', 'japan'], 'nl': ['nl_', 'netherlands'], 'se': ['se_', 'sweden'], 'fr': ['france'], 'sg': ['singapore'], 'hk': ['hong_kong'], 'vn': ['vietnam'], 'tw': ['taiwan'], 'kr': ['south_korea'], 'za': ['south_africa'], 'kh': ['cambodia'], 'cr': ['costa_rica'], 'mo': ['macao'], 'ch': ['switzerland'], 'br': ['brazil'], 'mx': ['mexico'], 'pl': ['poland'], 'ae': ['united_arab_emirates'], 'tr': ['turkey'], 'no': ['norway'], 'nz': ['new_zealand'], 'in': ['india'], 'id': ['indonesia'], 'my': ['malaysia'], 'ph': ['philippines'], 'th': ['thailand'], 'ie': ['ireland'], 'be': ['belgium'], 'at': ['austria'], 'cz': ['czech_republic'], 'ro': ['romania'], 'hu': ['hungary'], 'gr': ['greece'], 'pt': ['portugal'], 'bg': ['bulgaria'], 'ua': ['ukraine'], 'il': ['israel'], 'eg': ['egypt'], 'ar': ['argentina'], 'cl': ['chile'], 'co': ['colombia'], 'pe': ['peru']}

_recovered_data_2 = {'logs': []}

_recovered_data_3 = {'status': 'success', 'message': 'Đã xóa sạch nội dung file log.'}

_recovered_data_4 = {'accounts': [], 'groups': [], 'bridges': [], 'dcom_proxies': [], 'server_usage': {}}

_recovered_data_5 = {'groups': []}

_recovered_data_6 = {'status': 'ok', 'message': 'Hệ thống đã được khôi phục cài đặt gốc hoàn toàn sạch sẽ (Bản quyền được giữ nguyên)!'}

_recovered_data_7 = {'logs': ['Chưa có log ghi nhận.']}

_recovered_data_8 = {'proxies': {}}

_recovered_data_9 = {'status': 'ok', 'message': 'Đã gửi lệnh dừng khôi phục proxy'}

_recovered_data_10 = {'return_exceptions': True}

_recovered_data_11 = [{'name': 'VPN Proxies (IPv4)', 'description': 'Quản lý tạo nhóm, khởi chạy, kiểm tra và xoay Proxy IPv4 qua WireGuard VPN'}, {'name': 'IPv6 Dynamic Proxies', 'description': 'Tạo và xoay cụm Proxy IPv6 tự động từ dải IPv6 Subnet trên card mạng'}, {'name': 'SOCKS-to-HTTP Bridge', 'description': 'Chuyển đổi Proxy SOCKS5 sang cổng local HTTP proxy bằng Sing-box Core'}, {'name': 'Mobile 4G/5G (Dcom)', 'description': 'Quản lý Proxy di động 4G/5G qua Dcom/USB Modem, quay số Rasdial, HiLink và xoay IP'}, {'name': 'Proxy Tools & Live Check', 'description': 'Kiểm tra tình trạng Live/Die proxy qua WebSocket hai chiều siêu tốc'}, {'name': 'Auto Rotation', 'description': 'Cấu hình tự động đổi IP định kỳ theo chu kỳ thời gian (giây)'}, {'name': 'Accounts & Providers', 'description': 'Quản lý tài khoản VPN Provider và truy vấn danh sách máy chủ khả dụng'}, {'name': 'System & Settings', 'description': 'Cấu hình cổng Web, tự khởi động cùng Windows, dọn dẹp hệ thống và khôi phục cài đặt gốc'}]

_recovered_data_12 = {'is_recovering': False, 'total': 0, 'current': 0, 'recovered': 0, 'message': ''}


class ErrorAndMainFilter:

    def filter():
        # co_varnames (args+locals, order/split approximate): stdout, stderr, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

