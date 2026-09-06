# Module: hmac
# Pseudo-source reconstructed from bytecode (no decompiler)


def HMAC():
    """HMAC"""
    ...

def new(key, msg, digestmod):
    """
    Create a new hashing object and return it.
    
        key: bytes or buffer, The starting key for the hash.
        msg: bytes or buffer, Initial input for the hash, or None.
        digestmod: A hash name suitable for hashlib.new(). *OR*
                   A hashlib constructor returning a new hash object. *OR*
                   A module supporting PEP 247.
    
                   Required as of 3.8, despite its position after the optional
                   msg argument.  Passing it as a keyword argument is
                   recommended, though not required for legacy API reasons.
    
        You can now feed arbitrary bytes into the object using its update()
        method, and can ask for the hash value at any time by calling its digest()
        or hexdigest() methods.
        
    """
    ...

def digest(key, msg, digest):
    """
    Fast inline implementation of HMAC.
    
        key: bytes or buffer, The key for the keyed hash object.
        msg: bytes or buffer, Input message.
        digest: A hash name suitable for hashlib.new() for best performance. *OR*
                A hashlib constructor returning a new hash object. *OR*
                A module supporting PEP 247.
        
    """
    ...
