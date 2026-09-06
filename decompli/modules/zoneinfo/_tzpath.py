# Module: _tzpath
# Pseudo-source reconstructed from bytecode (no decompiler)


def reset_tzpath(to):
    ...

def _parse_python_tzpath(env_var):
    ...

def _get_invalid_paths_message(tzpaths):
    ...

def find_tzfile(key):
    """Retrieve the path to a TZif file from a key."""
    ...

def _validate_tzfile_path(path, _base):
    ...

def available_timezones():
    """
    Returns a set containing all available time zones.
    
        .. caution::
    
            This may attempt to open a large number of files, since the best way to
            determine if a given file on the time zone search path is to open it
            and check for the "magic string" at the beginning.
        
    """
    ...

def InvalidTZPathWarning():
    """InvalidTZPathWarning"""
    ...
