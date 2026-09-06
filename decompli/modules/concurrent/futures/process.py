# Module: process
# Pseudo-source reconstructed from bytecode (no decompiler)


def _ThreadWakeup():
    """_ThreadWakeup"""
    ...

def _python_exit():
    ...

def _RemoteTraceback():
    """_RemoteTraceback"""
    ...

def _ExceptionWithTraceback():
    """_ExceptionWithTraceback"""
    ...

def _rebuild_exc(exc, tb):
    ...

def _WorkItem():
    """_WorkItem"""
    ...

def _ResultItem():
    """_ResultItem"""
    ...

def _CallItem():
    """_CallItem"""
    ...

def _SafeQueue():
    """_SafeQueue"""
    ...

def _get_chunks(*iterables, chunksize=None):
    """ Iterates over zip()ed iterables in chunks. """
    import zip

def _process_chunk(fn, chunk):
    """
     Processes a chunk of an iterable passed to map.
    
        Runs the function passed to map() on a chunk of the
        iterable passed to map.
    
        This function is run in a separate process.
    
        
    """
    ...

def _sendback_result(result_queue, work_id, result, exception, exit_pid):
    """Safely send back the given result or exception"""
    ...

def _process_worker(call_queue, result_queue, initializer, initargs, max_tasks):
    """
    Evaluates calls from call_queue and places the results in result_queue.
    
        This worker is run in a separate process.
    
        Args:
            call_queue: A ctx.Queue of _CallItems that will be read and
                evaluated by the worker.
            result_queue: A ctx.Queue of _ResultItems that will written
                to by the worker.
            initializer: A callable initializer, or None
            initargs: A tuple of args for the initializer
        
    """
    ...

def _ExecutorManagerThread():
    """_ExecutorManagerThread"""
    ...

def _check_system_limits():
    ...

def _chain_from_iterable_of_lists(iterable):
    """
    
        Specialized implementation of itertools.chain.from_iterable.
        Each item in *iterable* should be a list.  This function is
        careful not to keep references to yielded objects.
        
    """
    ...

def BrokenProcessPool():
    """BrokenProcessPool"""
    ...

def ProcessPoolExecutor():
    """ProcessPoolExecutor"""
    ...
