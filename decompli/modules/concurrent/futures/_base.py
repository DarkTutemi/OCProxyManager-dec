# Module: _base
# Pseudo-source reconstructed from bytecode (no decompiler)


def Error():
    """Error"""
    ...

def CancelledError():
    """CancelledError"""
    ...

def InvalidStateError():
    """InvalidStateError"""
    ...

def _Waiter():
    """_Waiter"""
    ...

def _AsCompletedWaiter():
    """_AsCompletedWaiter"""
    ...

def _FirstCompletedWaiter():
    """_FirstCompletedWaiter"""
    ...

def _AllCompletedWaiter():
    """_AllCompletedWaiter"""
    ...

def _AcquireFutures():
    """_AcquireFutures"""
    ...

def _create_and_install_waiters(fs, return_when):
    ...

def _yield_finished_futures(fs, waiter, ref_collect):
    """
    
        Iterate on the list *fs*, yielding finished futures one by one in
        reverse order.
        Before yielding a future, *waiter* is removed from its waiters
        and the future is removed from each set in the collection of sets
        *ref_collect*.
    
        The aim of this function is to avoid keeping stale references after
        the future is yielded and before the iterator resumes.
        
    """
    ...

def as_completed(fs, timeout):
    """
    An iterator over the given futures that yields each as it completes.
    
        Args:
            fs: The sequence of Futures (possibly created by different Executors) to
                iterate over.
            timeout: The maximum number of seconds to wait. If None, then there
                is no limit on the wait time.
    
        Returns:
            An iterator that yields the given Futures as they complete (finished or
            cancelled). If any given Futures are duplicated, they will be returned
            once.
    
        Raises:
            TimeoutError: If the entire result iterator could not be generated
                before the given timeout.
        
    """
    ...

def wait(fs, timeout, return_when):
    """
    Wait for the futures in the given sequence to complete.
    
        Args:
            fs: The sequence of Futures (possibly created by different Executors) to
                wait upon.
            timeout: The maximum number of seconds to wait. If None, then there
                is no limit on the wait time.
            return_when: Indicates when this function should return. The options
                are:
    
                FIRST_COMPLETED - Return when any future finishes or is
                                  cancelled.
                FIRST_EXCEPTION - Return when any future finishes by raising an
                                  exception. If no future raises an exception
                                  then it is equivalent to ALL_COMPLETED.
                ALL_COMPLETED -   Return when all futures finish or are cancelled.
    
        Returns:
            A named 2-tuple of sets. The first set, named 'done', contains the
            futures that completed (is finished or cancelled) before the wait
            completed. The second set, named 'not_done', contains uncompleted
            futures. Duplicate futures given to *fs* are removed and will be
            returned only once.
        
    """
    ...

def _result_or_cancel(fut, timeout):
    ...

def Future():
    """Future"""
    ...

def Executor():
    """Executor"""
    ...

def BrokenExecutor():
    """BrokenExecutor"""
    ...
