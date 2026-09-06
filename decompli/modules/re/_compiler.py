# Module: _compiler
# Pseudo-source reconstructed from bytecode (no decompiler)


def _combine_flags(flags, add_flags, del_flags, TYPE_FLAGS):
    ...

def _compile(code, pattern, flags):
    ...

def _compile_charset(charset, flags, code):
    ...

def _optimize_charset(charset, iscased, fixup, fixes):
    ...

def _mk_bitmap(bits, _CODEBITS, _int):
    ...

def _bytes_to_codes(b):
    ...

def _simple(p):
    ...

def _generate_overlap_table(prefix):
    """
    
        Generate an overlap table for the following prefix.
        An overlap table is a table of the same size as the prefix which
        informs about the potential self-overlap for each index in the prefix:
        - if overlap[i] == 0, prefix[i:] can't overlap prefix[0:...]
        - if overlap[i] == k with 0 < k <= i, prefix[i-k+1:i+1] overlaps with
          prefix[0:k]
        
    """
    ...

def _get_iscased(flags):
    ...

def _get_literal_prefix(pattern, flags):
    ...

def _get_charset_prefix(pattern, flags):
    ...

def _compile_info(code, pattern, flags):
    ...

def isstring(obj):
    ...

def _code(p, flags):
    ...

def _hex_code(code):
    ...

def dis(code):
    ...

def compile(p, flags):
    ...
