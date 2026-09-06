# Module: cgi
# Pseudo-source reconstructed from bytecode (no decompiler)


def initlog(*allargs):
    """
    Write a log message, if there is a log file.
    
        Even though this function is called initlog(), you should always
        use log(); log is a variable that is set either to initlog
        (initially), to dolog (once the log file has been opened), or to
        nolog (when logging is disabled).
    
        The first argument is a format string; the remaining arguments (if
        any) are arguments to the % operator, so e.g.
            log("%s: %s", "a", "b")
        will write "a: b" to the log file, followed by a newline.
    
        If the global logfp is not None, it should be a file object to
        which log data is written.
    
        If the global logfp is None, the global logfile may be a string
        giving a filename to open, in append mode.  This file should be
        world writable!!!  If the file can't be opened, logging is
        silently disabled (since there is no safe place where we could
        send an error message).
    
        
    """
    ...

def dolog(fmt, *args):
    """Write a log message to the log file.  See initlog() for docs."""
    ...

def nolog(*allargs):
    """Dummy function, assigned to log when logging is disabled."""
    ...

def closelog():
    """Close the log file."""
    ...

def parse(fp, environ, keep_blank_values, strict_parsing, separator):
    """
    Parse a query in the environment or from a file (default stdin)
    
            Arguments, all optional:
    
            fp              : file pointer; default: sys.stdin.buffer
    
            environ         : environment dictionary; default: os.environ
    
            keep_blank_values: flag indicating whether blank values in
                percent-encoded forms should be treated as blank strings.
                A true value indicates that blanks should be retained as
                blank strings.  The default false value indicates that
                blank values are to be ignored and treated as if they were
                not included.
    
            strict_parsing: flag indicating what to do with parsing errors.
                If false (the default), errors are silently ignored.
                If true, errors raise a ValueError exception.
    
            separator: str. The symbol to use for separating the query arguments.
                Defaults to &.
        
    """
    ...

def parse_multipart(fp, pdict, encoding, errors, separator):
    """
    Parse multipart input.
    
        Arguments:
        fp   : input file
        pdict: dictionary containing other parameters of content-type header
        encoding, errors: request encoding and error handler, passed to
            FieldStorage
    
        Returns a dictionary just like parse_qs(): keys are the field names, each
        value is a list of values for that field. For non-file fields, the value
        is a list of strings.
        
    """
    ...

def _parseparam(s):
    ...

def parse_header(line):
    """
    Parse a Content-type like header.
    
        Return the main content-type and a dictionary of options.
    
        
    """
    ...

def MiniFieldStorage():
    """MiniFieldStorage"""
    ...

def FieldStorage():
    """FieldStorage"""
    ...

def test(environ):
    """
    Robust test CGI script, usable as main program.
    
        Write minimal HTTP headers and dump all information provided to
        the script in HTML form.
    
        
    """
    ...

def print_exception(type, value, tb, limit):
    ...

def print_environ(environ):
    """Dump the shell environment as HTML."""
    ...

def print_form(form):
    """Dump the contents of a form as HTML."""
    ...

def print_directory():
    """Dump the current directory as HTML."""
    ...

def print_arguments():
    ...

def print_environ_usage():
    """Dump a list of environment variables used by CGI as HTML."""
    ...

def valid_boundary(s):
    ...
