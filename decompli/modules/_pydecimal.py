# Module: _pydecimal
# Pseudo-source reconstructed from bytecode (no decompiler)


def DecimalException():
    """DecimalException"""
    ...

def Clamped():
    """Clamped"""
    ...

def InvalidOperation():
    """InvalidOperation"""
    ...

def ConversionSyntax():
    """ConversionSyntax"""
    ...

def DivisionByZero():
    """DivisionByZero"""
    ...

def DivisionImpossible():
    """DivisionImpossible"""
    ...

def DivisionUndefined():
    """DivisionUndefined"""
    ...

def Inexact():
    """Inexact"""
    ...

def InvalidContext():
    """InvalidContext"""
    ...

def Rounded():
    """Rounded"""
    ...

def Subnormal():
    """Subnormal"""
    ...

def Overflow():
    """Overflow"""
    ...

def Underflow():
    """Underflow"""
    ...

def FloatOperation():
    """FloatOperation"""
    ...

def getcontext():
    """
    Returns this thread's context.
    
        If this thread does not yet have a context, returns
        a new context and sets this thread's context.
        New contexts are copies of DefaultContext.
        
    """
    ...

def setcontext(context):
    """Set this thread's context to context."""
    ...

def localcontext(ctx, **kwargs):
    """
    Return a context manager for a copy of the supplied context
    
        Uses a copy of the current context if no context is specified
        The returned context manager creates a local decimal context
        in a with statement:
            def sin(x):
                 with localcontext() as ctx:
                     ctx.prec += 2
                     # Rest of sin calculation algorithm
                     # uses a precision 2 greater than normal
                 return +s  # Convert result to normal precision
    
             def sin(x):
                 with localcontext(ExtendedContext):
                     # Rest of sin calculation algorithm
                     # uses the Extended Context from the
                     # General Decimal Arithmetic Specification
                 return +s  # Convert result to normal context
    
        >>> setcontext(DefaultContext)
        >>> print(getcontext().prec)
        28
        >>> with localcontext():
        ...     ctx = getcontext()
        ...     ctx.prec += 2
        ...     print(ctx.prec)
        ...
        30
        >>> with localcontext(ExtendedContext):
        ...     print(getcontext().prec)
        ...
        9
        >>> print(getcontext().prec)
        28
        
    """
    ...

def Decimal():
    """Decimal"""
    ...

def _dec_from_triple(sign, coefficient, exponent, special):
    """
    Create a decimal instance directly, without any validation,
        normalization (e.g. removal of leading zeros) or argument
        conversion.
    
        This function is for *internal use only*.
        
    """
    ...

def _ContextManager():
    """_ContextManager"""
    ...

def Context():
    """Context"""
    ...

def _WorkRep():
    """_WorkRep"""
    ...

def _normalize(op1, op2, prec):
    """
    Normalizes op1, op2 to have the same exp and length of coefficient.
    
        Done during addition.
        
    """
    ...

def _decimal_lshift_exact(n, e):
    """
     Given integers n and e, return n * 10**e if it's an integer, else None.
    
        The computation is designed to avoid computing large powers of 10
        unnecessarily.
    
        >>> _decimal_lshift_exact(3, 4)
        30000
        >>> _decimal_lshift_exact(300, -999999999)  # returns None
    
        
    """
    ...

def _sqrt_nearest(n, a):
    """
    Closest integer to the square root of the positive integer n.  a is
        an initial approximation to the square root.  Any positive integer
        will do for a, but the closer a is to the square root of n the
        faster convergence will be.
    
        
    """
    ...

def _rshift_nearest(x, shift):
    """
    Given an integer x and a nonnegative integer shift, return closest
        integer to x / 2**shift; use round-to-even in case of a tie.
    
        
    """
    ...

def _div_nearest(a, b):
    """
    Closest integer to a/b, a and b positive integers; rounds to even
        in the case of a tie.
    
        
    """
    ...

def _ilog(x, M, L):
    """
    Integer approximation to M*log(x/M), with absolute error boundable
        in terms only of x/M.
    
        Given positive integers x and M, return an integer approximation to
        M * log(x/M).  For L = 8 and 0.1 <= x/M <= 10 the difference
        between the approximation and the exact result is at most 22.  For
        L = 8 and 1.0 <= x/M <= 10.0 the difference is at most 15.  In
        both cases these are upper bounds on the error; it will usually be
        much smaller.
    """
    ...

def _dlog10(c, e, p):
    """
    Given integers c, e and p with c > 0, p >= 0, compute an integer
        approximation to 10**p * log10(c*10**e), with an absolute error of
        at most 1.  Assumes that c*10**e is not exactly 1.
    """
    ...

def _dlog(c, e, p):
    """
    Given integers c, e and p with c > 0, compute an integer
        approximation to 10**p * log(c*10**e), with an absolute error of
        at most 1.  Assumes that c*10**e is not exactly 1.
    """
    ...

def _Log10Memoize():
    """_Log10Memoize"""
    ...

def _iexp(x, M, L):
    """
    Given integers x and M, M > 0, such that x/M is small in absolute
        value, compute an integer approximation to M*exp(x/M).  For 0 <=
        x/M <= 2.4, the absolute error in the result is bounded by 60 (and
        is usually much smaller).
    """
    ...

def _dexp(c, e, p):
    """
    Compute an approximation to exp(c*10**e), with p decimal places of
        precision.
    
        Returns integers d, f such that:
    
          10**(p-1) <= d <= 10**p, and
          (d-1)*10**f < exp(c*10**e) < (d+1)*10**f
    
        In other words, d*10**f is an approximation to exp(c*10**e) with p
        digits of precision, and with an error in d of at most 1.  This is
        almost, but not quite, the same as the error being < 1ulp: when d
        = 10**(p-1) the error could be up to 10 ulp.
    """
    ...

def _dpower(xc, xe, yc, ye, p):
    """
    Given integers xc, xe, yc and ye representing Decimals x = xc*10**xe and
        y = yc*10**ye, compute x**y.  Returns a pair of integers (c, e) such that:
    
          10**(p-1) <= c <= 10**p, and
          (c-1)*10**e < x**y < (c+1)*10**e
    
        in other words, c*10**e is an approximation to x**y with p digits
        of precision, and with an error in c of at most 1.  (This is
        almost, but not quite, the same as the error being < 1ulp: when c
        == 10**(p-1) we can only guarantee error < 10ulp.)
    
        We assume that: x is positive and not equal to 1, and y is nonzero.
        
    """
    ...

def _log10_lb(c, correction):
    """Compute a lower bound for 100*log10(c) for a positive integer c."""
    ...

def _convert_other(other, raiseit, allow_float):
    """
    Convert other to Decimal.
    
        Verifies that it's ok to use in an implicit construction.
        If allow_float is true, allow conversion from float;  this
        is used in the comparison methods (__eq__ and friends).
    
        
    """
    ...

def _convert_for_comparison(self, other, equality_op):
    """
    Given a Decimal instance self and a Python object other, return
        a pair (s, o) of Decimal instances such that "s op o" is
        equivalent to "self op other" for any of the 6 comparison
        operators "op".
    
        
    """
    ...

def _parse_format_specifier(format_spec, _localeconv):
    """
    Parse and validate a format specifier.
    
        Turns a standard numeric format specifier into a dict, with the
        following entries:
    
          fill: fill character to pad field to minimum width
          align: alignment type, either '<', '>', '=' or '^'
          sign: either '+', '-' or ' '
          minimumwidth: nonnegative integer giving minimum width
          zeropad: boolean, indicating whether to pad with zeros
          thousands_sep: string to use as thousands separator, or ''
          grouping: grouping for thousands separators, in format
            used by localeconv
          decimal_point: string to use for decimal point
          precision: nonnegative integer giving precision, or None
          type: one of the characters 'eEfFgG%', or None
    
        
    """
    ...

def _format_align(sign, body, spec):
    """
    Given an unpadded, non-aligned numeric string 'body' and sign
        string 'sign', add padding and alignment conforming to the given
        format specifier dictionary 'spec' (as produced by
        parse_format_specifier).
    
        
    """
    ...

def _group_lengths(grouping):
    """
    Convert a localeconv-style grouping into a (possibly infinite)
        iterable of integers representing group lengths.
    
        
    """
    ...

def _insert_thousands_sep(digits, spec, min_width):
    """
    Insert thousands separators into a digit string.
    
        spec is a dictionary whose keys should include 'thousands_sep' and
        'grouping'; typically it's the result of parsing the format
        specifier using _parse_format_specifier.
    
        The min_width keyword argument gives the minimum length of the
        result, which will be padded on the left with zeros if necessary.
    
        If necessary, the zero padding adds an extra '0' on the left to
        avoid a leading thousands separator.  For example, inserting
        commas every three digits in '123456', with min_width=8, gives
        '0,123,456', even though that has length 9.
    
        
    """
    ...

def _format_sign(is_negative, spec):
    """Determine sign character."""
    ...

def _format_number(is_negative, intpart, fracpart, exp, spec):
    """
    Format a number, given the following data:
    
        is_negative: true if the number is negative, else false
        intpart: string of digits that must appear before the decimal point
        fracpart: string of digits that must come after the point
        exp: exponent, as an integer
        spec: dictionary resulting from parsing the format specifier
    
        This function uses the information in spec to:
          insert separators (decimal separator and thousands separators)
          format the sign
          format the exponent
          add trailing '%' for the '%' type
          zero-pad if necessary
          fill and align if necessary
        
    """
    ...
