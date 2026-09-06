# Module: site
# Pseudo-source reconstructed from bytecode (no decompiler)


def _trace(message):
    ...

def makepath(*paths):
    ...

def abs_paths():
    """Set all module __file__ and __cached__ attributes to an absolute path"""
    ...

def removeduppaths():
    """
     Remove duplicate entries from sys.path along with making them
        absolute
    """
    ...

def _init_pathinfo():
    """Return a set containing all existing file system items from sys.path."""
    ...

def addpackage(sitedir, name, known_paths):
    """
    Process a .pth file within the site-packages directory:
           For each line in the file, either combine it with sitedir to a path
           and add that to known_paths, or execute it if it starts with 'import '.
        
    """
    ...

def addsitedir(sitedir, known_paths):
    """
    Add 'sitedir' argument to sys.path if missing and handle .pth files in
        'sitedir'
    """
    ...

def check_enableusersite():
    """
    Check if user site directory is safe for inclusion
    
        The function tests for the command line flag (including environment var),
        process uid/gid equal to effective uid/gid.
    
        None: Disabled for security reasons
        False: Disabled by user (command line option)
        True: Safe and enabled
        
    """
    ...

def _getuserbase():
    ...

def _get_path(userbase):
    ...

def getuserbase():
    """
    Returns the `user base` directory path.
    
        The `user base` directory can be used to store data. If the global
        variable ``USER_BASE`` is not initialized yet, this function will also set
        it.
        
    """
    ...

def getusersitepackages():
    """
    Returns the user-specific site-packages directory path.
    
        If the global variable ``USER_SITE`` is not initialized yet, this
        function will also set it.
        
    """
    ...

def addusersitepackages(known_paths):
    """
    Add a per user site-package to sys.path
    
        Each user has its own python directory with site-packages in the
        home directory.
        
    """
    ...

def getsitepackages(prefixes):
    """
    Returns a list containing all global site-packages directories.
    
        For each directory present in ``prefixes`` (or the global ``PREFIXES``),
        this function will find its `site-packages` subdirectory depending on the
        system environment, and will return a list of full paths.
        
    """
    ...

def addsitepackages(known_paths, prefixes):
    """Add site-packages to sys.path"""
    ...

def setquit():
    """
    Define new builtins 'quit' and 'exit'.
    
        These are objects which make the interpreter exit when called.
        The repr of each object contains a hint at how it works.
    
        
    """
    ...

def setcopyright():
    """Set 'copyright' and 'credits' in builtins"""
    ...

def sethelper():
    ...

def enablerlcompleter():
    """
    Enable default readline configuration on interactive prompts, by
        registering a sys.__interactivehook__.
    
        If the readline module can be imported, the hook will set the Tab key
        as completion key and register ~/.python_history as history file.
        This can be overridden in the sitecustomize or usercustomize module,
        or in a PYTHONSTARTUP file.
        
    """
    ...

def venv(known_paths):
    ...

def execsitecustomize():
    """Run custom site specific code, if available."""
    ...

def execusercustomize():
    """Run custom user specific code, if available."""
    ...

def main():
    """
    Add standard site-specific directories to the module search path.
    
        This function is called automatically when this module is imported,
        unless the python interpreter was started with the -S flag.
        
    """
    ...

def _script():
    ...
