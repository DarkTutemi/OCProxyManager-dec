# Module: pickle
# Pseudo-source reconstructed from bytecode (no decompiler)


def PickleError():
    """PickleError"""
    ...

def PicklingError():
    """PicklingError"""
    ...

def UnpicklingError():
    """UnpicklingError"""
    ...

def _Stop():
    """_Stop"""
    ...

def _Framer():
    """_Framer"""
    ...

def _Unframer():
    """_Unframer"""
    ...

def _getattribute(obj, name):
    ...

def whichmodule(obj, name):
    """Find the module an object belong to."""
    ...

def encode_long(x):
    """
    Encode a long to a two's complement little-endian binary string.
        Note that 0 is a special case, returning an empty string, to save a
        byte in the LONG1 pickling context.
    
        >>> encode_long(0)
        b''
        >>> encode_long(255)
        b'\xff\x00'
        >>> encode_long(32767)
        b'\xff\x7f'
        >>> encode_long(-256)
        b'\x00\xff'
        >>> encode_long(-32768)
        b'\x00\x80'
        >>> encode_long(-128)
        b'\x80'
        >>> encode_long(127)
        b'\x7f'
        >>>
        
    """
    ...

def decode_long(data):
    """
    Decode a long from a two's complement little-endian binary string.
    
        >>> decode_long(b'')
        0
        >>> decode_long(b"\xff\x00")
        255
        >>> decode_long(b"\xff\x7f")
        32767
        >>> decode_long(b"\x00\xff")
        -256
        >>> decode_long(b"\x00\x80")
        -32768
        >>> decode_long(b"\x80")
        -128
        >>> decode_long(b"\x7f")
        127
        
    """
    ...

def _Pickler():
    """_Pickler"""
    ...

def _Unpickler():
    """_Unpickler"""
    ...

def _dump(obj, file, protocol, *, fix_imports=None, buffer_callback=None):
    ...

def _dumps(obj, protocol, *, fix_imports=None, buffer_callback=None):
    ...

def _load(file, *, fix_imports=None, encoding=None, errors=None, buffers=None):
    ...

def _loads(s, *, fix_imports=None, encoding=None, errors=None, buffers=None):
    ...

def _test():
    ...
