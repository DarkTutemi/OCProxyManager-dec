# Module: signal
# Pseudo-source reconstructed from bytecode (no decompiler)


def _int_to_enum(value, enum_klass):
    """
    Convert a possible numeric value to an IntEnum member.
        If it's not a known member, return the value itself.
        
    """
    ...

def _enum_to_int(value):
    """
    Convert an IntEnum member to a numeric value.
        If it's not an IntEnum member return the value itself.
        
    """
    ...

def _wraps(wrapped):
    ...

def signal(signalnum, handler):
    ...

def getsignal(signalnum):
    ...

def pthread_sigmask(how, mask):
    ...

def sigpending():
    ...

def sigwait(sigset):
    ...

def valid_signals():
    ...
