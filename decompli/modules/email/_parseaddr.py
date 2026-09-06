# Module: _parseaddr
# Pseudo-source reconstructed from bytecode (no decompiler)


def parsedate_tz(data):
    """
    Convert a date string to a time tuple.
    
        Accounts for military timezones.
        
    """
    ...

def _parsedate_tz(data):
    """
    Convert date to extended time tuple.
    
        The last (additional) element is the time zone offset in seconds, except if
        the timezone was specified as -0000.  In that case the last element is
        None.  This indicates a UTC timestamp that explicitly declaims knowledge of
        the source timezone, as opposed to a +0000 timestamp that indicates the
        source timezone really was UTC.
    
        
    """
    ...

def parsedate(data):
    """Convert a time string to a time tuple."""
    ...

def mktime_tz(data):
    """Turn a 10-tuple as returned by parsedate_tz() into a POSIX timestamp."""
    ...

def quote(str):
    """
    Prepare string to be used in a quoted string.
    
        Turns backslash and double quote characters into quoted pairs.  These
        are the only characters that need to be quoted inside a quoted string.
        Does not add the surrounding double quotes.
        
    """
    ...

def AddrlistClass():
    """AddrlistClass"""
    ...

def AddressList():
    """AddressList"""
    ...
