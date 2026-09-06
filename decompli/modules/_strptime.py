# Module: _strptime
# Pseudo-source reconstructed from bytecode (no decompiler)


def _getlang():
    ...

def LocaleTime():
    """LocaleTime"""
    ...

def TimeRE():
    """TimeRE"""
    ...

def _calc_julian_from_U_or_W(year, week_of_year, day_of_week, week_starts_Mon):
    """
    Calculate the Julian day based on the year, week of the year, and day of
        the week, with week_start_day representing whether the week of the year
        assumes the week starts on Sunday or Monday (6 or 0).
    """
    ...

def _calc_julian_from_V(iso_year, iso_week, iso_weekday):
    """
    Calculate the Julian day based on the ISO 8601 year, week, and weekday.
        ISO weeks start on Mondays, with week 01 being the week containing 4 Jan.
        ISO week days range from 1 (Monday) to 7 (Sunday).
        
    """
    ...

def _strptime(data_string, format):
    """
    Return a 2-tuple consisting of a time struct and an int containing
        the number of microseconds based on the input string and the
        format string.
    """
    ...

def _strptime_time(data_string, format):
    """
    Return a time struct based on the input string and the
        format string.
    """
    ...

def _strptime_datetime(cls, data_string, format):
    """
    Return a class cls instance based on the input string and the
        format string.
    """
    ...
