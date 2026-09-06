# Module: connection
# Pseudo-source reconstructed from bytecode (no decompiler)


def _init_timeout(timeout):
    ...

def _check_timeout(t):
    ...

def arbitrary_address(family):
    """
    
        Return an arbitrary free address for the given family
        
    """
    ...

def _validate_family(family):
    """
    
        Checks if the family is valid for the current environment.
        
    """
    ...

def address_type(address):
    """
    
        Return the types of the address
    
        This can be 'AF_INET', 'AF_UNIX', or 'AF_PIPE'
        
    """
    ...

def _ConnectionBase():
    """_ConnectionBase"""
    ...

def PipeConnection():
    """PipeConnection"""
    ...

def Connection():
    """Connection"""
    ...

def Listener():
    """Listener"""
    ...

def Client(address, family, authkey):
    """
    
        Returns a connection to the address of a `Listener`
        
    """
    ...

def Pipe(duplex):
    """
    
            Returns pair of connection objects at either end of a pipe
            
    """
    ...

def SocketListener():
    """SocketListener"""
    ...

def SocketClient(address):
    """
    
        Return a connection object connected to the socket given by `address`
        
    """
    ...

def PipeListener():
    """PipeListener"""
    ...

def PipeClient(address):
    """
    
            Return a connection object connected to the pipe given by `address`
            
    """
    ...

def deliver_challenge(connection, authkey):
    ...

def answer_challenge(connection, authkey):
    ...

def ConnectionWrapper():
    """ConnectionWrapper"""
    ...

def _xml_dumps(obj):
    ...

def _xml_loads(s):
    ...

def XmlListener():
    """XmlListener"""
    ...

def XmlClient(*args, **kwds):
    ...

def _exhaustive_wait(handles, timeout):
    ...

def wait(object_list, timeout):
    """
    
            Wait till an object in object_list is ready/readable.
    
            Returns list of those objects in object_list which are ready/readable.
            
    """
    ...

def reduce_connection(conn):
    ...

def rebuild_connection(ds, readable, writable):
    ...

def reduce_pipe_connection(conn):
    ...

def rebuild_pipe_connection(dh, readable, writable):
    ...
