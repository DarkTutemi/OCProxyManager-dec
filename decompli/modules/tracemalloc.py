# Module: tracemalloc
# Pseudo-source reconstructed from bytecode (no decompiler)


def _format_size(size, sign):
    ...

def Statistic():
    """Statistic"""
    ...

def StatisticDiff():
    """StatisticDiff"""
    ...

def _compare_grouped_stats(old_group, new_group):
    ...

def Frame():
    """Frame"""
    ...

def Traceback():
    """Traceback"""
    ...

def get_object_traceback(obj):
    """
    
        Get the traceback where the Python object *obj* was allocated.
        Return a Traceback instance.
    
        Return None if the tracemalloc module is not tracing memory allocations or
        did not trace the allocation of the object.
        
    """
    ...

def Trace():
    """Trace"""
    ...

def _Traces():
    """_Traces"""
    ...

def _normalize_filename(filename):
    ...

def BaseFilter():
    """BaseFilter"""
    ...

def Filter():
    """Filter"""
    ...

def DomainFilter():
    """DomainFilter"""
    ...

def Snapshot():
    """Snapshot"""
    ...

def take_snapshot():
    """
    
        Take a snapshot of traces of memory blocks allocated by Python.
        
    """
    ...
