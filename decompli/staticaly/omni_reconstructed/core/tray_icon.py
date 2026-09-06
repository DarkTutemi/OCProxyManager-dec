"""Module: core.tray_icon

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

import ctypes
from pathlib import Path
import sys
from convert import RGBA
from main import close_browser_app
from core.settings import settings_mgr


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'Tray icon loaded from: ',
    'Không thể load tray icon từ ',
    ': ',
    'Load logo.ico hoặc logo.png làm tray icon. Fallback về icon vẽ tay nếu không tìm được file.',
    'http://localhost:',
    '/#',
    'Không thể mở browser: ',
    'Mở dashboard trong browser',
    'Mở tab settings trên Web Dashboard',
    'TrayIcon._on_restart.<locals>._do_restart',
    'Lỗi khi restart process: ',
    'TrayIcon._on_exit.<locals>._force_exit',
    'Server running on port ',
    '\n🚀 Dashboard: http://localhost:',
    'OCProxy Manager',
    'Phát thông báo Toast nhẹ nhàng khi ứng dụng khởi động',
    '📊 Open Dashboard',
    '⚙️ Settings',
    '🔄 Restart',
    '🚪 Exit',
    'OCProxy Manager (:',
    ')',
    'Chạy tray icon loop (blocking)',
    'Chủ động hiển thị thông báo Toast trên khay hệ thống Windows',
    '\n    Khởi động tray icon trong thread riêng\n    \n    Args:\n        port: Port server đang chạy\n        server_stop_event: Event để signal server stop\n        \n    Returns:\n        TrayIcon instance (có thể check should_restart)\n    ',
    '\nSystem Tray Icon for PIA Proxy Manager v2\n\nKhi app start: ẩn cửa sổ console, chỉ hiển thị icon ở system tray.\nMenu chuột phải: Exit, Restart, Open Dashboard\n',
    '\n    Quản lý system tray icon\n    \n    Menu:\n    - Open Dashboard → mở browser http://localhost:PORT\n    - Settings → mở settings API\n    - Restart → restart app\n    - Exit → stop server + thoát\n    ',
)


class TrayIcon:

    def __init__():
        # co_varnames (args+locals, order/split approximate): settings_mgr
        pass  # native-compiled body — faithful op trace in the .nbc

    def _get_dashboard_url():
        # co_varnames (args+locals, order/split approximate): target, daemon
        pass  # native-compiled body — faithful op trace in the .nbc

    def _open_browser():
        # co_varnames (args+locals, order/split approximate): default
        pass  # native-compiled body — faithful op trace in the .nbc

    def _on_open():
        # co_varnames (args+locals, order/split approximate): port, server_stop_event
        pass  # native-compiled body — faithful op trace in the .nbc

    def _on_settings():
        # co_varnames (args+locals, order/split approximate): Image, ImageDraw
        pass  # native-compiled body — faithful op trace in the .nbc

    def _on_restart():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def _on_exit(self):
        # co_varnames (args+locals, order/split approximate): port, server_stop_event
        pass  # native-compiled body — faithful op trace in the .nbc

    def _on_show_notification():
        # co_varnames (args+locals, order/split approximate): candidates, base, path, img, e, size, draw, accent
        pass  # native-compiled body — faithful op trace in the .nbc

    def _setup_menu():
        # co_varnames (args+locals, order/split approximate): e
        pass  # native-compiled body — faithful op trace in the .nbc

    def run(self):
        # co_varnames (args+locals, order/split approximate): settings_mgr, current_port
        pass  # native-compiled body — faithful op trace in the .nbc

    def notify(self):
        # co_varnames (args+locals, order/split approximate): icon, item, close_browser_app, _force_exit
        pass  # native-compiled body — faithful op trace in the .nbc

    def should_restart(self):
        # co_varnames (args+locals, order/split approximate): icon, item
        pass  # native-compiled body — faithful op trace in the .nbc

