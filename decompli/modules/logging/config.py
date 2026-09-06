# Module: config
# Pseudo-source reconstructed from bytecode (no decompiler)


def fileConfig(fname, defaults, disable_existing_loggers, encoding):
    """
    
        Read the logging configuration from a ConfigParser-format file.
    
        This can be called several times from an application, allowing an end user
        the ability to select from various pre-canned configurations (if the
        developer provides a mechanism to present the choices and load the chosen
        configuration).
        
    """
    ...

def _resolve(name):
    """Resolve a dotted name to a global object."""
    ...

def _strip_spaces(alist):
    ...

def _create_formatters(cp):
    """Create and return formatters"""
    ...

def _install_handlers(cp, formatters):
    """Install and return handlers"""
    ...

def _handle_existing_loggers(existing, child_loggers, disable_existing):
    """
    
        When (re)configuring logging, handle loggers which were in the previous
        configuration but are not in the new configuration. There's no point
        deleting them as other threads may continue to hold references to them;
        and by disabling them, you stop them doing any logging.
    
        However, don't disable children of named loggers, as that's probably not
        what was intended by the user. Also, allow existing loggers to NOT be
        disabled if disable_existing is false.
        
    """
    ...

def _install_loggers(cp, handlers, disable_existing):
    """Create and install loggers"""
    ...

def _clearExistingHandlers():
    """Clear and close existing handlers"""
    ...

def valid_ident(s):
    ...

def ConvertingMixin():
    """ConvertingMixin"""
    ...

def ConvertingDict():
    """ConvertingDict"""
    ...

def ConvertingList():
    """ConvertingList"""
    ...

def ConvertingTuple():
    """ConvertingTuple"""
    ...

def BaseConfigurator():
    """BaseConfigurator"""
    ...

def DictConfigurator():
    """DictConfigurator"""
    ...

def dictConfig(config):
    """Configure logging using a dictionary."""
    ...

def listen(port, verify):
    """
    
        Start up a socket server on the specified port, and listen for new
        configurations.
    
        These will be sent as a file suitable for processing by fileConfig().
        Returns a Thread object on which you can call start() to start the server,
        and which you can join() when appropriate. To stop the server, call
        stopListening().
    
        Use the ``verify`` argument to verify any bytes received across the wire
        from a client. If specified, it should be a callable which receives a
        single argument - the bytes of configuration data received across the
        network - and it should return either ``None``, to indicate that the
        passed in bytes could not be verified and should be discarded, or a
        byte string which is then passed to the configuration machinery as
        normal. Note that you can return transformed bytes, e.g. by decrypting
        the bytes passed in.
        
    """
    ...

def stopListening():
    """
    
        Stop the listening server which was created with a call to listen().
        
    """
    ...
