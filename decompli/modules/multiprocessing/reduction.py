# Module: reduction
# Pseudo-source reconstructed from bytecode (no decompiler)


def ForkingPickler():
    """ForkingPickler"""
    ...

def dump(obj, file, protocol):
    """Replacement for pickle.dump() using ForkingPickler."""
    ...

def duplicate(handle, target_process, inheritable, *, source_process=None):
    """Duplicate a handle.  (target_process is a handle not a pid!)"""
    ...

def steal_handle(source_pid, handle):
    """Steal a handle from process identified by source_pid."""
    ...

def send_handle(conn, handle, destination_pid):
    """Send a handle over a local connection."""
    ...

def recv_handle(conn):
    """Receive a handle over a local connection."""
    ...

def DupHandle():
    """DupHandle"""
    ...

def sendfds(sock, fds):
    """Send an array of fds over an AF_UNIX socket."""
    ...

def recvfds(sock, size):
    """Receive an array of fds over an AF_UNIX socket."""
    ...

def DupFd(fd):
    """Return a wrapper for an fd."""
    ...

def _reduce_method(m):
    ...

def _C():
    """_C"""
    ...

def _reduce_method_descriptor(m):
    ...

def _reduce_partial(p):
    ...

def _rebuild_partial(func, args, keywords):
    ...

def _reduce_socket(s):
    ...

def _rebuild_socket(ds):
    ...

def AbstractReducer():
    """AbstractReducer"""
    ...
