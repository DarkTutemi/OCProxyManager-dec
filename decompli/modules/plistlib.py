# Module: plistlib
# Pseudo-source reconstructed from bytecode (no decompiler)


def UID():
    """UID"""
    ...

def _encode_base64(s, maxlinelength):
    ...

def _decode_base64(s):
    ...

def _date_from_string(s):
    ...

def _date_to_string(d):
    ...

def _escape(text):
    ...

def _PlistParser():
    """_PlistParser"""
    ...

def _DumbXMLWriter():
    """_DumbXMLWriter"""
    ...

def _PlistWriter():
    """_PlistWriter"""
    ...

def _is_fmt_xml(header):
    ...

def InvalidFileException():
    """InvalidFileException"""
    ...

def _BinaryPlistParser():
    """_BinaryPlistParser"""
    ...

def _count_to_size(count):
    ...

def _BinaryPlistWriter():
    """_BinaryPlistWriter"""
    ...

def _is_fmt_binary(header):
    ...

def load(fp, *, fmt=None, dict_type=None):
    """
    Read a .plist file. 'fp' should be a readable and binary file object.
        Return the unpacked root object (which usually is a dictionary).
        
    """
    ...

def loads(value, *, fmt=None, dict_type=None):
    """
    Read a .plist file from a bytes object.
        Return the unpacked root object (which usually is a dictionary).
        
    """
    ...

def dump(value, fp, *, fmt=None, sort_keys=None, skipkeys=None):
    """
    Write 'value' to a .plist file. 'fp' should be a writable,
        binary file object.
        
    """
    ...

def dumps(value, *, fmt=None, skipkeys=None, sort_keys=None):
    """
    Return a bytes object with the contents for a .plist file.
        
    """
    ...
