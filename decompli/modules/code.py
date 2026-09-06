# Module: code
# Pseudo-source reconstructed from bytecode (no decompiler)


def InteractiveInterpreter():
    """InteractiveInterpreter"""
    ...

def InteractiveConsole():
    """InteractiveConsole"""
    ...

def interact(banner, readfunc, local, exitmsg):
    """
    Closely emulate the interactive Python interpreter.
    
        This is a backwards compatible interface to the InteractiveConsole
        class.  When readfunc is not specified, it attempts to import the
        readline module to enable GNU readline if it is available.
    
        Arguments (all optional, all default to None):
    
        banner -- passed to InteractiveConsole.interact()
        readfunc -- if not None, replaces InteractiveConsole.raw_input()
        local -- passed to InteractiveInterpreter.__init__()
        exitmsg -- passed to InteractiveConsole.interact()
    
        
    """
    ...
