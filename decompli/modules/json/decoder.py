# Module: decoder
# Pseudo-source reconstructed from bytecode (no decompiler)


def JSONDecodeError():
    """JSONDecodeError"""
    ...

def _decode_uXXXX(s, pos):
    ...

def py_scanstring(s, end, strict, _b, _m):
    """
    Scan the string s for a JSON string. End is the index of the
        character in s after the quote that started the JSON string.
        Unescapes all valid JSON string escape sequences and raises ValueError
        on attempt to decode an invalid string. If strict is False then literal
        control characters are allowed in the string.
    
        Returns a tuple of the decoded string and the index of the character in s
        after the end quote.
    """
    ...

def JSONObject(s_and_end, strict, scan_once, object_hook, object_pairs_hook, memo, _w, _ws):
    ...

def JSONArray(s_and_end, scan_once, _w, _ws):
    ...

def JSONDecoder():
    """JSONDecoder"""
    ...
