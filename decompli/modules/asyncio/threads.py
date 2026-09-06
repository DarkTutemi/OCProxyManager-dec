# Module: threads
# Pseudo-source reconstructed from bytecode (no decompiler)


async def to_thread(func, *args, **kwargs):
    """
    Asynchronously run function *func* in a separate thread.
    
        Any *args and **kwargs supplied for this function are directly passed
        to *func*. Also, the current :class:`contextvars.Context` is propagated,
        allowing context variables from the main thread to be accessed in the
        separate thread.
    
        Return a coroutine that can be awaited to get the eventual result of *func*.
        
    """
    ...
