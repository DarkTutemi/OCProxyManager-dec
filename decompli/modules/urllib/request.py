# Module: request
# Pseudo-source reconstructed from bytecode (no decompiler)


def urlopen(url, data, timeout, *, cafile=None, capath=None, cadefault=None, context=None):
    """
    Open the URL url, which can be either a string or a Request object.
    
        *data* must be an object specifying additional data to be sent to
        the server, or None if no such data is needed.  See Request for
        details.
    
        urllib.request module uses HTTP/1.1 and includes a "Connection:close"
        header in its HTTP requests.
    
        The optional *timeout* parameter specifies a timeout in seconds for
        blocking operations like the connection attempt (if not specified, the
        global default timeout setting will be used). This only works for HTTP,
        HTTPS and FTP connections.
    
        If *context* is specified, it must be a ssl.SSLContext instance describing
        the various SSL options. See HTTPSConnection for more details.
    
        The optional *cafile* and *capath* parameters specify a set of trusted CA
        certificates for HTTPS requests. cafile should point to a single file
        containing a bundle of CA certificates, whereas capath should point to a
        directory of hashed certificate files. More information can be found in
        ssl.SSLContext.load_verify_locations().
    
        The *cadefault* parameter is ignored.
    
    
        This function always returns an object which can work as a
        context manager and has the properties url, headers, and status.
        See urllib.response.addinfourl for more detail on these properties.
    
        For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse
        object slightly modified. In addition to the three new methods above, the
        msg attribute contains the same information as the reason attribute ---
        the reason phrase returned by the server --- instead of the response
        headers as it is specified in the documentation for HTTPResponse.
    
        For FTP, file, and data URLs and requests explicitly handled by legacy
        URLopener and FancyURLopener classes, this function returns a
        urllib.response.addinfourl object.
    
        Note that None may be returned if no handler handles the request (though
        the default installed global OpenerDirector uses UnknownHandler to ensure
        this never happens).
    
        In addition, if proxy settings are detected (for example, when a *_proxy
        environment variable like http_proxy is set), ProxyHandler is default
        installed and makes sure the requests are handled through the proxy.
    
        
    """
    ...

def install_opener(opener):
    ...

def urlretrieve(url, filename, reporthook, data):
    """
    
        Retrieve a URL into a temporary location on disk.
    
        Requires a URL argument. If a filename is passed, it is used as
        the temporary file location. The reporthook argument should be
        a callable that accepts a block number, a read size, and the
        total file size of the URL target. The data argument should be
        valid URL encoded data.
    
        If a filename is passed and the URL points to a local resource,
        the result is a copy from local file to new file.
    
        Returns a tuple containing the path to the newly created
        data file as well as the resulting HTTPMessage object.
        
    """
    ...

def urlcleanup():
    """Clean up temporary files from urlretrieve calls."""
    ...

def request_host(request):
    """
    Return request-host, as defined by RFC 2965.
    
        Variation from RFC: returned value is lowercased, for convenient
        comparison.
    
        
    """
    ...

def Request():
    """Request"""
    ...

def OpenerDirector():
    """OpenerDirector"""
    ...

def build_opener(*handlers):
    """
    Create an opener object from a list of handlers.
    
        The opener will use several default handlers, including support
        for HTTP, FTP and when applicable HTTPS.
    
        If any of the handlers passed as arguments are subclasses of the
        default handlers, the default handlers will not be used.
        
    """
    ...

def BaseHandler():
    """BaseHandler"""
    ...

def HTTPErrorProcessor():
    """HTTPErrorProcessor"""
    ...

def HTTPDefaultErrorHandler():
    """HTTPDefaultErrorHandler"""
    ...

def HTTPRedirectHandler():
    """HTTPRedirectHandler"""
    ...

def _parse_proxy(proxy):
    """
    Return (scheme, user, password, host/port) given a URL or an authority.
    
        If a URL is supplied, it must have an authority (host:port) component.
        According to RFC 3986, having an authority component means the URL must
        have two slashes after the scheme.
        
    """
    ...

def ProxyHandler():
    """ProxyHandler"""
    ...

def HTTPPasswordMgr():
    """HTTPPasswordMgr"""
    ...

def HTTPPasswordMgrWithDefaultRealm():
    """HTTPPasswordMgrWithDefaultRealm"""
    ...

def HTTPPasswordMgrWithPriorAuth():
    """HTTPPasswordMgrWithPriorAuth"""
    ...

def AbstractBasicAuthHandler():
    """AbstractBasicAuthHandler"""
    ...

def HTTPBasicAuthHandler():
    """HTTPBasicAuthHandler"""
    ...

def ProxyBasicAuthHandler():
    """ProxyBasicAuthHandler"""
    ...

def AbstractDigestAuthHandler():
    """AbstractDigestAuthHandler"""
    ...

def HTTPDigestAuthHandler():
    """HTTPDigestAuthHandler"""
    ...

def ProxyDigestAuthHandler():
    """ProxyDigestAuthHandler"""
    ...

def AbstractHTTPHandler():
    """AbstractHTTPHandler"""
    ...

def HTTPHandler():
    """HTTPHandler"""
    ...

def HTTPSHandler():
    """HTTPSHandler"""
    ...

def HTTPCookieProcessor():
    """HTTPCookieProcessor"""
    ...

def UnknownHandler():
    """UnknownHandler"""
    ...

def parse_keqv_list(l):
    """Parse list of key=value strings where keys are not duplicated."""
    ...

def parse_http_list(s):
    """
    Parse lists as described by RFC 2068 Section 2.
    
        In particular, parse comma-separated lists where the elements of
        the list may include quoted-strings.  A quoted-string could
        contain a comma.  A non-quoted string could have quotes in the
        middle.  Neither commas nor quotes count if they are escaped.
        Only double-quotes count, not single-quotes.
        
    """
    ...

def FileHandler():
    """FileHandler"""
    ...

def _safe_gethostbyname(host):
    ...

def FTPHandler():
    """FTPHandler"""
    ...

def CacheFTPHandler():
    """CacheFTPHandler"""
    ...

def DataHandler():
    """DataHandler"""
    ...

def url2pathname(pathname):
    """
    OS-specific conversion from a relative URL of the 'file' scheme
            to a file system path; not recommended for general use.
    """
    ...

def pathname2url(pathname):
    """
    OS-specific conversion from a file system path to a relative URL
            of the 'file' scheme; not recommended for general use.
    """
    ...

def URLopener():
    """URLopener"""
    ...

def FancyURLopener():
    """FancyURLopener"""
    ...

def localhost():
    """Return the IP address of the magic hostname 'localhost'."""
    ...

def thishost():
    """Return the IP addresses of the current host."""
    ...

def ftperrors():
    """Return the set of errors raised by the FTP class."""
    ...

def noheaders():
    """Return an empty email Message object."""
    ...

def ftpwrapper():
    """ftpwrapper"""
    ...

def getproxies_environment():
    """
    Return a dictionary of scheme -> proxy server URL mappings.
    
        Scan the environment for variables named <scheme>_proxy;
        this seems to be the standard convention.  If you need a
        different way, you can pass a proxies dictionary to the
        [Fancy]URLopener constructor.
    
        
    """
    ...

def proxy_bypass_environment(host, proxies):
    """
    Test if proxies should not be used for a particular host.
    
        Checks the proxy dict for the value of no_proxy, which should
        be a list of comma separated DNS suffixes, or '*' for all hosts.
    
        
    """
    ...

def _proxy_bypass_macosx_sysconf(host, proxy_settings):
    """
    
        Return True iff this host shouldn't be accessed using a proxy
    
        This function uses the MacOSX framework SystemConfiguration
        to fetch the proxy information.
    
        proxy_settings come from _scproxy._get_proxy_settings or get mocked ie:
        { 'exclude_simple': bool,
          'exceptions': ['foo.bar', '*.bar.com', '127.0.0.1', '10.1', '10.0/16']
        }
        
    """
    ...

def _proxy_bypass_winreg_override(host, override):
    """
    Return True if the host should bypass the proxy server.
    
        The proxy override list is obtained from the Windows
        Internet settings proxy override registry value.
    
        An example of a proxy override value is:
        "www.example.com;*.example.net; 192.168.0.1"
        
    """
    ...

def proxy_bypass_macosx_sysconf(host):
    ...

def getproxies_macosx_sysconf():
    """
    Return a dictionary of scheme -> proxy server URL mappings.
    
            This function uses the MacOSX framework SystemConfiguration
            to fetch the proxy information.
            
    """
    ...

def proxy_bypass(host):
    """
    Return True, if host should be bypassed.
    
            Checks proxy settings gathered from the environment, if specified,
            or from the MacOSX framework SystemConfiguration.
    
            
    """
    ...

def getproxies():
    ...

def getproxies_registry():
    """
    Return a dictionary of scheme -> proxy server URL mappings.
    
            Win32 uses the registry to store proxies.
    
            
    """
    ...

def proxy_bypass_registry(host):
    ...
