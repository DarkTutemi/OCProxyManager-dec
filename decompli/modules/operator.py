# Module: operator
# Pseudo-source reconstructed from bytecode (no decompiler)


def lt(a, b):
    """Same as a < b."""
    ...

def le(a, b):
    """Same as a <= b."""
    ...

def eq(a, b):
    """Same as a == b."""
    ...

def ne(a, b):
    """Same as a != b."""
    ...

def ge(a, b):
    """Same as a >= b."""
    ...

def gt(a, b):
    """Same as a > b."""
    ...

def not_(a):
    """Same as not a."""
    ...

def truth(a):
    """Return True if a is true, False otherwise."""
    ...

def is_(a, b):
    """Same as a is b."""
    ...

def is_not(a, b):
    """Same as a is not b."""
    ...

def abs(a):
    """Same as abs(a)."""
    ...

def add(a, b):
    """Same as a + b."""
    ...

def and_(a, b):
    """Same as a & b."""
    ...

def floordiv(a, b):
    """Same as a // b."""
    ...

def index(a):
    """Same as a.__index__()."""
    ...

def inv(a):
    """Same as ~a."""
    ...

def lshift(a, b):
    """Same as a << b."""
    ...

def mod(a, b):
    """Same as a % b."""
    ...

def mul(a, b):
    """Same as a * b."""
    ...

def matmul(a, b):
    """Same as a @ b."""
    ...

def neg(a):
    """Same as -a."""
    ...

def or_(a, b):
    """Same as a | b."""
    ...

def pos(a):
    """Same as +a."""
    ...

def pow(a, b):
    """Same as a ** b."""
    ...

def rshift(a, b):
    """Same as a >> b."""
    ...

def sub(a, b):
    """Same as a - b."""
    ...

def truediv(a, b):
    """Same as a / b."""
    ...

def xor(a, b):
    """Same as a ^ b."""
    ...

def concat(a, b):
    """Same as a + b, for a and b sequences."""
    ...

def contains(a, b):
    """Same as b in a (note reversed operands)."""
    ...

def countOf(a, b):
    """Return the number of items in a which are, or which equal, b."""
    ...

def delitem(a, b):
    """Same as del a[b]."""
    ...

def getitem(a, b):
    """Same as a[b]."""
    ...

def indexOf(a, b):
    """Return the first index of b in a."""
    ...

def setitem(a, b, c):
    """Same as a[b] = c."""
    ...

def length_hint(obj, default):
    """
    
        Return an estimate of the number of items in obj.
        This is useful for presizing containers when building from an iterable.
    
        If the object supports len(), the result will be exact. Otherwise, it may
        over- or under-estimate by an arbitrary amount. The result will be an
        integer >= 0.
        
    """
    ...

def call(obj, *args, **kwargs):
    """Same as obj(*args, **kwargs)."""
    ...

def attrgetter():
    """attrgetter"""
    ...

def itemgetter():
    """itemgetter"""
    ...

def methodcaller():
    """methodcaller"""
    ...

def iadd(a, b):
    """Same as a += b."""
    ...

def iand(a, b):
    """Same as a &= b."""
    ...

def iconcat(a, b):
    """Same as a += b, for a and b sequences."""
    ...

def ifloordiv(a, b):
    """Same as a //= b."""
    ...

def ilshift(a, b):
    """Same as a <<= b."""
    ...

def imod(a, b):
    """Same as a %= b."""
    ...

def imul(a, b):
    """Same as a *= b."""
    ...

def imatmul(a, b):
    """Same as a @= b."""
    ...

def ior(a, b):
    """Same as a |= b."""
    ...

def ipow(a, b):
    """Same as a **= b."""
    ...

def irshift(a, b):
    """Same as a >>= b."""
    ...

def isub(a, b):
    """Same as a -= b."""
    ...

def itruediv(a, b):
    """Same as a /= b."""
    ...

def ixor(a, b):
    """Same as a ^= b."""
    ...
