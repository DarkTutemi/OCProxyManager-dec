# Module: _parser
# Pseudo-source reconstructed from bytecode (no decompiler)


def TOMLDecodeError():
    """TOMLDecodeError"""
    ...

def load(fp, *, parse_float=None):
    """Parse TOML from a binary file object."""
    ...

def loads(s, *, parse_float=None):
    """Parse TOML from a string."""
    ...

def Flags():
    """Flags"""
    ...

def NestedDict():
    """NestedDict"""
    ...

def Output():
    """Output"""
    ...

def skip_chars(src, pos, chars):
    ...

def skip_until(src, pos, expect, *, error_on=None, error_on_eof=None):
    ...

def skip_comment(src, pos):
    ...

def skip_comments_and_array_ws(src, pos):
    ...

def create_dict_rule(src, pos, out):
    ...

def create_list_rule(src, pos, out):
    ...

def key_value_rule(src, pos, out, header, parse_float):
    ...

def parse_key_value_pair(src, pos, parse_float):
    ...

def parse_key(src, pos):
    ...

def parse_key_part(src, pos):
    ...

def parse_one_line_basic_str(src, pos):
    ...

def parse_array(src, pos, parse_float):
    ...

def parse_inline_table(src, pos, parse_float):
    ...

def parse_basic_str_escape(src, pos, *, multiline=None):
    ...

def parse_basic_str_escape_multiline(src, pos):
    ...

def parse_hex_char(src, pos, hex_len):
    ...

def parse_literal_str(src, pos):
    ...

def parse_multiline_str(src, pos, *, literal=None):
    ...

def parse_basic_str(src, pos, *, multiline=None):
    ...

def parse_value(src, pos, parse_float):
    ...

def suffixed_err(src, pos, msg):
    """
    Return a `TOMLDecodeError` where error message is suffixed with
        coordinates in source.
    """
    ...

def is_unicode_scalar_value(codepoint):
    ...

def make_safe_parse_float(parse_float):
    """
    A decorator to make `parse_float` safe.
    
        `parse_float` must not return dicts or lists, because these types
        would be mixed with parsed TOML tables and arrays, thus confusing
        the parser. The returned decorated callable raises `ValueError`
        instead of returning illegal types.
        
    """
    ...
