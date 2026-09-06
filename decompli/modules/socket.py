# Module: socket
# Pseudo-source reconstructed from bytecode (no decompiler)


def _intenum_converter(value, enum_klass):
    """
    Convert a numeric family value to an IntEnum member.
    
        If it's not a known member, return the numeric value itself.
        
    """
    ...

def _GiveupOnSendfile():
    """_GiveupOnSendfile"""
    ...

def socket():
    """socket"""
    ...

def fromfd(fd, family, type, proto):
    """
     fromfd(fd, family, type[, proto]) -> socket object
    
        Create a socket object from a duplicate of the given file
        descriptor.  The remaining arguments are the same as for socket().
        
    """
    ...

def send_fds(sock, buffers, fds, flags, address):
    """
     send_fds(sock, buffers, fds[, flags[, address]]) -> integer
    
            Send the list of file descriptors fds over an AF_UNIX socket.
            
    """
    ...

def recv_fds(sock, bufsize, maxfds, flags):
    """
     recv_fds(sock, bufsize, maxfds[, flags]) -> (data, list of file
            descriptors, msg_flags, address)
    
            Receive up to maxfds file descriptors returning the message
            data and a list containing the descriptors.
            
    """
    ...

def fromshare(info):
    """
     fromshare(info) -> socket object
    
            Create a socket object from the bytes object returned by
            socket.share(pid).
            
    """
    ...

def socketpair(family, type, proto):
    """
    socketpair([family[, type[, proto]]]) -> (socket object, socket object)
    
            Create a pair of socket objects from the sockets returned by the platform
            socketpair() function.
            The arguments are the same as for socket() except the default family is
            AF_UNIX if defined on the platform; otherwise, the default is AF_INET.
            
    """
    ...

def SocketIO():
    """SocketIO"""
    ...

def getfqdn(name):
    """
    Get fully qualified domain name from name.
    
        An empty argument is interpreted as meaning the local host.
    
        First the hostname returned by gethostbyaddr() is checked, then
        possibly existing aliases. In case no FQDN is available and `name`
        was given, it is returned unchanged. If `name` was empty, '0.0.0.0' or '::',
        hostname from gethostname() is returned.
        
    """
    ...

def create_connection(address, timeout, source_address, *, all_errors=None):
    """
    Connect to *address* and return the socket object.
    
        Convenience function.  Connect to *address* (a 2-tuple ``(host,
        port)``) and return the socket object.  Passing the optional
        *timeout* parameter will set the timeout on the socket instance
        before attempting to connect.  If no *timeout* is supplied, the
        global default timeout setting returned by :func:`getdefaulttimeout`
        is used.  If *source_address* is set it must be a tuple of (host, port)
        for the socket to bind as a source address before making the connection.
        A host of '' or port 0 tells the OS to use the default. When a connection
        cannot be created, raises the last error if *all_errors* is False,
        and an ExceptionGroup of all errors if *all_errors* is True.
        
    """
    ...

def has_dualstack_ipv6():
    """
    Return True if the platform supports creating a SOCK_STREAM socket
        which can handle both AF_INET and AF_INET6 (IPv4 / IPv6) connections.
        
    """
    ...

def create_server(address, *, family=None, backlog=None, reuse_port=None, dualstack_ipv6=None):
    """
    Convenience function which creates a SOCK_STREAM type socket
        bound to *address* (a 2-tuple (host, port)) and return the socket
        object.
    
        *family* should be either AF_INET or AF_INET6.
        *backlog* is the queue size passed to socket.listen().
        *reuse_port* dictates whether to use the SO_REUSEPORT socket option.
        *dualstack_ipv6*: if true and the platform supports it, it will
        create an AF_INET6 socket able to accept both IPv4 or IPv6
        connections. When false it will explicitly disable this option on
        platforms that enable it by default (e.g. Linux).
    
        >>> with create_server(('', 8000)) as server:
        ...     while True:
        ...         conn, addr = server.accept()
        ...         # handle new connection
        
    """
    ...

def getaddrinfo(host, port, family, type, proto, flags):
    """
    Resolve host and port into list of address info entries.
    
        Translate the host/port argument into a sequence of 5-tuples that contain
        all the necessary arguments for creating a socket connected to that service.
        host is a domain name, a string representation of an IPv4/v6 address or
        None. port is a string service name such as 'http', a numeric port number or
        None. By passing None as the value of host and port, you can pass NULL to
        the underlying C API.
    
        The family, type and proto arguments can be optionally specified in order to
        narrow the list of addresses returned. Passing zero as a value for each of
        these arguments selects the full range of results.
        
    """
    ...
