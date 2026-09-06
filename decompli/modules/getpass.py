# Module: getpass
# Pseudo-source reconstructed from bytecode (no decompiler)


def GetPassWarning():
    """GetPassWarning"""
    ...

def unix_getpass(prompt, stream):
    """
    Prompt for a password, with echo turned off.
    
        Args:
          prompt: Written on stream to ask for the input.  Default: 'Password: '
          stream: A writable file object to display the prompt.  Defaults to
                  the tty.  If no tty is available defaults to sys.stderr.
        Returns:
          The seKr3t input.
        Raises:
          EOFError: If our input tty or stdin was closed.
          GetPassWarning: When we were unable to turn echo off on the input.
    
        Always restores terminal settings before returning.
        
    """
    ...

def win_getpass(prompt, stream):
    """Prompt for password with echo off, using Windows getwch()."""
    ...

def fallback_getpass(prompt, stream):
    ...

def _raw_input(prompt, stream, input):
    ...

def getuser():
    """
    Get the username from the environment or password database.
    
        First try various environment variables, then the password
        database.  This works on Windows as long as USERNAME is set.
    
        
    """
    ...
