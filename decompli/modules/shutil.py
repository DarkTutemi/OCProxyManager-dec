# Module: shutil
# Pseudo-source reconstructed from bytecode (no decompiler)


def Error():
    """Error"""
    ...

def SameFileError():
    """SameFileError"""
    ...

def SpecialFileError():
    """SpecialFileError"""
    ...

def ExecError():
    """ExecError"""
    ...

def ReadError():
    """ReadError"""
    ...

def RegistryError():
    """RegistryError"""
    ...

def _GiveupOnFastCopy():
    """_GiveupOnFastCopy"""
    ...

def _fastcopy_fcopyfile(fsrc, fdst, flags):
    """
    Copy a regular file content or metadata by using high-performance
        fcopyfile(3) syscall (macOS).
        
    """
    ...

def _fastcopy_sendfile(fsrc, fdst):
    """
    Copy data from one regular mmap-like fd to another by using
        high-performance sendfile(2) syscall.
        This should work on Linux >= 2.6.33 only.
        
    """
    ...

def _copyfileobj_readinto(fsrc, fdst, length):
    """
    readinto()/memoryview() based variant of copyfileobj().
        *fsrc* must support readinto() method and both files must be
        open in binary mode.
        
    """
    ...

def copyfileobj(fsrc, fdst, length):
    """copy data from file-like object fsrc to file-like object fdst"""
    ...

def _samefile(src, dst):
    ...

def _stat(fn):
    ...

def _islink(fn):
    ...

def copyfile(src, dst, *, follow_symlinks=None):
    """
    Copy data from src to dst in the most efficient way possible.
    
        If follow_symlinks is not set and src is a symbolic link, a new
        symlink will be created instead of copying the file it points to.
    
        
    """
    ...

def copymode(src, dst, *, follow_symlinks=None):
    """
    Copy mode bits from src to dst.
    
        If follow_symlinks is not set, symlinks aren't followed if and only
        if both `src` and `dst` are symlinks.  If `lchmod` isn't available
        (e.g. Linux) this method does nothing.
    
        
    """
    ...

def _copyxattr(src, dst, *, follow_symlinks=None):
    """
    Copy extended filesystem attributes from `src` to `dst`.
    
            Overwrite existing attributes.
    
            If `follow_symlinks` is false, symlinks won't be followed.
    
            
    """
    ...

def copystat(src, dst, *, follow_symlinks=None):
    """
    Copy file metadata
    
        Copy the permission bits, last access time, last modification time, and
        flags from `src` to `dst`. On Linux, copystat() also copies the "extended
        attributes" where possible. The file contents, owner, and group are
        unaffected. `src` and `dst` are path-like objects or path names given as
        strings.
    
        If the optional flag `follow_symlinks` is not set, symlinks aren't
        followed if and only if both `src` and `dst` are symlinks.
        
    """
    ...

def copy(src, dst, *, follow_symlinks=None):
    """
    Copy data and mode bits ("cp src dst"). Return the file's destination.
    
        The destination may be a directory.
    
        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".
    
        If source and destination are the same file, a SameFileError will be
        raised.
    
        
    """
    ...

def copy2(src, dst, *, follow_symlinks=None):
    """
    Copy data and metadata. Return the file's destination.
    
        Metadata is copied with copystat(). Please see the copystat function
        for more information.
    
        The destination may be a directory.
    
        If follow_symlinks is false, symlinks won't be followed. This
        resembles GNU's "cp -P src dst".
        
    """
    ...

def ignore_patterns(*patterns):
    """
    Function that can be used as copytree() ignore parameter.
    
        Patterns is a sequence of glob-style patterns
        that are used to exclude files
    """
    ...

def _copytree(entries, src, dst, symlinks, ignore, copy_function, ignore_dangling_symlinks, dirs_exist_ok):
    ...

def copytree(src, dst, symlinks, ignore, copy_function, ignore_dangling_symlinks, dirs_exist_ok):
    """
    Recursively copy a directory tree and return the destination directory.
    
        If exception(s) occur, an Error is raised with a list of reasons.
    
        If the optional symlinks flag is true, symbolic links in the
        source tree result in symbolic links in the destination tree; if
        it is false, the contents of the files pointed to by symbolic
        links are copied. If the file pointed by the symlink doesn't
        exist, an exception will be added in the list of errors raised in
        an Error exception at the end of the copy process.
    
        You can set the optional ignore_dangling_symlinks flag to true if you
        want to silence this exception. Notice that this has no effect on
        platforms that don't support os.symlink.
    
        The optional ignore argument is a callable. If given, it
        is called with the `src` parameter, which is the directory
        being visited by copytree(), and `names` which is the list of
        `src` contents, as returned by os.listdir():
    
            callable(src, names) -> ignored_names
    
        Since copytree() is called recursively, the callable will be
        called once for each directory that is copied. It returns a
        list of names relative to the `src` directory that should
        not be copied.
    
        The optional copy_function argument is a callable that will be used
        to copy each file. It will be called with the source path and the
        destination path as arguments. By default, copy2() is used, but any
        function that supports the same signature (like copy()) can be used.
    
        If dirs_exist_ok is false (the default) and `dst` already exists, a
        `FileExistsError` is raised. If `dirs_exist_ok` is true, the copying
        operation will continue if it encounters existing directories, and files
        within the `dst` tree will be overwritten by corresponding files from the
        `src` tree.
        
    """
    ...

def _rmtree_isdir(entry):
    ...

def _rmtree_islink(path):
    ...

def _rmtree_unsafe(path, onerror):
    ...

def _rmtree_safe_fd(topfd, path, onerror):
    ...

def rmtree(path, ignore_errors, onerror, *, dir_fd=None):
    """
    Recursively delete a directory tree.
    
        If dir_fd is not None, it should be a file descriptor open to a directory;
        path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
        If it is unavailable, using it will raise a NotImplementedError.
    
        If ignore_errors is set, errors are ignored; otherwise, if onerror
        is set, it is called to handle the error with arguments (func,
        path, exc_info) where func is platform and implementation dependent;
        path is the argument to that function that caused it to fail; and
        exc_info is a tuple returned by sys.exc_info().  If ignore_errors
        is false and onerror is None, an exception is raised.
    
        
    """
    ...

def _basename(path):
    """
    A basename() variant which first strips the trailing slash, if present.
        Thus we always get the last component of the path, even for directories.
    
        path: Union[PathLike, str]
    
        e.g.
        >>> os.path.basename('/bar/foo')
        'foo'
        >>> os.path.basename('/bar/foo/')
        ''
        >>> _basename('/bar/foo/')
        'foo'
        
    """
    ...

def move(src, dst, copy_function):
    """
    Recursively move a file or directory to another location. This is
        similar to the Unix "mv" command. Return the file or directory's
        destination.
    
        If dst is an existing directory or a symlink to a directory, then src is
        moved inside that directory. The destination path in that directory must
        not already exist.
    
        If dst already exists but is not a directory, it may be overwritten
        depending on os.rename() semantics.
    
        If the destination is on our current filesystem, then rename() is used.
        Otherwise, src is copied to the destination and then removed. Symlinks are
        recreated under the new name if os.rename() fails because of cross
        filesystem renames.
    
        The optional `copy_function` argument is a callable that will be used
        to copy the source or it will be delegated to `copytree`.
        By default, copy2() is used, but any function that supports the same
        signature (like copy()) can be used.
    
        A lot more could be done here...  A look at a mv.c shows a lot of
        the issues this implementation glosses over.
    
        
    """
    ...

def _destinsrc(src, dst):
    ...

def _is_immutable(src):
    ...

def _get_gid(name):
    """Returns a gid, given a group name."""
    ...

def _get_uid(name):
    """Returns an uid, given a user name."""
    ...

def _make_tarball(base_name, base_dir, compress, verbose, dry_run, owner, group, logger, root_dir):
    """
    Create a (possibly compressed) tar file from all the files under
        'base_dir'.
    
        'compress' must be "gzip" (the default), "bzip2", "xz", or None.
    
        'owner' and 'group' can be used to define an owner and a group for the
        archive that is being built. If not provided, the current owner and group
        will be used.
    
        The output tar file will be named 'base_name' +  ".tar", possibly plus
        the appropriate compression extension (".gz", ".bz2", or ".xz").
    
        Returns the output filename.
        
    """
    ...

def _make_zipfile(base_name, base_dir, verbose, dry_run, logger, owner, group, root_dir):
    """
    Create a zip file from all the files under 'base_dir'.
    
        The output zip file will be named 'base_name' + ".zip".  Returns the
        name of the output zip file.
        
    """
    ...

def get_archive_formats():
    """
    Returns a list of supported formats for archiving and unarchiving.
    
        Each element of the returned sequence is a tuple (name, description)
        
    """
    ...

def register_archive_format(name, function, extra_args, description):
    """
    Registers an archive format.
    
        name is the name of the format. function is the callable that will be
        used to create archives. If provided, extra_args is a sequence of
        (name, value) tuples that will be passed as arguments to the callable.
        description can be provided to describe the format, and will be returned
        by the get_archive_formats() function.
        
    """
    ...

def unregister_archive_format(name):
    ...

def make_archive(base_name, format, root_dir, base_dir, verbose, dry_run, owner, group, logger):
    """
    Create an archive file (eg. zip or tar).
    
        'base_name' is the name of the file to create, minus any format-specific
        extension; 'format' is the archive format: one of "zip", "tar", "gztar",
        "bztar", or "xztar".  Or any other registered format.
    
        'root_dir' is a directory that will be the root directory of the
        archive; ie. we typically chdir into 'root_dir' before creating the
        archive.  'base_dir' is the directory where we start archiving from;
        ie. 'base_dir' will be the common prefix of all files and
        directories in the archive.  'root_dir' and 'base_dir' both default
        to the current directory.  Returns the name of the archive file.
    
        'owner' and 'group' are used when creating a tar archive. By default,
        uses the current owner and group.
        
    """
    ...

def get_unpack_formats():
    """
    Returns a list of supported formats for unpacking.
    
        Each element of the returned sequence is a tuple
        (name, extensions, description)
        
    """
    ...

def _check_unpack_options(extensions, function, extra_args):
    """Checks what gets registered as an unpacker."""
    ...

def register_unpack_format(name, extensions, function, extra_args, description):
    """
    Registers an unpack format.
    
        `name` is the name of the format. `extensions` is a list of extensions
        corresponding to the format.
    
        `function` is the callable that will be
        used to unpack archives. The callable will receive archives to unpack.
        If it's unable to handle an archive, it needs to raise a ReadError
        exception.
    
        If provided, `extra_args` is a sequence of
        (name, value) tuples that will be passed as arguments to the callable.
        description can be provided to describe the format, and will be returned
        by the get_unpack_formats() function.
        
    """
    ...

def unregister_unpack_format(name):
    """Removes the pack format from the registry."""
    ...

def _ensure_directory(path):
    """Ensure that the parent directory of `path` exists"""
    ...

def _unpack_zipfile(filename, extract_dir):
    """
    Unpack zip `filename` to `extract_dir`
        
    """
    ...

def _unpack_tarfile(filename, extract_dir, *, filter=None):
    """
    Unpack tar/tar.gz/tar.bz2/tar.xz `filename` to `extract_dir`
        
    """
    ...

def _find_unpack_format(filename):
    ...

def unpack_archive(filename, extract_dir, format, *, filter=None):
    """
    Unpack an archive.
    
        `filename` is the name of the archive.
    
        `extract_dir` is the name of the target directory, where the archive
        is unpacked. If not provided, the current working directory is used.
    
        `format` is the archive format: one of "zip", "tar", "gztar", "bztar",
        or "xztar".  Or any other registered format.  If not provided,
        unpack_archive will use the filename extension and see if an unpacker
        was registered for that extension.
    
        In case none is found, a ValueError is raised.
    
        If `filter` is given, it is passed to the underlying
        extraction function.
        
    """
    ...

def disk_usage(path):
    """
    Return disk usage statistics about the given path.
    
            Returned value is a named tuple with attributes 'total', 'used' and
            'free', which are the amount of total, used and free space, in bytes.
            
    """
    ...

def chown(path, user, group):
    """
    Change owner user and group of the given path.
    
        user and group can be the uid/gid or the user/group names, and in that case,
        they are converted to their respective uid/gid.
        
    """
    ...

def get_terminal_size(fallback):
    """
    Get the size of the terminal window.
    
        For each of the two dimensions, the environment variable, COLUMNS
        and LINES respectively, is checked. If the variable is defined and
        the value is a positive integer, it is used.
    
        When COLUMNS or LINES is not defined, which is the common case,
        the terminal connected to sys.__stdout__ is queried
        by invoking os.get_terminal_size.
    
        If the terminal size cannot be successfully queried, either because
        the system doesn't support querying, or because we are not
        connected to a terminal, the value given in fallback parameter
        is used. Fallback defaults to (80, 24) which is the default
        size used by many terminal emulators.
    
        The value returned is a named tuple of type os.terminal_size.
        
    """
    ...

def _access_check(fn, mode):
    ...

def which(cmd, mode, path):
    """
    Given a command, mode, and a PATH string, return the path which
        conforms to the given mode on the PATH, or None if there is no such
        file.
    
        `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
        of os.environ.get("PATH"), or can be overridden with a custom search
        path.
    
        
    """
    ...
