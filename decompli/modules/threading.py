# Module: threading
# Pseudo-source reconstructed from bytecode (no decompiler)


def setprofile(func):
    """
    Set a profile function for all threads started from the threading module.
    
        The func will be passed to sys.setprofile() for each thread, before its
        run() method is called.
    
        
    """
    ...

def getprofile():
    """Get the profiler function as set by threading.setprofile()."""
    ...

def settrace(func):
    """
    Set a trace function for all threads started from the threading module.
    
        The func will be passed to sys.settrace() for each thread, before its run()
        method is called.
    
        
    """
    ...

def gettrace():
    """Get the trace function as set by threading.settrace()."""
    ...

def RLock(*args, **kwargs):
    """
    Factory function that returns a new reentrant lock.
    
        A reentrant lock must be released by the thread that acquired it. Once a
        thread has acquired a reentrant lock, the same thread may acquire it again
        without blocking; the thread must release it once for each time it has
        acquired it.
    
        
    """
    ...

def _RLock():
    """_RLock"""
    ...

def Condition():
    """Condition"""
    ...

def Semaphore():
    """Semaphore"""
    ...

def BoundedSemaphore():
    """BoundedSemaphore"""
    ...

def Event():
    """Event"""
    ...

def Barrier():
    """Barrier"""
    ...

def BrokenBarrierError():
    """BrokenBarrierError"""
    ...

def _newname(name_template):
    ...

def _maintain_shutdown_locks():
    """
    
        Drop any shutdown locks that don't correspond to running threads anymore.
    
        Calling this from time to time avoids an ever-growing _shutdown_locks
        set when Thread objects are not joined explicitly. See bpo-37788.
    
        This must be called with _shutdown_locks_lock acquired.
        
    """
    ...

def Thread():
    """Thread"""
    ...

def ExceptHookArgs(args):
    ...

def excepthook(args):
    """
    
            Handle uncaught Thread.run() exception.
            
    """
    ...

def _make_invoke_excepthook():
    ...

def Timer():
    """Timer"""
    ...

def _MainThread():
    """_MainThread"""
    ...

def _DummyThread():
    """_DummyThread"""
    ...

def current_thread():
    """
    Return the current Thread object, corresponding to the caller's thread of control.
    
        If the caller's thread of control was not created through the threading
        module, a dummy thread object with limited functionality is returned.
    
        
    """
    ...

def currentThread():
    """
    Return the current Thread object, corresponding to the caller's thread of control.
    
        This function is deprecated, use current_thread() instead.
    
        
    """
    ...

def active_count():
    """
    Return the number of Thread objects currently alive.
    
        The returned count is equal to the length of the list returned by
        enumerate().
    
        
    """
    ...

def activeCount():
    """
    Return the number of Thread objects currently alive.
    
        This function is deprecated, use active_count() instead.
    
        
    """
    ...

def _enumerate():
    ...

def enumerate():
    """
    Return a list of all Thread objects currently alive.
    
        The list includes daemonic threads, dummy thread objects created by
        current_thread(), and the main thread. It excludes terminated threads and
        threads that have not yet been started.
    
        
    """
    ...

def _register_atexit(func, *arg, **kwargs):
    """
    CPython internal: register *func* to be called before joining threads.
    
        The registered *func* is called with its arguments just before all
        non-daemon threads are joined in `_shutdown()`. It provides a similar
        purpose to `atexit.register()`, but its functions are called prior to
        threading shutdown instead of interpreter shutdown.
    
        For similarity to atexit, the registered functions are called in reverse.
        
    """
    ...

def _shutdown():
    """
    
        Wait until the Python thread state of all non-daemon threads get deleted.
        
    """
    ...

def main_thread():
    """
    Return the main thread object.
    
        In normal conditions, the main thread is the thread from which the
        Python interpreter was started.
        
    """
    ...

def _after_fork():
    """
    
        Cleanup threading module state that should not exist after a fork.
        
    """
    ...
