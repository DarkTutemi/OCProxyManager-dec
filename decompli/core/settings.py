"""Module: core.settings

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

from pathlib import Path
import sys
from stdout import Ready, Running


# --- string / numeric literals recovered from the constant pool ---
# (the original variable bindings are gone; the values are exact)
_recovered_literals = (
    'Lấy thư mục data bền vững (nơi chứa settings.json, db.json, v6_config.json, license.dat)',
    'Lấy đường dẫn tới main executable/script',
    'Lỗi di chuyển settings.json cũ: ',
    'utf-8',
    'Không thể đọc settings.json: ',
    'Đọc settings từ file',
    'Đã lưu settings → ',
    'Lỗi ghi settings.json: ',
    'Ghi settings ra file',
    'Lấy toàn bộ settings',
    'Cập nhật settings và áp dụng',
    'Bật/tắt auto-start thông qua Windows Task Scheduler',
    'Kiểm tra process hiện tại có đang chạy quyền Admin không',
    "-Argument '--autostart'",
    '-Argument \'"',
    '" --autostart\'',
    "\n        $user = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name\n        $action = New-ScheduledTaskAction -Execute '",
    "' ",
    " -WorkingDirectory '",
    '\'\n        $trigger = New-ScheduledTaskTrigger -AtLogOn\n        $principal = New-ScheduledTaskPrincipal -UserId $user -LogonType Interactive -RunLevel Highest\n        $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit 0 -Priority 3\n        Register-ScheduledTask -TaskName "OCProxyManager" -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force\n        ',
    '-NoProfile',
    '-NonInteractive',
    '-Command',
    '✅ Đã đăng ký auto-start (Task Scheduler: OCProxyManager, WorkDir: ',
    ')',
    '⚠️  Lỗi đăng ký auto-start: ',
    'Lỗi khi đăng ký auto-start: ',
    'Tạo Task Scheduler để chạy app khi người dùng đăng nhập với quyền Admin cao nhất (RunLevel Highest)',
    134217728,
    "Unregister-ScheduledTask -TaskName '",
    "' -Confirm:$false -ErrorAction SilentlyContinue",
    15,
    '✅ Đã xóa auto-start (Task Scheduler: ',
    'Lỗi khi xóa auto-start ',
    ': ',
    'Xóa Task Scheduler (xóa cả tên cũ PIAProxyManager lẫn tên mới OCProxyManager)',
    'Kiểm tra Task Scheduler đã đăng ký chưa (check cả tên mới OCProxyManager lẫn tên cũ)',
    '\nSettings Manager for PIA Proxy Manager v2\n\nQuản lý settings.json (port, auto_startup) và Auto-start trên Windows.\n',
    'Quản lý cài đặt hệ thống',
)

_recovered_data_0 = {'port': 8000, 'auto_startup': False}


class SettingsManager:

    def __init__():
        # co_varnames (args+locals, order/split approximate): capture_output, text, timeout, creationflags
        pass  # native-compiled body — faithful op trace in the .nbc

    def _load():
        # co_varnames (args+locals, order/split approximate): OCProxyManager, PIAProxyManager
        pass  # native-compiled body — faithful op trace in the .nbc

    def _save():
        # co_varnames (args+locals, order/split approximate): __class__
        pass  # native-compiled body — faithful op trace in the .nbc

    def port(self):
        # co_varnames (args+locals, order/split approximate): data_dir, legacy_file, shutil, me
        pass  # native-compiled body — faithful op trace in the .nbc

    def auto_startup(self):
        # co_varnames (args+locals, order/split approximate): enable
        pass  # native-compiled body — faithful op trace in the .nbc

    def get_all(self):
        # co_varnames (args+locals, order/split approximate): f, data, merged, e
        pass  # native-compiled body — faithful op trace in the .nbc

    def update(self):
        # co_varnames (args+locals, order/split approximate): task_name, exe_path, arg_part, work_dir, main_py, ps_cmd, no_window, result, e
        pass  # native-compiled body — faithful op trace in the .nbc

    def _apply_auto_startup(self):
        # co_varnames (args+locals, order/split approximate): f, e
        pass  # native-compiled body — faithful op trace in the .nbc

    def is_admin(self):
        # co_varnames (args+locals, order/split approximate): no_window, task_name, result, e
        pass  # native-compiled body — faithful op trace in the .nbc

    def _register_scheduled_task(self):
        pass  # native-compiled body — faithful op trace in the .nbc

    def _unregister_scheduled_task(self):
        # co_varnames (args+locals, order/split approximate): value
        pass  # native-compiled body — faithful op trace in the .nbc

    def is_task_registered():
        # co_varnames (args+locals, order/split approximate): base_dir, data_dir
        pass  # native-compiled body — faithful op trace in the .nbc

