# Module: rich
# Pseudo-source reconstructed from bytecode (no decompiler)


def get_console():
    """
    Get a global :class:`~rich.console.Console` instance. This function is used when Rich requires a Console,
        and hasn't been explicitly given one.
    
        Returns:
            Console: A console instance.
        
    """
    ...

def reconfigure(*args, **kwargs):
    """
    Reconfigures the global console by replacing it with another.
    
        Args:
            *args (Any): Positional arguments for the replacement :class:`~rich.console.Console`.
            **kwargs (Any): Keyword arguments for the replacement :class:`~rich.console.Console`.
        
    """
    ...

def print(*objects, sep=None, end=None, file=None, flush=None):
    """
    Print object(s) supplied via positional arguments.
        This function has an identical signature to the built-in print.
        For more advanced features, see the :class:`~rich.console.Console` class.
    
        Args:
            sep (str, optional): Separator between printed objects. Defaults to " ".
            end (str, optional): Character to write at end of output. Defaults to "\\n".
            file (IO[str], optional): File to write to, or None for stdout. Defaults to None.
            flush (bool, optional): Has no effect as Rich always flushes output. Defaults to False.
    
        
    """
    ...

def print_json(json, *, data=None, indent=None, highlight=None, skip_keys=None, ensure_ascii=None, check_circular=None, allow_nan=None, default=None, sort_keys=None):
    """
    Pretty prints JSON. Output will be valid JSON.
    
        Args:
            json (str): A string containing JSON.
            data (Any): If json is not supplied, then encode this data.
            indent (int, optional): Number of spaces to indent. Defaults to 2.
            highlight (bool, optional): Enable highlighting of output: Defaults to True.
            skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
            ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
            check_circular (bool, optional): Check for circular references. Defaults to True.
            allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
            default (Callable, optional): A callable that converts values that can not be encoded
                in to something that can be JSON encoded. Defaults to None.
            sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
        
    """
    ...

def inspect(obj, *, console=None, title=None, help=None, methods=None, docs=None, private=None, dunder=None, sort=None, all=None, value=None):
    """
    Inspect any Python object.
    
        * inspect(<OBJECT>) to see summarized info.
        * inspect(<OBJECT>, methods=True) to see methods.
        * inspect(<OBJECT>, help=True) to see full (non-abbreviated) help.
        * inspect(<OBJECT>, private=True) to see private attributes (single underscore).
        * inspect(<OBJECT>, dunder=True) to see attributes beginning with double underscore.
        * inspect(<OBJECT>, all=True) to see all attributes.
    
        Args:
            obj (Any): An object to inspect.
            title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
            help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
            methods (bool, optional): Enable inspection of callables. Defaults to False.
            docs (bool, optional): Also render doc strings. Defaults to True.
            private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
            dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
            sort (bool, optional):  Sort attributes alphabetically, callables at the top, leading and trailing underscores ignored. Defaults to True.
            all (bool, optional): Show all attributes. Defaults to False.
            value (bool, optional): Pretty print value. Defaults to True.
        
    """
    ...
