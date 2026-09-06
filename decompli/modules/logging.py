# Module: logging
# Pseudo-source reconstructed from bytecode (no decompiler)


def getLevelNamesMapping():
    ...

def getLevelName(level):
    """
    
        Return the textual or numeric representation of logging level 'level'.
    
        If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
        INFO, DEBUG) then you get the corresponding string. If you have
        associated levels with names using addLevelName then the name you have
        associated with 'level' is returned.
    
        If a numeric value corresponding to one of the defined levels is passed
        in, the corresponding string representation is returned.
    
        If a string representation of the level is passed in, the corresponding
        numeric value is returned.
    
        If no matching numeric or string value is passed in, the string
        'Level %s' % level is returned.
        
    """
    ...

def addLevelName(level, levelName):
    """
    
        Associate 'levelName' with 'level'.
    
        This is used when converting levels to text during message formatting.
        
    """
    ...

def currentframe():
    """Return the frame object for the caller's stack frame."""
    ...

def _is_internal_frame(frame):
    """Signal whether the frame is a CPython or logging module internal."""
    ...

def _checkLevel(level):
    ...

def _acquireLock():
    """
    
        Acquire the module-level lock for serializing access to shared data.
    
        This should be released with _releaseLock().
        
    """
    ...

def _releaseLock():
    """
    
        Release the module-level lock acquired by calling _acquireLock().
        
    """
    ...

def _register_at_fork_reinit_lock(instance):
    ...

def _after_at_fork_child_reinit_locks():
    ...

def LogRecord():
    """LogRecord"""
    ...

def setLogRecordFactory(factory):
    """
    
        Set the factory to be used when instantiating a log record.
    
        :param factory: A callable which will be called to instantiate
        a log record.
        
    """
    ...

def getLogRecordFactory():
    """
    
        Return the factory to be used when instantiating a log record.
        
    """
    ...

def makeLogRecord(dict):
    """
    
        Make a LogRecord whose attributes are defined by the specified dictionary,
        This function is useful for converting a logging event received over
        a socket connection (which is sent as a dictionary) into a LogRecord
        instance.
        
    """
    ...

def PercentStyle():
    """PercentStyle"""
    ...

def StrFormatStyle():
    """StrFormatStyle"""
    ...

def StringTemplateStyle():
    """StringTemplateStyle"""
    ...

def Formatter():
    """Formatter"""
    ...

def BufferingFormatter():
    """BufferingFormatter"""
    ...

def Filter():
    """Filter"""
    ...

def Filterer():
    """Filterer"""
    ...

def _removeHandlerRef(wr):
    """
    
        Remove a handler reference from the internal cleanup list.
        
    """
    ...

def _addHandlerRef(handler):
    """
    
        Add a handler to the internal cleanup list using a weak reference.
        
    """
    ...

def Handler():
    """Handler"""
    ...

def StreamHandler():
    """StreamHandler"""
    ...

def FileHandler():
    """FileHandler"""
    ...

def _StderrHandler():
    """_StderrHandler"""
    ...

def PlaceHolder():
    """PlaceHolder"""
    ...

def setLoggerClass(klass):
    """
    
        Set the class to be used when instantiating a logger. The class should
        define __init__() such that only a name argument is required, and the
        __init__() should call Logger.__init__()
        
    """
    ...

def getLoggerClass():
    """
    
        Return the class to be used when instantiating a logger.
        
    """
    ...

def Manager():
    """Manager"""
    ...

def Logger():
    """Logger"""
    ...

def RootLogger():
    """RootLogger"""
    ...

def LoggerAdapter():
    """LoggerAdapter"""
    ...

def basicConfig(**kwargs):
    """
    
        Do basic configuration for the logging system.
    
        This function does nothing if the root logger already has handlers
        configured, unless the keyword argument *force* is set to ``True``.
        It is a convenience method intended for use by simple scripts
        to do one-shot configuration of the logging package.
    
        The default behaviour is to create a StreamHandler which writes to
        sys.stderr, set a formatter using the BASIC_FORMAT format string, and
        add the handler to the root logger.
    
        A number of optional keyword arguments may be specified, which can alter
        the default behaviour.
    
        filename  Specifies that a FileHandler be created, using the specified
                  filename, rather than a StreamHandler.
        filemode  Specifies the mode to open the file, if filename is specified
                  (if filemode is unspecified, it defaults to 'a').
        format    Use the specified format string for the handler.
        datefmt   Use the specified date/time format.
        style     If a format string is specified, use this to specify the
                  type of format string (possible values '%', '{', '$', for
                  %-formatting, :meth:`str.format` and :class:`string.Template`
                  - defaults to '%').
        level     Set the root logger level to the specified level.
        stream    Use the specified stream to initialize the StreamHandler. Note
                  that this argument is incompatible with 'filename' - if both
                  are present, 'stream' is ignored.
        handlers  If specified, this should be an iterable of already created
                  handlers, which will be added to the root logger. Any handler
                  in the list which does not have a formatter assigned will be
                  assigned the formatter created in this function.
        force     If this keyword  is specified as true, any existing handlers
                  attached to the root logger are removed and closed, before
                  carrying out the configuration as specified by the other
                  arguments.
        encoding  If specified together with a filename, this encoding is passed to
                  the created FileHandler, causing it to be used when the file is
                  opened.
        errors    If specified together with a filename, this value is passed to the
                  created FileHandler, causing it to be used when the file is
                  opened in text mode. If not specified, the default value is
                  `backslashreplace`.
    
        Note that you could specify a stream created using open(filename, mode)
        rather than passing the filename and mode in. However, it should be
        remembered that StreamHandler does not close its stream (since it may be
        using sys.stdout or sys.stderr), whereas FileHandler closes its stream
        when the handler is closed.
    
        .. versionchanged:: 3.2
           Added the ``style`` parameter.
    
        .. versionchanged:: 3.3
           Added the ``handlers`` parameter. A ``ValueError`` is now thrown for
           incompatible arguments (e.g. ``handlers`` specified together with
           ``filename``/``filemode``, or ``filename``/``filemode`` specified
           together with ``stream``, or ``handlers`` specified together with
           ``stream``.
    
        .. versionchanged:: 3.8
           Added the ``force`` parameter.
    
        .. versionchanged:: 3.9
           Added the ``encoding`` and ``errors`` parameters.
        
    """
    ...

def getLogger(name):
    """
    
        Return a logger with the specified name, creating it if necessary.
    
        If no name is specified, return the root logger.
        
    """
    ...

def critical(msg, *args, **kwargs):
    """
    
        Log a message with severity 'CRITICAL' on the root logger. If the logger
        has no handlers, call basicConfig() to add a console handler with a
        pre-defined format.
        
    """
    ...

def fatal(msg, *args, **kwargs):
    """
    
        Don't use this function, use critical() instead.
        
    """
    ...

def error(msg, *args, **kwargs):
    """
    
        Log a message with severity 'ERROR' on the root logger. If the logger has
        no handlers, call basicConfig() to add a console handler with a pre-defined
        format.
        
    """
    ...

def exception(msg, *args, exc_info=None, **kwargs):
    """
    
        Log a message with severity 'ERROR' on the root logger, with exception
        information. If the logger has no handlers, basicConfig() is called to add
        a console handler with a pre-defined format.
        
    """
    ...

def warning(msg, *args, **kwargs):
    """
    
        Log a message with severity 'WARNING' on the root logger. If the logger has
        no handlers, call basicConfig() to add a console handler with a pre-defined
        format.
        
    """
    ...

def warn(msg, *args, **kwargs):
    ...

def info(msg, *args, **kwargs):
    """
    
        Log a message with severity 'INFO' on the root logger. If the logger has
        no handlers, call basicConfig() to add a console handler with a pre-defined
        format.
        
    """
    ...

def debug(msg, *args, **kwargs):
    """
    
        Log a message with severity 'DEBUG' on the root logger. If the logger has
        no handlers, call basicConfig() to add a console handler with a pre-defined
        format.
        
    """
    ...

def log(level, msg, *args, **kwargs):
    """
    
        Log 'msg % args' with the integer severity 'level' on the root logger. If
        the logger has no handlers, call basicConfig() to add a console handler
        with a pre-defined format.
        
    """
    ...

def disable(level):
    """
    
        Disable all logging calls of severity 'level' and below.
        
    """
    ...

def shutdown(handlerList):
    """
    
        Perform any cleanup actions in the logging system (e.g. flushing
        buffers).
    
        Should be called at application exit.
        
    """
    ...

def NullHandler():
    """NullHandler"""
    ...

def _showwarning(message, category, filename, lineno, file, line):
    """
    
        Implementation of showwarnings which redirects to logging, which will first
        check to see if the file parameter is None. If a file is specified, it will
        delegate to the original warnings implementation of showwarning. Otherwise,
        it will call warnings.formatwarning and will log the resulting string to a
        warnings logger named "py.warnings" with level logging.WARNING.
        
    """
    ...

def captureWarnings(capture):
    """
    
        If capture is true, redirect all warnings to the logging package.
        If capture is False, ensure that warnings are not redirected to logging
        but to their original destinations.
        
    """
    ...
