# Module: traceback
# Pseudo-source reconstructed from bytecode (no decompiler)


def _iter_syntax_lines(start, end):
    """
    Yield start and end positions per line.
    
        Args:
            start: Start position.
            end: End position.
    
        Returns:
            Iterable of (LINE, COLUMN1, COLUMN2).
        
    """
    ...

def install(*, console=None, width=None, code_width=None, extra_lines=None, theme=None, word_wrap=None, show_locals=None, locals_max_length=None, locals_max_string=None, locals_max_depth=None, locals_hide_dunder=None, locals_hide_sunder=None, locals_overflow=None, indent_guides=None, suppress=None, max_frames=None):
    """
    Install a rich traceback handler.
    
        Once installed, any tracebacks will be printed with syntax highlighting and rich formatting.
    
    
        Args:
            console (Optional[Console], optional): Console to write exception to. Default uses internal Console instance.
            width (Optional[int], optional): Width (in characters) of traceback. Defaults to 100.
            code_width (Optional[int], optional): Code width (in characters) of traceback. Defaults to 88.
            extra_lines (int, optional): Extra lines of code. Defaults to 3.
            theme (Optional[str], optional): Pygments theme to use in traceback. Defaults to ``None`` which will pick
                a theme appropriate for the platform.
            word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
            show_locals (bool, optional): Enable display of local variables. Defaults to False.
            locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to 10.
            locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
            locals_max_depth (int, optional): Maximum depths of locals before truncating, or None to disable. Defaults to None.
            locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
            locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
            locals_overflow (OverflowMethod, optional): How to handle overflowing locals, or None to disable. Defaults to None.
            indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
            suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
    
        Returns:
            Callable: The previous exception handler that was replaced.
    
        
    """
    ...

def Frame():
    """Frame"""
    ...

def _SyntaxError():
    """_SyntaxError"""
    ...

def Stack():
    """Stack"""
    ...

def Trace():
    """Trace"""
    ...

def PathHighlighter():
    """PathHighlighter"""
    ...

def Traceback():
    """Traceback"""
    ...

def bar(a):
    ...

def foo(a):
    ...

def error():
    ...
