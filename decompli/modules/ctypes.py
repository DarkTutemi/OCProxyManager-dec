# Module: ctypes
# Pseudo-source reconstructed from bytecode (no decompiler)


def create_string_buffer(init, size):
    """
    create_string_buffer(aBytes) -> character array
        create_string_buffer(anInteger) -> character array
        create_string_buffer(aBytes, anInteger) -> character array
        
    """
    ...

def CFUNCTYPE(restype, *argtypes, **kw):
    """
    CFUNCTYPE(restype, *argtypes,
                     use_errno=False, use_last_error=False) -> function prototype.
    
        restype: the result type
        argtypes: a sequence specifying the argument types
    
        The function prototype can be called in different ways to create a
        callable object:
    
        prototype(integer address) -> foreign function
        prototype(callable) -> create and return a C callable function from callable
        prototype(integer index, method name[, paramflags]) -> foreign function calling a COM method
        prototype((ordinal number, dll object)[, paramflags]) -> foreign function exported by ordinal
        prototype((function name, dll object)[, paramflags]) -> foreign function exported by name
        
    """
    ...

def WINFUNCTYPE(restype, *argtypes, **kw):
    ...

def _check_size(typ, typecode):
    ...

def py_object():
    """py_object"""
    ...

def c_short():
    """c_short"""
    ...

def c_ushort():
    """c_ushort"""
    ...

def c_long():
    """c_long"""
    ...

def c_ulong():
    """c_ulong"""
    ...

def c_int():
    """c_int"""
    ...

def c_uint():
    """c_uint"""
    ...

def c_float():
    """c_float"""
    ...

def c_double():
    """c_double"""
    ...

def c_longdouble():
    """c_longdouble"""
    ...

def c_longlong():
    """c_longlong"""
    ...

def c_ulonglong():
    """c_ulonglong"""
    ...

def c_ubyte():
    """c_ubyte"""
    ...

def c_byte():
    """c_byte"""
    ...

def c_char():
    """c_char"""
    ...

def c_char_p():
    """c_char_p"""
    ...

def c_void_p():
    """c_void_p"""
    ...

def c_bool():
    """c_bool"""
    ...

def c_wchar_p():
    """c_wchar_p"""
    ...

def c_wchar():
    """c_wchar"""
    ...

def _reset_cache():
    ...

def create_unicode_buffer(init, size):
    """
    create_unicode_buffer(aString) -> character array
        create_unicode_buffer(anInteger) -> character array
        create_unicode_buffer(aString, anInteger) -> character array
        
    """
    ...

def SetPointerType(pointer, cls):
    ...

def ARRAY(typ, len):
    ...

def CDLL():
    """CDLL"""
    ...

def PyDLL():
    """PyDLL"""
    ...

def WinDLL():
    """WinDLL"""
    ...

def HRESULT():
    """HRESULT"""
    ...

def OleDLL():
    """OleDLL"""
    ...

def LibraryLoader():
    """LibraryLoader"""
    ...

def WinError(code, descr):
    ...

def PYFUNCTYPE(restype, *argtypes):
    ...

def cast(obj, typ):
    ...

def string_at(ptr, size):
    """
    string_at(addr[, size]) -> string
    
        Return the string at addr.
    """
    ...

def wstring_at(ptr, size):
    """
    wstring_at(addr[, size]) -> string
    
            Return the string at addr.
    """
    ...

def DllGetClassObject(rclsid, riid, ppv):
    ...

def DllCanUnloadNow():
    ...
