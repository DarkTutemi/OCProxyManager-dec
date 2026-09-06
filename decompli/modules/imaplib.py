# Module: imaplib
# Pseudo-source reconstructed from bytecode (no decompiler)


def IMAP4():
    """IMAP4"""
    ...

def IMAP4_SSL():
    """IMAP4_SSL"""
    ...

def IMAP4_stream():
    """IMAP4_stream"""
    ...

def _Authenticator():
    """_Authenticator"""
    ...

def Internaldate2tuple(resp):
    """
    Parse an IMAP4 INTERNALDATE string.
    
        Return corresponding local time.  The return value is a
        time.struct_time tuple or None if the string has wrong format.
        
    """
    ...

def Int2AP(num):
    """Convert integer to A-P string representation."""
    ...

def ParseFlags(resp):
    """Convert IMAP4 flags response to python tuple."""
    ...

def Time2Internaldate(date_time):
    """
    Convert date_time to IMAP4 INTERNALDATE representation.
    
        Return string in form: '"DD-Mmm-YYYY HH:MM:SS +HHMM"'.  The
        date_time argument can be a number (int or float) representing
        seconds since epoch (as returned by time.time()), a 9-tuple
        representing local time, an instance of time.struct_time (as
        returned by time.localtime()), an aware datetime instance or a
        double-quoted string.  In the last case, it is assumed to already
        be in the correct format.
        
    """
    ...

def run(cmd, args):
    ...
