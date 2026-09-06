# Module: server
# Pseudo-source reconstructed from bytecode (no decompiler)


def HTTPServer():
    """HTTPServer"""
    ...

def ThreadingHTTPServer():
    """ThreadingHTTPServer"""
    ...

def BaseHTTPRequestHandler():
    """BaseHTTPRequestHandler"""
    ...

def SimpleHTTPRequestHandler():
    """SimpleHTTPRequestHandler"""
    ...

def _url_collapse_path(path):
    """
    
        Given a URL path, remove extra '/'s and '.' path elements and collapse
        any '..' references and returns a collapsed path.
    
        Implements something akin to RFC-2396 5.2 step 6 to parse relative paths.
        The utility of this function is limited to is_cgi method and helps
        preventing some security attacks.
    
        Returns: The reconstituted URL, which will always start with a '/'.
    
        Raises: IndexError if too many '..' occur within the path.
    
        
    """
    ...

def nobody_uid():
    """Internal routine to get nobody's uid"""
    ...

def executable(path):
    """Test for executable file."""
    ...

def CGIHTTPRequestHandler():
    """CGIHTTPRequestHandler"""
    ...

def _get_best_family(*address):
    ...

def test(HandlerClass, ServerClass, protocol, port, bind):
    """
    Test the HTTP request handler class.
    
        This runs an HTTP server on port 8000 (or the port argument).
    
        
    """
    ...

def DualStackServer():
    """DualStackServer"""
    ...
