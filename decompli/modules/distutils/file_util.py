# Module: file_util
# Pseudo-source reconstructed from bytecode (no decompiler)


def _copy_file_contents(src, dst, buffer_size):
    """
    Copy the file 'src' to 'dst'; both must be filenames.  Any error
        opening either file, reading from 'src', or writing to 'dst', raises
        DistutilsFileError.  Data is read/written in chunks of 'buffer_size'
        bytes (default 16k).  No attempt is made to handle anything apart from
        regular files.
        
    """
    ...

def copy_file(src, dst, preserve_mode, preserve_times, update, link, verbose, dry_run):
    """
    Copy a file 'src' to 'dst'.  If 'dst' is a directory, then 'src' is
        copied there with the same name; otherwise, it must be a filename.  (If
        the file exists, it will be ruthlessly clobbered.)  If 'preserve_mode'
        is true (the default), the file's mode (type and permission bits, or
        whatever is analogous on the current platform) is copied.  If
        'preserve_times' is true (the default), the last-modified and
        last-access times are copied as well.  If 'update' is true, 'src' will
        only be copied if 'dst' does not exist, or if 'dst' does exist but is
        older than 'src'.
    
        'link' allows you to make hard links (os.link) or symbolic links
        (os.symlink) instead of copying: set it to "hard" or "sym"; if it is
        None (the default), files are copied.  Don't set 'link' on systems that
        don't support it: 'copy_file()' doesn't check if hard or symbolic
        linking is available. If hardlink fails, falls back to
        _copy_file_contents().
    
        Under Mac OS, uses the native file copy function in macostools; on
        other systems, uses '_copy_file_contents()' to copy file contents.
    
        Return a tuple (dest_name, copied): 'dest_name' is the actual name of
        the output file, and 'copied' is true if the file was copied (or would
        have been copied, if 'dry_run' true).
        
    """
    ...

def move_file(src, dst, verbose, dry_run):
    """
    Move a file 'src' to 'dst'.  If 'dst' is a directory, the file will
        be moved into it with the same name; otherwise, 'src' is just renamed
        to 'dst'.  Return the new full name of the file.
    
        Handles cross-device moves on Unix using 'copy_file()'.  What about
        other systems???
        
    """
    ...

def write_file(filename, contents):
    """
    Create a file with the specified name and write 'contents' (a
        sequence of strings without line terminators) to it.
        
    """
    ...
