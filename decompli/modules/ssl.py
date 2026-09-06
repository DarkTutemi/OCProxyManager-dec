# Module: ssl
# Pseudo-source reconstructed from bytecode (no decompiler)


def TLSVersion():
    """TLSVersion"""
    ...

def _TLSContentType():
    """_TLSContentType"""
    ...

def _TLSAlertType():
    """_TLSAlertType"""
    ...

def _TLSMessageType():
    """_TLSMessageType"""
    ...

def _dnsname_match(dn, hostname):
    """
    Matching according to RFC 6125, section 6.4.3
    
        - Hostnames are compared lower-case.
        - For IDNA, both dn and hostname must be encoded as IDN A-label (ACE).
        - Partial wildcards like 'www*.example.org', multiple wildcards, sole
          wildcard or wildcards in labels other then the left-most label are not
          supported and a CertificateError is raised.
        - A wildcard must match at least one character.
        
    """
    ...

def _inet_paton(ipname):
    """
    Try to convert an IP address to packed binary form
    
        Supports IPv4 addresses on all platforms and IPv6 on platforms with IPv6
        support.
        
    """
    ...

def _ipaddress_match(cert_ipaddress, host_ip):
    """
    Exact matching of IP addresses.
    
        RFC 6125 explicitly doesn't define an algorithm for this
        (section 1.7.2 - "Out of Scope").
        
    """
    ...

def match_hostname(cert, hostname):
    """
    Verify that *cert* (in decoded format as returned by
        SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 and RFC 6125
        rules are followed.
    
        The function matches IP addresses rather than dNSNames if hostname is a
        valid ipaddress string. IPv4 addresses are supported on all platforms.
        IPv6 addresses are supported on platforms with IPv6 support (AF_INET6
        and inet_pton).
    
        CertificateError is raised on failure. On success, the function
        returns nothing.
        
    """
    ...

def get_default_verify_paths():
    """
    Return paths to default cafile and capath.
        
    """
    ...

def _ASN1Object():
    """_ASN1Object"""
    ...

def Purpose():
    """Purpose"""
    ...

def SSLContext():
    """SSLContext"""
    ...

def create_default_context(purpose, *, cafile=None, capath=None, cadata=None):
    """
    Create a SSLContext object with default settings.
    
        NOTE: The protocol and settings may change anytime without prior
              deprecation. The values represent a fair balance between maximum
              compatibility and security.
        
    """
    ...

def _create_unverified_context(protocol, *, cert_reqs=None, check_hostname=None, purpose=None, certfile=None, keyfile=None, cafile=None, capath=None, cadata=None):
    """
    Create a SSLContext object for Python stdlib modules
    
        All Python stdlib modules shall use this function to create SSLContext
        objects in order to keep common settings in one place. The configuration
        is less restrict than create_default_context()'s to increase backward
        compatibility.
        
    """
    ...

def SSLObject():
    """SSLObject"""
    ...

def _sslcopydoc(func):
    """Copy docstring from SSLObject to SSLSocket"""
    ...

def SSLSocket():
    """SSLSocket"""
    ...

def wrap_socket(sock, keyfile, certfile, server_side, cert_reqs, ssl_version, ca_certs, do_handshake_on_connect, suppress_ragged_eofs, ciphers):
    ...

def cert_time_to_seconds(cert_time):
    """
    Return the time in seconds since the Epoch, given the timestring
        representing the "notBefore" or "notAfter" date from a certificate
        in ``"%b %d %H:%M:%S %Y %Z"`` strptime format (C locale).
    
        "notBefore" or "notAfter" dates must use UTC (RFC 5280).
    
        Month is one of: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
        UTC should be specified as GMT (see ASN1_TIME_print())
        
    """
    ...

def DER_cert_to_PEM_cert(der_cert_bytes):
    """
    Takes a certificate in binary DER format and returns the
        PEM version of it as a string.
    """
    ...

def PEM_cert_to_DER_cert(pem_cert_string):
    """
    Takes a certificate in ASCII PEM format and returns the
        DER-encoded version of it as a byte sequence
    """
    ...

def get_server_certificate(addr, ssl_version, ca_certs, timeout):
    """
    Retrieve the certificate from the server at the specified address,
        and return it as a PEM-encoded string.
        If 'ca_certs' is specified, validate the server cert against it.
        If 'ssl_version' is specified, use it in the connection attempt.
        If 'timeout' is specified, use it in the connection attempt.
        
    """
    ...

def get_protocol_name(protocol_code):
    ...
