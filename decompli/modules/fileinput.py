# Module: fileinput
# Pseudo-source reconstructed from bytecode (no decompiler)


def input(files, inplace, backup, *, mode=None, openhook=None, encoding=None, errors=None):
    """
    Return an instance of the FileInput class, which can be iterated.
    
        The parameters are passed to the constructor of the FileInput class.
        The returned instance, in addition to being an iterator,
        keeps global state for the functions of this module,.
        
    """
    ...

def close():
    """Close the sequence."""
    ...

def nextfile():
    """
    
        Close the current file so that the next iteration will read the first
        line from the next file (if any); lines not read from the file will
        not count towards the cumulative line count. The filename is not
        changed until after the first line of the next file has been read.
        Before the first line has been read, this function has no effect;
        it cannot be used to skip the first file. After the last line of the
        last file has been read, this function has no effect.
        
    """
    ...

def filename():
    """
    
        Return the name of the file currently being read.
        Before the first line has been read, returns None.
        
    """
    ...

def lineno():
    """
    
        Return the cumulative line number of the line that has just been read.
        Before the first line has been read, returns 0. After the last line
        of the last file has been read, returns the line number of that line.
        
    """
    ...

def filelineno():
    """
    
        Return the line number in the current file. Before the first line
        has been read, returns 0. After the last line of the last file has
        been read, returns the line number of that line within the file.
        
    """
    ...

def fileno():
    """
    
        Return the file number of the current file. When no file is currently
        opened, returns -1.
        
    """
    ...

def isfirstline():
    """
    
        Returns true the line just read is the first line of its file,
        otherwise returns false.
        
    """
    ...

def isstdin():
    """
    
        Returns true if the last line was read from sys.stdin,
        otherwise returns false.
        
    """
    ...

def FileInput():
    """FileInput"""
    ...

def hook_compressed(filename, mode, *, encoding=None, errors=None):
    ...

def hook_encoded(encoding, errors):
    ...

def _test():
    ...
