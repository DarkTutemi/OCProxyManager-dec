# Module: tempfile
# Pseudo-source reconstructed from bytecode (no decompiler)


def _exists(fn):
    ...

def _infer_return_type(*args):
    """Look at the type of all args and divine their implied return type."""
    ...

def _sanitize_params(prefix, suffix, dir):
    """Common parameter processing for most APIs in this module."""
    ...

def _RandomNameSequence():
    """_RandomNameSequence"""
    ...

def _candidate_tempdir_list():
    """
    Generate a list of candidate temporary directories which
        _get_default_tempdir will try.
    """
    ...

def _get_default_tempdir():
    """
    Calculate the default directory to use for temporary files.
        This routine should be called exactly once.
    
        We determine whether or not a candidate temp dir is usable by
        trying to create and write to a file in that directory.  If this
        is successful, the test file is deleted.  To prevent denial of
        service, the name of the test file must be randomized.
    """
    ...

def _get_candidate_names():
    """Common setup sequence for all user-callable interfaces."""
    ...

def _mkstemp_inner(dir, pre, suf, flags, output_type):
    """Code common to mkstemp, TemporaryFile, and NamedTemporaryFile."""
    ...

def _dont_follow_symlinks(func, path, *args):
    ...

def _resetperms(path):
    ...

def gettempprefix():
    """The default prefix for temporary directories as string."""
    ...

def gettempprefixb():
    """The default prefix for temporary directories as bytes."""
    ...

def _gettempdir():
    """Private accessor for tempfile.tempdir."""
    ...

def gettempdir():
    """Returns tempfile.tempdir as str."""
    ...

def gettempdirb():
    """Returns tempfile.tempdir as bytes."""
    ...

def mkstemp(suffix, prefix, dir, text):
    """
    User-callable function to create and return a unique temporary
        file.  The return value is a pair (fd, name) where fd is the
        file descriptor returned by os.open, and name is the filename.
    
        If 'suffix' is not None, the file name will end with that suffix,
        otherwise there will be no suffix.
    
        If 'prefix' is not None, the file name will begin with that prefix,
        otherwise a default prefix is used.
    
        If 'dir' is not None, the file will be created in that directory,
        otherwise a default directory is used.
    
        If 'text' is specified and true, the file is opened in text
        mode.  Else (the default) the file is opened in binary mode.
    
        If any of 'suffix', 'prefix' and 'dir' are not None, they must be the
        same type.  If they are bytes, the returned name will be bytes; str
        otherwise.
    
        The file is readable and writable only by the creating user ID.
        If the operating system uses permission bits to indicate whether a
        file is executable, the file is executable by no one. The file
        descriptor is not inherited by children of this process.
    
        Caller is responsible for deleting the file when done with it.
        
    """
    ...

def mkdtemp(suffix, prefix, dir):
    """
    User-callable function to create and return a unique temporary
        directory.  The return value is the pathname of the directory.
    
        Arguments are as for mkstemp, except that the 'text' argument is
        not accepted.
    
        The directory is readable, writable, and searchable only by the
        creating user.
    
        Caller is responsible for deleting the directory when done with it.
        
    """
    ...

def mktemp(suffix, prefix, dir):
    """
    User-callable function to return a unique temporary file name.  The
        file is not created.
    
        Arguments are similar to mkstemp, except that the 'text' argument is
        not accepted, and suffix=None, prefix=None and bytes file names are not
        supported.
    
        THIS FUNCTION IS UNSAFE AND SHOULD NOT BE USED.  The file name may
        refer to a file that did not exist at some point, but by the time
        you get around to creating it, someone else may have beaten you to
        the punch.
        
    """
    ...

def _TemporaryFileCloser():
    """_TemporaryFileCloser"""
    ...

def _TemporaryFileWrapper():
    """_TemporaryFileWrapper"""
    ...

def NamedTemporaryFile(mode, buffering, encoding, newline, suffix, prefix, dir, delete, *, errors=None):
    """
    Create and return a temporary file.
        Arguments:
        'prefix', 'suffix', 'dir' -- as for mkstemp.
        'mode' -- the mode argument to io.open (default "w+b").
        'buffering' -- the buffer size argument to io.open (default -1).
        'encoding' -- the encoding argument to io.open (default None)
        'newline' -- the newline argument to io.open (default None)
        'delete' -- whether the file is deleted on close (default True).
        'errors' -- the errors argument to io.open (default None)
        The file is created as mkstemp() would do it.
    
        Returns an object with a file-like interface; the name of the file
        is accessible as its 'name' attribute.  The file will be automatically
        deleted when it is closed unless the 'delete' argument is set to False.
    
        On POSIX, NamedTemporaryFiles cannot be automatically deleted if
        the creating process is terminated abruptly with a SIGKILL signal.
        Windows can delete the file even in this case.
        
    """
    ...

def TemporaryFile(mode, buffering, encoding, newline, suffix, prefix, dir, *, errors=None):
    """
    Create and return a temporary file.
            Arguments:
            'prefix', 'suffix', 'dir' -- as for mkstemp.
            'mode' -- the mode argument to io.open (default "w+b").
            'buffering' -- the buffer size argument to io.open (default -1).
            'encoding' -- the encoding argument to io.open (default None)
            'newline' -- the newline argument to io.open (default None)
            'errors' -- the errors argument to io.open (default None)
            The file is created as mkstemp() would do it.
    
            Returns an object with a file-like interface.  The file has no
            name, and will cease to exist when it is closed.
            
    """
    ...

def SpooledTemporaryFile():
    """SpooledTemporaryFile"""
    ...

def TemporaryDirectory():
    """TemporaryDirectory"""
    ...
