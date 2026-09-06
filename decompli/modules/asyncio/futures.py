# Module: futures
# Pseudo-source reconstructed from bytecode (no decompiler)


def Future():
    """Future"""
    ...

def _get_loop(fut):
    ...

def _set_result_unless_cancelled(fut, result):
    """Helper setting the result only if the future was not cancelled."""
    ...

def _convert_future_exc(exc):
    ...

def _set_concurrent_future_state(concurrent, source):
    """Copy state from a future to a concurrent.futures.Future."""
    ...

def _copy_future_state(source, dest):
    """
    Internal helper to copy state from another Future.
    
        The other Future may be a concurrent.futures.Future.
        
    """
    ...

def _chain_future(source, destination):
    """
    Chain two futures so that when one completes, so does the other.
    
        The result (or exception) of source will be copied to destination.
        If destination is cancelled, source gets cancelled too.
        Compatible with both asyncio.Future and concurrent.futures.Future.
        
    """
    ...

def wrap_future(future, *, loop=None):
    """Wrap concurrent.futures.Future object."""
    ...
