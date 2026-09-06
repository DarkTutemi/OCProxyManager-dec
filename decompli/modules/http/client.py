# Module: client
# Pseudo-source reconstructed from bytecode (no decompiler)


def _encode(data, name):
    """Call data.encode("latin-1") but show a better error message."""
    ...

def _strip_ipv6_iface(enc_name):
    """Remove interface scope from IPv6 address."""
    ...

def HTTPMessage():
    """HTTPMessage"""
    ...

def _read_headers(fp):
    """
    Reads potential header lines into a list from a file pointer.
    
        Length of line is limited by _MAXLINE, and number of
        headers is limited by _MAXHEADERS.
        
    """
    ...

def parse_headers(fp, _class):
    """
    Parses only RFC2822 headers from a file pointer.
    
        email Parser wants to see strings rather than bytes.
        But a TextIOWrapper around self.rfile would buffer too many bytes
        from the stream, bytes which we later need to read as bytes.
        So we read the correct bytes here, as bytes, for email Parser
        to parse.
    
        
    """
    ...

def HTTPResponse():
    """HTTPResponse"""
    ...

def HTTPConnection():
    """HTTPConnection"""
    ...

def HTTPSConnection():
    """HTTPSConnection"""
    ...

def HTTPException():
    """HTTPException"""
    ...

def NotConnected():
    """NotConnected"""
    ...

def InvalidURL():
    """InvalidURL"""
    ...

def UnknownProtocol():
    """UnknownProtocol"""
    ...

def UnknownTransferEncoding():
    """UnknownTransferEncoding"""
    ...

def UnimplementedFileMode():
    """UnimplementedFileMode"""
    ...

def IncompleteRead():
    """IncompleteRead"""
    ...

def ImproperConnectionState():
    """ImproperConnectionState"""
    ...

def CannotSendRequest():
    """CannotSendRequest"""
    ...

def CannotSendHeader():
    """CannotSendHeader"""
    ...

def ResponseNotReady():
    """ResponseNotReady"""
    ...

def BadStatusLine():
    """BadStatusLine"""
    ...

def LineTooLong():
    """LineTooLong"""
    ...

def RemoteDisconnected():
    """RemoteDisconnected"""
    ...
