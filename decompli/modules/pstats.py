# Module: pstats
# Pseudo-source reconstructed from bytecode (no decompiler)


def SortKey():
    """SortKey"""
    ...

def FunctionProfile():
    """FunctionProfile"""
    ...

def StatsProfile():
    """StatsProfile"""
    ...

def Stats():
    """Stats"""
    ...

def TupleComp():
    """TupleComp"""
    ...

def func_strip_path(func_name):
    ...

def func_get_function_name(func):
    ...

def func_std_string(func_name):
    ...

def add_func_stats(target, source):
    """Add together all the stats for two profile entries."""
    ...

def add_callers(target, source):
    """Combine two caller lists in a single list."""
    ...

def count_calls(callers):
    """Sum the caller statistics to get total number of calls received."""
    ...

def f8(x):
    ...

def ProfileBrowser():
    """ProfileBrowser"""
    ...
