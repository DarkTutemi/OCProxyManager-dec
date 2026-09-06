# Module: pydoc
# Pseudo-source reconstructed from bytecode (no decompiler)


def pathdirs():
    """Convert sys.path into a list of absolute, existing, unique paths."""
    ...

def _findclass(func):
    ...

def _finddoc(obj):
    ...

def _getowndoc(obj):
    """
    Get the documentation string for an object if it is not
        inherited from its class.
    """
    ...

def _getdoc(object):
    """
    Get the documentation string for an object.
    
        All tabs are expanded to spaces.  To clean up docstrings that are
        indented to line up with blocks of code, any whitespace than can be
        uniformly removed from the second line onwards is removed.
    """
    ...

def getdoc(object):
    """Get the doc string or comments for an object."""
    ...

def splitdoc(doc):
    """Split a doc string into a synopsis line (if any) and the rest."""
    ...

def classname(object, modname):
    """Get a class name and qualify it with a module name if necessary."""
    ...

def parentname(object, modname):
    """
    Get a name of the enclosing class (qualified it with a module name
        if necessary) or module.
    """
    ...

def isdata(object):
    """Check if an object is of a type that probably means it's data."""
    ...

def replace(text, *pairs):
    """Do a series of global replacements on a string."""
    ...

def cram(text, maxlen):
    """Omit part of a string if needed to make it fit in a maximum length."""
    ...

def stripid(text):
    """Remove the hexadecimal id from a Python object representation."""
    ...

def _is_bound_method(fn):
    """
    
        Returns True if fn is a bound method, regardless of whether
        fn was implemented in Python or in C.
        
    """
    ...

def allmethods(cl):
    ...

def _split_list(s, predicate):
    """
    Split sequence s via predicate, and return pair ([true], [false]).
    
        The return value is a 2-tuple of lists,
            ([x for x in s if predicate(x)],
             [x for x in s if not predicate(x)])
        
    """
    ...

def visiblename(name, all, obj):
    """Decide whether to show documentation on a variable."""
    ...

def classify_class_attrs(object):
    """Wrap inspect.classify_class_attrs, with fixup for data descriptors and bound methods."""
    ...

def sort_attributes(attrs, object):
    """Sort the attrs list in-place by _fields and then alphabetically by name"""
    ...

def ispackage(path):
    """Guess whether a path refers to a package directory."""
    ...

def source_synopsis(file):
    ...

def synopsis(filename, cache):
    """Get the one-line summary out of a module file."""
    ...

def ErrorDuringImport():
    """ErrorDuringImport"""
    ...

def importfile(path):
    """Import a Python source file or compiled file given its path."""
    ...

def safeimport(path, forceload, cache):
    """
    Import a module; handle errors; return None if the module isn't found.
    
        If the module *is* found but an exception occurs, it's wrapped in an
        ErrorDuringImport exception and reraised.  Unlike __import__, if a
        package path is specified, the module at the end of the path is returned,
        not the package at the beginning.  If the optional 'forceload' argument
        is 1, we reload the module from disk (unless it's a dynamic extension).
    """
    ...

def Doc():
    """Doc"""
    ...

def HTMLRepr():
    """HTMLRepr"""
    ...

def HTMLDoc():
    """HTMLDoc"""
    ...

def TextRepr():
    """TextRepr"""
    ...

def TextDoc():
    """TextDoc"""
    ...

def _PlainTextDoc():
    """_PlainTextDoc"""
    ...

def pager(text):
    """The first time this is called, determine what kind of pager to use."""
    ...

def getpager():
    """Decide what method to use for paging through text."""
    ...

def plain(text):
    """Remove boldface formatting from text."""
    ...

def pipepager(text, cmd):
    """Page through text by feeding it to another program."""
    ...

def tempfilepager(text, cmd):
    """Page through text by invoking a program on a temporary file."""
    ...

def _escape_stdout(text):
    ...

def ttypager(text):
    """Page through text on a text terminal."""
    ...

def plainpager(text):
    """Simply print unformatted text.  This is the ultimate fallback."""
    ...

def describe(thing):
    """Produce a short description of the given thing."""
    ...

def locate(path, forceload):
    """Locate an object by name or dotted path, importing as necessary."""
    ...

def resolve(thing, forceload):
    """Given an object or a path to an object, get the object and its name."""
    ...

def render_doc(thing, title, forceload, renderer):
    """Render text documentation, given an object or a path to an object."""
    ...

def doc(thing, title, forceload, output, is_cli):
    """Display text documentation, given an object or a path to an object."""
    ...

def writedoc(thing, forceload):
    """Write HTML documentation to a file in the current directory."""
    ...

def writedocs(dir, pkgpath, done):
    """Write out HTML documentation for all modules in a directory tree."""
    ...

def Helper():
    """Helper"""
    ...

def ModuleScanner():
    """ModuleScanner"""
    ...

def apropos(key):
    """Print all the one-line module summaries that contain a substring."""
    ...

def _start_server(urlhandler, hostname, port):
    """
    Start an HTTP server thread on a specific port.
    
        Start an HTML/text server thread, so HTML or text documents can be
        browsed dynamically and interactively with a web browser.  Example use:
    
            >>> import time
            >>> import pydoc
    
            Define a URL handler.  To determine what the client is asking
            for, check the URL and content_type.
    
            Then get or generate some text or HTML code and return it.
    
            >>> def my_url_handler(url, content_type):
            ...     text = 'the URL sent was: (%s, %s)' % (url, content_type)
            ...     return text
    
            Start server thread on port 0.
            If you use port 0, the server will pick a random port number.
            You can then use serverthread.port to get the port number.
    
            >>> port = 0
            >>> serverthread = pydoc._start_server(my_url_handler, port)
    
            Check that the server is really started.  If it is, open browser
            and get first page.  Use serverthread.url as the starting page.
    
            >>> if serverthread.serving:
            ...    import webbrowser
    
            The next two lines are commented out so a browser doesn't open if
            doctest is run on this module.
    
            #...    webbrowser.open(serverthread.url)
            #True
    
            Let the server do its thing. We just need to monitor its status.
            Use time.sleep so the loop doesn't hog the CPU.
    
            >>> starttime = time.monotonic()
            >>> timeout = 1                    #seconds
    
            This is a short timeout for testing purposes.
    
            >>> while serverthread.serving:
            ...     time.sleep(.01)
            ...     if serverthread.serving and time.monotonic() - starttime > timeout:
            ...          serverthread.stop()
            ...          break
    
            Print any errors that may have occurred.
    
            >>> print(serverthread.error)
            None
       
    """
    ...

def _url_handler(url, content_type):
    """
    The pydoc url handler for use with the pydoc server.
    
        If the content_type is 'text/css', the _pydoc.css style
        sheet is read and returned if it exits.
    
        If the content_type is 'text/html', then the result of
        get_html_page(url) is returned.
        
    """
    ...

def browse(port, *, open_browser=None, hostname=None):
    """
    Start the enhanced pydoc web server and open a web browser.
    
        Use port '0' to start the server on an arbitrary port.
        Set open_browser to False to suppress opening a browser.
        
    """
    ...

def ispath(x):
    ...

def _get_revised_path(given_path, argv0):
    """
    Ensures current directory is on returned path, and argv0 directory is not
    
        Exception: argv0 dir is left alone if it's also pydoc's directory.
    
        Returns a new path entry list, or None if no adjustment is needed.
        
    """
    ...

def _adjust_cli_sys_path():
    """
    Ensures current directory is on sys.path, and __main__ directory is not.
    
        Exception: __main__ dir is left alone if it's also pydoc's directory.
        
    """
    ...

def cli():
    """Command-line interface (looks at sys.argv to decide what to do)."""
    ...
