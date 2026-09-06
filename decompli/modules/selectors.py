# Module: selectors
# Pseudo-source reconstructed from bytecode (no decompiler)


def _fileobj_to_fd(fileobj):
    """
    Return a file descriptor from a file object.
    
        Parameters:
        fileobj -- file object or file descriptor
    
        Returns:
        corresponding file descriptor
    
        Raises:
        ValueError if the object is invalid
        
    """
    ...

def _SelectorMapping():
    """_SelectorMapping"""
    ...

def BaseSelector():
    """BaseSelector"""
    ...

def _BaseSelectorImpl():
    """_BaseSelectorImpl"""
    ...

def SelectSelector():
    """SelectSelector"""
    ...

def _PollLikeSelector():
    """_PollLikeSelector"""
    ...

def PollSelector():
    """PollSelector"""
    ...

def EpollSelector():
    """EpollSelector"""
    ...

def DevpollSelector():
    """DevpollSelector"""
    ...

def KqueueSelector():
    """KqueueSelector"""
    ...

def _can_use(method):
    """
    Check if we can use the selector depending upon the
        operating system. 
    """
    ...
