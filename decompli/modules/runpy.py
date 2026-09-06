# Module: runpy
# Pseudo-source reconstructed from bytecode (no decompiler)


def _TempModule():
    """_TempModule"""
    ...

def _ModifiedArgv0():
    """_ModifiedArgv0"""
    ...

def _run_code(code, run_globals, init_globals, mod_name, mod_spec, pkg_name, script_name):
    """Helper to run code in nominated namespace"""
    ...

def _run_module_code(code, init_globals, mod_name, mod_spec, pkg_name, script_name):
    """Helper to run code in new namespace with sys modified"""
    ...

def _get_module_details(mod_name, error):
    ...

def _Error():
    """_Error"""
    ...

def _run_module_as_main(mod_name, alter_argv):
    """
    Runs the designated module in the __main__ namespace
    
           Note that the executed module will have full access to the
           __main__ namespace. If this is not desirable, the run_module()
           function should be used to run the module code in a fresh namespace.
    
           At the very least, these variables in __main__ will be overwritten:
               __name__
               __file__
               __cached__
               __loader__
               __package__
        
    """
    ...

def run_module(mod_name, init_globals, run_name, alter_sys):
    """
    Execute a module's code without importing it.
    
           mod_name -- an absolute module name or package name.
    
           Optional arguments:
           init_globals -- dictionary used to pre-populate the module’s
           globals dictionary before the code is executed.
    
           run_name -- if not None, this will be used for setting __name__;
           otherwise, __name__ will be set to mod_name + '__main__' if the
           named module is a package and to just mod_name otherwise.
    
           alter_sys -- if True, sys.argv[0] is updated with the value of
           __file__ and sys.modules[__name__] is updated with a temporary
           module object for the module being executed. Both are
           restored to their original values before the function returns.
    
           Returns the resulting module globals dictionary.
        
    """
    ...

def _get_main_module_details(error):
    ...

def _get_code_from_file(run_name, fname):
    ...

def run_path(path_name, init_globals, run_name):
    """
    Execute code located at the specified filesystem location.
    
           path_name -- filesystem location of a Python script, zipfile,
           or directory containing a top level __main__.py script.
    
           Optional arguments:
           init_globals -- dictionary used to pre-populate the module’s
           globals dictionary before the code is executed.
    
           run_name -- if not None, this will be used to set __name__;
           otherwise, '<run_path>' will be used for __name__.
    
           Returns the resulting module globals dictionary.
        
    """
    ...
