# Module: datetime
# Pseudo-source reconstructed from bytecode (no decompiler)


def _cmp(x, y):
    ...

def _is_leap(year):
    """year -> 1 if leap year, else 0."""
    ...

def _days_before_year(year):
    """year -> number of days before January 1st of year."""
    ...

def _days_in_month(year, month):
    """year, month -> number of days in that month in that year."""
    ...

def _days_before_month(year, month):
    """year, month -> number of days in year preceding first day of month."""
    ...

def _ymd2ord(year, month, day):
    """year, month, day -> ordinal, considering 01-Jan-0001 as day 1."""
    ...

def _ord2ymd(n):
    """ordinal -> (year, month, day), considering 01-Jan-0001 as day 1."""
    ...

def _build_struct_time(y, m, d, hh, mm, ss, dstflag):
    ...

def _format_time(hh, mm, ss, us, timespec):
    ...

def _format_offset(off):
    ...

def _wrap_strftime(object, format, timetuple):
    ...

def _is_ascii_digit(c):
    ...

def _find_isoformat_datetime_separator(dtstr):
    ...

def _parse_isoformat_date(dtstr):
    ...

def _parse_hh_mm_ss_ff(tstr):
    ...

def _parse_isoformat_time(tstr):
    ...

def _isoweek_to_gregorian(year, week, day):
    ...

def _check_tzname(name):
    ...

def _check_utc_offset(name, offset):
    ...

def _check_date_fields(year, month, day):
    ...

def _check_time_fields(hour, minute, second, microsecond, fold):
    ...

def _check_tzinfo_arg(tz):
    ...

def _cmperror(x, y):
    ...

def _divide_and_round(a, b):
    """
    divide a by b and round result to the nearest integer
    
        When the ratio is exactly half-way between two integers,
        the even integer is returned.
        
    """
    ...

def timedelta():
    """timedelta"""
    ...

def date():
    """date"""
    ...

def tzinfo():
    """tzinfo"""
    ...

def IsoCalendarDate():
    """IsoCalendarDate"""
    ...

def time():
    """time"""
    ...

def datetime():
    """datetime"""
    ...

def _isoweek1monday(year):
    ...

def timezone():
    """timezone"""
    ...
