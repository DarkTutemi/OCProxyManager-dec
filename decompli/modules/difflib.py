# Module: difflib
# Pseudo-source reconstructed from bytecode (no decompiler)


def _calculate_ratio(matches, length):
    ...

def SequenceMatcher():
    """SequenceMatcher"""
    ...

def get_close_matches(word, possibilities, n, cutoff):
    """
    Use SequenceMatcher to return list of the best "good enough" matches.
    
        word is a sequence for which close matches are desired (typically a
        string).
    
        possibilities is a list of sequences against which to match word
        (typically a list of strings).
    
        Optional arg n (default 3) is the maximum number of close matches to
        return.  n must be > 0.
    
        Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
        that don't score at least that similar to word are ignored.
    
        The best (no more than n) matches among the possibilities are returned
        in a list, sorted by similarity score, most similar first.
    
        >>> get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
        ['apple', 'ape']
        >>> import keyword as _keyword
        >>> get_close_matches("wheel", _keyword.kwlist)
        ['while']
        >>> get_close_matches("Apple", _keyword.kwlist)
        []
        >>> get_close_matches("accept", _keyword.kwlist)
        ['except']
        
    """
    ...

def _keep_original_ws(s, tag_s):
    """Replace whitespace with the original whitespace characters in `s`"""
    ...

def Differ():
    """Differ"""
    ...

def IS_LINE_JUNK(line, pat):
    """
    
        Return True for ignorable line: iff `line` is blank or contains a single '#'.
    
        Examples:
    
        >>> IS_LINE_JUNK('\n')
        True
        >>> IS_LINE_JUNK('  #   \n')
        True
        >>> IS_LINE_JUNK('hello\n')
        False
        
    """
    ...

def IS_CHARACTER_JUNK(ch, ws):
    """
    
        Return True for ignorable character: iff `ch` is a space or tab.
    
        Examples:
    
        >>> IS_CHARACTER_JUNK(' ')
        True
        >>> IS_CHARACTER_JUNK('\t')
        True
        >>> IS_CHARACTER_JUNK('\n')
        False
        >>> IS_CHARACTER_JUNK('x')
        False
        
    """
    ...

def _format_range_unified(start, stop):
    """Convert range to the "ed" format"""
    ...

def unified_diff(a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm):
    """
    
        Compare two sequences of lines; generate the delta as a unified diff.
    
        Unified diffs are a compact way of showing line changes and a few
        lines of context.  The number of context lines is set by 'n' which
        defaults to three.
    
        By default, the diff control lines (those with ---, +++, or @@) are
        created with a trailing newline.  This is helpful so that inputs
        created from file.readlines() result in diffs that are suitable for
        file.writelines() since both the inputs and outputs have trailing
        newlines.
    
        For inputs that do not have trailing newlines, set the lineterm
        argument to "" so that the output will be uniformly newline free.
    
        The unidiff format normally has a header for filenames and modification
        times.  Any or all of these may be specified using strings for
        'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
        The modification times are normally expressed in the ISO 8601 format.
    
        Example:
    
        >>> for line in unified_diff('one two three four'.split(),
        ...             'zero one tree four'.split(), 'Original', 'Current',
        ...             '2005-01-26 23:30:50', '2010-04-02 10:20:52',
        ...             lineterm=''):
        ...     print(line)                 # doctest: +NORMALIZE_WHITESPACE
        --- Original        2005-01-26 23:30:50
        +++ Current         2010-04-02 10:20:52
        @@ -1,4 +1,4 @@
        +zero
         one
        -two
        -three
        +tree
         four
        
    """
    ...

def _format_range_context(start, stop):
    """Convert range to the "ed" format"""
    ...

def context_diff(a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm):
    """
    
        Compare two sequences of lines; generate the delta as a context diff.
    
        Context diffs are a compact way of showing line changes and a few
        lines of context.  The number of context lines is set by 'n' which
        defaults to three.
    
        By default, the diff control lines (those with *** or ---) are
        created with a trailing newline.  This is helpful so that inputs
        created from file.readlines() result in diffs that are suitable for
        file.writelines() since both the inputs and outputs have trailing
        newlines.
    
        For inputs that do not have trailing newlines, set the lineterm
        argument to "" so that the output will be uniformly newline free.
    
        The context diff format normally has a header for filenames and
        modification times.  Any or all of these may be specified using
        strings for 'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
        The modification times are normally expressed in the ISO 8601 format.
        If not specified, the strings default to blanks.
    
        Example:
    
        >>> print(''.join(context_diff('one\ntwo\nthree\nfour\n'.splitlines(True),
        ...       'zero\none\ntree\nfour\n'.splitlines(True), 'Original', 'Current')),
        ...       end="")
        *** Original
        --- Current
        ***************
        *** 1,4 ****
          one
        ! two
        ! three
          four
        --- 1,4 ----
        + zero
          one
        ! tree
          four
        
    """
    ...

def _check_types(a, b, *args):
    ...

def diff_bytes(dfunc, a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm):
    """
    
        Compare `a` and `b`, two sequences of lines represented as bytes rather
        than str. This is a wrapper for `dfunc`, which is typically either
        unified_diff() or context_diff(). Inputs are losslessly converted to
        strings so that `dfunc` only has to worry about strings, and encoded
        back to bytes on return. This is necessary to compare files with
        unknown or inconsistent encoding. All other inputs (except `n`) must be
        bytes rather than str.
        
    """
    ...

def ndiff(a, b, linejunk, charjunk):
    """
    
        Compare `a` and `b` (lists of strings); return a `Differ`-style delta.
    
        Optional keyword parameters `linejunk` and `charjunk` are for filter
        functions, or can be None:
    
        - linejunk: A function that should accept a single string argument and
          return true iff the string is junk.  The default is None, and is
          recommended; the underlying SequenceMatcher class has an adaptive
          notion of "noise" lines.
    
        - charjunk: A function that accepts a character (string of length
          1), and returns true iff the character is junk. The default is
          the module-level function IS_CHARACTER_JUNK, which filters out
          whitespace characters (a blank or tab; note: it's a bad idea to
          include newline in this!).
    
        Tools/scripts/ndiff.py is a command-line front-end to this function.
    
        Example:
    
        >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
        ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
        >>> print(''.join(diff), end="")
        - one
        ?  ^
        + ore
        ?  ^
        - two
        - three
        ?  -
        + tree
        + emu
        
    """
    ...

def _mdiff(fromlines, tolines, context, linejunk, charjunk):
    """
    Returns generator yielding marked up from/to side by side differences.
    
        Arguments:
        fromlines -- list of text lines to compared to tolines
        tolines -- list of text lines to be compared to fromlines
        context -- number of context lines to display on each side of difference,
                   if None, all from/to text lines will be generated.
        linejunk -- passed on to ndiff (see ndiff documentation)
        charjunk -- passed on to ndiff (see ndiff documentation)
    
        This function returns an iterator which returns a tuple:
        (from line tuple, to line tuple, boolean flag)
    
        from/to line tuple -- (line num, line text)
            line num -- integer or None (to indicate a context separation)
            line text -- original line text with following markers inserted:
                '\0+' -- marks start of added text
                '\0-' -- marks start of deleted text
                '\0^' -- marks start of changed text
                '\1' -- marks end of added/deleted/changed text
    
        boolean flag -- None indicates context separation, True indicates
            either "from" or "to" line contains a change, otherwise False.
    
        This function/iterator was originally developed to generate side by side
        file difference for making HTML pages (see HtmlDiff class for example
        usage).
    
        Note, this function utilizes the ndiff function to generate the side by
        side difference markup.  Optional ndiff arguments may be passed to this
        function and they in turn will be passed to ndiff.
        
    """
    ...

def HtmlDiff():
    """HtmlDiff"""
    ...

def restore(delta, which):
    """
    
        Generate one of the two sequences that generated a delta.
    
        Given a `delta` produced by `Differ.compare()` or `ndiff()`, extract
        lines originating from file 1 or 2 (parameter `which`), stripping off line
        prefixes.
    
        Examples:
    
        >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
        ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
        >>> diff = list(diff)
        >>> print(''.join(restore(diff, 1)), end="")
        one
        two
        three
        >>> print(''.join(restore(diff, 2)), end="")
        ore
        tree
        emu
        
    """
    ...

def _test():
    ...
