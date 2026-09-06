# Module: util
# Pseudo-source reconstructed from bytecode (no decompiler)


def sub_debug(msg, *args):
    ...

def debug(msg, *args):
    ...

def info(msg, *args):
    ...

def sub_warning(msg, *args):
    ...

def get_logger():
    """
    
        Returns logger used by multiprocessing
        
    """
    ...

def log_to_stderr(level):
    """
    
        Turn on logging and add a handler which prints to stderr
        
    """
    ...

def _platform_supports_abstract_sockets():
    ...

def is_abstract_socket_namespace(address):
    ...

def _remove_temp_dir(rmtree, tempdir):
    ...

def get_temp_dir():
    ...

def _run_after_forkers():
    ...

def register_after_fork(obj, func):
    ...

def Finalize():
    """Finalize"""
    ...

def _run_finalizers(minpriority):
    """
    
        Run all finalizers whose exit priority is not None and at least minpriority
    
        Finalizers with highest priority are called first; finalizers with
        the same priority will be called in reverse order of creation.
        
    """
    ...

def is_exiting():
    """
    
        Returns true if the process is shutting down
        
    """
    ...

def _exit_function(info, debug, _run_finalizers, active_children, current_process):
    ...

def ForkAwareThreadLock():
    """ForkAwareThreadLock"""
    ...

def ForkAwareLocal():
    """ForkAwareLocal"""
    ...

def close_all_fds_except(fds):
    ...

def _close_stdin():
    ...

def _flush_std_streams():
    ...

def spawnv_passfds(path, args, passfds):
    ...

def close_fds(*fds):
    """Close each file descriptor given as an argument"""
    ...

def _cleanup_tests():
    """
    Cleanup multiprocessing resources when multiprocessing tests
        completed.
    """
    ...
