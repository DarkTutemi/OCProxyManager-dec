# Module: hashlib
# Pseudo-source reconstructed from bytecode (no decompiler)


def __get_builtin_constructor(name):
    ...

def __get_openssl_constructor(name):
    ...

def __py_new(name, data, **kwargs):
    """
    new(name, data=b'', **kwargs) - Return a new hashing object using the
        named algorithm; optionally initialized with data (which must be
        a bytes-like object).
        
    """
    ...

def __hash_new(name, data, **kwargs):
    """
    new(name, data=b'') - Return a new hashing object using the named algorithm;
        optionally initialized with data (which must be a bytes-like object).
        
    """
    ...

def pbkdf2_hmac(hash_name, password, salt, iterations, dklen):
    """
    Password based key derivation function 2 (PKCS #5 v2.0)
    
            This Python implementations based on the hmac module about as fast
            as OpenSSL's PKCS5_PBKDF2_HMAC for short passwords and much faster
            for long passwords.
            
    """
    ...

def file_digest(fileobj, digest, *, _bufsize=None):
    """
    Hash the contents of a file-like object. Returns a digest object.
    
        *fileobj* must be a file-like object opened for reading in binary mode.
        It accepts file objects from open(), io.BytesIO(), and SocketIO objects.
        The function may bypass Python's I/O and use the file descriptor *fileno*
        directly.
    
        *digest* must either be a hash algorithm name as a *str*, a hash
        constructor, or a callable that returns a hash object.
        
    """
    ...
