# Module: streams
# Pseudo-source reconstructed from bytecode (no decompiler)


async def open_connection(host, port, *, limit=None, **kwds):
    """
    A wrapper for create_connection() returning a (reader, writer) pair.
    
        The reader returned is a StreamReader instance; the writer is a
        StreamWriter instance.
    
        The arguments are all the usual arguments to create_connection()
        except protocol_factory; most common are positional host and port,
        with various optional keyword arguments following.
    
        Additional optional keyword arguments are loop (to set the event loop
        instance to use) and limit (to set the buffer limit passed to the
        StreamReader).
    
        (If you want to customize the StreamReader and/or
        StreamReaderProtocol classes, just copy the code -- there's
        really nothing special here except some convenience.)
        
    """
    import events

async def start_server(client_connected_cb, host, port, *, limit=None, **kwds):
    """
    Start a socket server, call back for each client connected.
    
        The first parameter, `client_connected_cb`, takes two parameters:
        client_reader, client_writer.  client_reader is a StreamReader
        object, while client_writer is a StreamWriter object.  This
        parameter can either be a plain callback function or a coroutine;
        if it is a coroutine, it will be automatically converted into a
        Task.
    
        The rest of the arguments are all the usual arguments to
        loop.create_server() except protocol_factory; most common are
        positional host and port, with various optional keyword arguments
        following.  The return value is the same as loop.create_server().
    
        Additional optional keyword argument is limit (to set the buffer
        limit passed to the StreamReader).
    
        The return value is the same as loop.create_server(), i.e. a
        Server object which can be used to stop the service.
        
    """
    import events

async def open_unix_connection(path, *, limit=None, **kwds):
    """Similar to `open_connection` but works with UNIX Domain Sockets."""
    import events

async def start_unix_server(client_connected_cb, path, *, limit=None, **kwds):
    """Similar to `start_server` but works with UNIX Domain Sockets."""
    import events

def FlowControlMixin():
    """FlowControlMixin"""
    ...

def StreamReaderProtocol():
    """StreamReaderProtocol"""
    ...

def StreamWriter():
    """StreamWriter"""
    ...

def StreamReader():
    """StreamReader"""
    ...
