# Module: calendar
# Pseudo-source reconstructed from bytecode (no decompiler)


def IllegalMonthError():
    """IllegalMonthError"""
    ...

def IllegalWeekdayError():
    """IllegalWeekdayError"""
    ...

def _localized_month():
    """_localized_month"""
    ...

def _localized_day():
    """_localized_day"""
    ...

def isleap(year):
    """Return True for leap years, False for non-leap years."""
    ...

def leapdays(y1, y2):
    """
    Return number of leap years in range [y1, y2).
           Assume y1 <= y2.
    """
    ...

def weekday(year, month, day):
    """Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31)."""
    ...

def monthrange(year, month):
    """
    Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
           year, month.
    """
    ...

def _monthlen(year, month):
    ...

def _prevmonth(year, month):
    ...

def _nextmonth(year, month):
    ...

def Calendar():
    """Calendar"""
    ...

def TextCalendar():
    """TextCalendar"""
    ...

def HTMLCalendar():
    """HTMLCalendar"""
    ...

def different_locale():
    """different_locale"""
    ...

def _get_default_locale():
    ...

def LocaleTextCalendar():
    """LocaleTextCalendar"""
    ...

def LocaleHTMLCalendar():
    """LocaleHTMLCalendar"""
    ...

def setfirstweekday(firstweekday):
    ...

def format(cols, colwidth, spacing):
    """Prints multi-column formatting for year calendars"""
    ...

def formatstring(cols, colwidth, spacing):
    """Returns a string formatted from n strings, centered within n columns."""
    ...

def timegm(tuple):
    """Unrelated but handy function to calculate Unix timestamp from GMT."""
    ...

def main(args):
    ...
