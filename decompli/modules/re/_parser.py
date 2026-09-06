# Module: _parser
# Pseudo-source reconstructed from bytecode (no decompiler)


def State():
    """State"""
    ...

def SubPattern():
    """SubPattern"""
    ...

def Tokenizer():
    """Tokenizer"""
    ...

def _class_escape(source, escape):
    ...

def _escape(source, escape, state):
    ...

def _uniq(items):
    ...

def _parse_sub(source, state, verbose, nested):
    ...

def _parse(source, state, verbose, nested, first):
    ...

def _parse_flags(source, state, char):
    ...

def fix_flags(src, flags):
    ...

def parse(str, flags, state):
    ...

def parse_template(source, state):
    ...

def expand_template(template, match):
    ...
