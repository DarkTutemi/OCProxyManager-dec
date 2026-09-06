# Module: optparse
# Pseudo-source reconstructed from bytecode (no decompiler)


def _repr(self):
    ...

def gettext(message):
    ...

def ngettext(singular, plural, n):
    ...

def OptParseError():
    """OptParseError"""
    ...

def OptionError():
    """OptionError"""
    ...

def OptionConflictError():
    """OptionConflictError"""
    ...

def OptionValueError():
    """OptionValueError"""
    ...

def BadOptionError():
    """BadOptionError"""
    ...

def AmbiguousOptionError():
    """AmbiguousOptionError"""
    ...

def HelpFormatter():
    """HelpFormatter"""
    ...

def IndentedHelpFormatter():
    """IndentedHelpFormatter"""
    ...

def TitledHelpFormatter():
    """TitledHelpFormatter"""
    ...

def _parse_num(val, type):
    ...

def _parse_int(val):
    ...

def check_builtin(option, opt, value):
    ...

def check_choice(option, opt, value):
    ...

def Option():
    """Option"""
    ...

def Values():
    """Values"""
    ...

def OptionContainer():
    """OptionContainer"""
    ...

def OptionGroup():
    """OptionGroup"""
    ...

def OptionParser():
    """OptionParser"""
    ...

def _match_abbrev(s, wordmap):
    """
    _match_abbrev(s : string, wordmap : {string : Option}) -> string
    
        Return the string key in 'wordmap' for which 's' is an unambiguous
        abbreviation.  If 's' is found to be ambiguous or doesn't match any of
        'words', raise BadOptionError.
        
    """
    ...
