# Module: events
# Pseudo-source reconstructed from bytecode (no decompiler)


def Handle():
    """Handle"""
    ...

def TimerHandle():
    """TimerHandle"""
    ...

def AbstractServer():
    """AbstractServer"""
    ...

def AbstractEventLoop():
    """AbstractEventLoop"""
    ...

def AbstractEventLoopPolicy():
    """AbstractEventLoopPolicy"""
    ...

def BaseDefaultEventLoopPolicy():
    """BaseDefaultEventLoopPolicy"""
    ...

def _RunningLoop():
    """_RunningLoop"""
    ...

def get_running_loop():
    """
    Return the running event loop.  Raise a RuntimeError if there is none.
    
        This function is thread-specific.
        
    """
    ...

def _get_running_loop():
    """
    Return the running event loop or None.
    
        This is a low-level function intended to be used by event loops.
        This function is thread-specific.
        
    """
    ...

def _set_running_loop(loop):
    """
    Set the running event loop.
    
        This is a low-level function intended to be used by event loops.
        This function is thread-specific.
        
    """
    ...

def _init_event_loop_policy():
    ...

def get_event_loop_policy():
    """Get the current event loop policy."""
    ...

def set_event_loop_policy(policy):
    """
    Set the current event loop policy.
    
        If policy is None, the default policy is restored.
    """
    ...

def get_event_loop():
    """
    Return an asyncio event loop.
    
        When called from a coroutine or a callback (e.g. scheduled with call_soon
        or similar API), this function will always return the running event loop.
    
        If there is no running event loop set, the function will return
        the result of `get_event_loop_policy().get_event_loop()` call.
        
    """
    ...

def _get_event_loop(stacklevel):
    ...

def set_event_loop(loop):
    """Equivalent to calling get_event_loop_policy().set_event_loop(loop)."""
    ...

def new_event_loop():
    """Equivalent to calling get_event_loop_policy().new_event_loop()."""
    ...

def get_child_watcher():
    """Equivalent to calling get_event_loop_policy().get_child_watcher()."""
    ...

def set_child_watcher(watcher):
    """
    Equivalent to calling
        get_event_loop_policy().set_child_watcher(watcher).
    """
    ...
