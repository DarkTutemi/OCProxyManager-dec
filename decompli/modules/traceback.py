# Module: traceback
# Pseudo-source reconstructed from bytecode (no decompiler)


def print_list(extracted_list, file):
    """
    Print the list of tuples as returned by extract_tb() or
        extract_stack() as a formatted stack trace to the given file.
    """
    ...

def format_list(extracted_list):
    """
    Format a list of tuples or FrameSummary objects for printing.
    
        Given a list of tuples or FrameSummary objects as returned by
        extract_tb() or extract_stack(), return a list of strings ready
        for printing.
    
        Each string in the resulting list corresponds to the item with the
        same index in the argument list.  Each string ends in a newline;
        the strings may contain internal newlines as well, for those items
        whose source text line is not None.
        
    """
    ...

def print_tb(tb, limit, file):
    """
    Print up to 'limit' stack trace entries from the traceback 'tb'.
    
        If 'limit' is omitted or None, all entries are printed.  If 'file'
        is omitted or None, the output goes to sys.stderr; otherwise
        'file' should be an open file or file-like object with a write()
        method.
        
    """
    ...

def format_tb(tb, limit):
    """A shorthand for 'format_list(extract_tb(tb, limit))'."""
    ...

def extract_tb(tb, limit):
    """
    
        Return a StackSummary object representing a list of
        pre-processed entries from traceback.
    
        This is useful for alternate formatting of stack traces.  If
        'limit' is omitted or None, all entries are extracted.  A
        pre-processed stack trace entry is a FrameSummary object
        containing attributes filename, lineno, name, and line
        representing the information that is usually printed for a stack
        trace.  The line is a string with leading and trailing
        whitespace stripped; if the source is not available it is None.
        
    """
    ...

def _Sentinel():
    """_Sentinel"""
    ...

def _parse_value_tb(exc, value, tb):
    ...

def print_exception(exc, value, tb, limit, file, chain):
    """
    Print exception up to 'limit' stack trace entries from 'tb' to 'file'.
    
        This differs from print_tb() in the following ways: (1) if
        traceback is not None, it prints a header "Traceback (most recent
        call last):"; (2) it prints the exception type and value after the
        stack trace; (3) if type is SyntaxError and value has the
        appropriate format, it prints the line where the syntax error
        occurred with a caret on the next line indicating the approximate
        position of the error.
        
    """
    ...

def format_exception(exc, value, tb, limit, chain):
    """
    Format a stack trace and the exception information.
    
        The arguments have the same meaning as the corresponding arguments
        to print_exception().  The return value is a list of strings, each
        ending in a newline and some containing internal newlines.  When
        these lines are concatenated and printed, exactly the same text is
        printed as does print_exception().
        
    """
    ...

def format_exception_only(exc, value):
    """
    Format the exception part of a traceback.
    
        The return value is a list of strings, each ending in a newline.
    
        The list contains the exception's message, which is
        normally a single string; however, for :exc:`SyntaxError` exceptions, it
        contains several lines that (when printed) display detailed information
        about where the syntax error occurred. Following the message, the list
        contains the exception's ``__notes__``.
        
    """
    ...

def _format_final_exc_line(etype, value):
    ...

def _safe_string(value, what, func):
    ...

def print_exc(limit, file, chain):
    """Shorthand for 'print_exception(*sys.exc_info(), limit, file)'."""
    ...

def format_exc(limit, chain):
    """Like print_exc() but return a string."""
    ...

def print_last(limit, file, chain):
    """
    This is a shorthand for 'print_exception(sys.last_type,
        sys.last_value, sys.last_traceback, limit, file)'.
    """
    ...

def print_stack(f, limit, file):
    """
    Print a stack trace from its invocation point.
    
        The optional 'f' argument can be used to specify an alternate
        stack frame at which to start. The optional 'limit' and 'file'
        arguments have the same meaning as for print_exception().
        
    """
    ...

def format_stack(f, limit):
    """Shorthand for 'format_list(extract_stack(f, limit))'."""
    ...

def extract_stack(f, limit):
    """
    Extract the raw traceback from the current stack frame.
    
        The return value has the same format as for extract_tb().  The
        optional 'f' and 'limit' arguments have the same meaning as for
        print_stack().  Each item in the list is a quadruple (filename,
        line number, function name, text), and the entries are in order
        from oldest to newest stack frame.
        
    """
    ...

def clear_frames(tb):
    """Clear all references to local variables in the frames of a traceback."""
    ...

def FrameSummary():
    """FrameSummary"""
    ...

def walk_stack(f):
    """
    Walk a stack yielding the frame and line number for each frame.
    
        This will follow f.f_back from the given frame. If no frame is given, the
        current stack is used. Usually used with StackSummary.extract.
        
    """
    import sys

def walk_tb(tb):
    """
    Walk a traceback yielding the frame and line number for each frame.
    
        This will follow tb.tb_next (and thus is in the opposite order to
        walk_stack). Usually used with StackSummary.extract.
        
    """
    import tb_frame

def _walk_tb_with_full_positions(tb):
    ...

def _get_code_position(code, instruction_index):
    ...

def StackSummary():
    """StackSummary"""
    ...

def _byte_offset_to_character_offset(str, offset):
    ...

def _extract_caret_anchors_from_line_segment(segment):
    ...

def _display_width(line, offset):
    """
    Calculate the extra amount of width space the given source
        code segment might take if it were to be displayed on a fixed
        width output device. Supports wide unicode characters and emojis.
    """
    ...

def _ExceptionPrintContext():
    """_ExceptionPrintContext"""
    ...

def TracebackException():
    """TracebackException"""
    ...
