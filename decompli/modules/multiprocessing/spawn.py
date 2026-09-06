# Module: spawn
# Pseudo-source reconstructed from bytecode (no decompiler)


def set_executable(exe):
    ...

def get_executable():
    ...

def is_forking(argv):
    """
    
        Return whether commandline indicates we are forking
        
    """
    ...

def freeze_support():
    """
    
        Run code for process object if this in not the main process
        
    """
    ...

def get_command_line(**kwds):
    """
    
        Returns prefix of command line used for spawning a child process
        
    """
    ...

def spawn_main(pipe_handle, parent_pid, tracker_fd):
    """
    
        Run code specified by data received over pipe
        
    """
    ...

def _main(fd, parent_sentinel):
    ...

def _check_not_importing_main():
    ...

def get_preparation_data(name):
    """
    
        Return info about parent needed by child to unpickle process object
        
    """
    ...

def prepare(data):
    """
    
        Try to get current process ready to unpickle process object
        
    """
    ...

def _fixup_main_from_name(mod_name):
    ...

def _fixup_main_from_path(main_path):
    ...

def import_main_path(main_path):
    """
    
        Set sys.modules['__main__'] to module at main_path
        
    """
    ...
