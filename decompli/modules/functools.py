# Module: functools
# Pseudo-source reconstructed from bytecode (no decompiler)


def update_wrapper(wrapper, wrapped, assigned, updated):
    """
    Update a wrapper function to look like the wrapped function
    
           wrapper is the function to be updated
           wrapped is the original function
           assigned is a tuple naming the attributes assigned directly
           from the wrapped function to the wrapper function (defaults to
           functools.WRAPPER_ASSIGNMENTS)
           updated is a tuple naming the attributes of the wrapper that
           are updated with the corresponding attribute from the wrapped
           function (defaults to functools.WRAPPER_UPDATES)
        
    """
    ...

def wraps(wrapped, assigned, updated):
    """
    Decorator factory to apply update_wrapper() to a wrapper function
    
           Returns a decorator that invokes update_wrapper() with the decorated
           function as the wrapper argument and the arguments to wraps() as the
           remaining arguments. Default arguments are as for update_wrapper().
           This is a convenience function to simplify applying partial() to
           update_wrapper().
        
    """
    ...

def _gt_from_lt(self, other):
    """Return a > b.  Computed by @total_ordering from (not a < b) and (a != b)."""
    ...

def _le_from_lt(self, other):
    """Return a <= b.  Computed by @total_ordering from (a < b) or (a == b)."""
    ...

def _ge_from_lt(self, other):
    """Return a >= b.  Computed by @total_ordering from (not a < b)."""
    ...

def _ge_from_le(self, other):
    """Return a >= b.  Computed by @total_ordering from (not a <= b) or (a == b)."""
    ...

def _lt_from_le(self, other):
    """Return a < b.  Computed by @total_ordering from (a <= b) and (a != b)."""
    ...

def _gt_from_le(self, other):
    """Return a > b.  Computed by @total_ordering from (not a <= b)."""
    ...

def _lt_from_gt(self, other):
    """Return a < b.  Computed by @total_ordering from (not a > b) and (a != b)."""
    ...

def _ge_from_gt(self, other):
    """Return a >= b.  Computed by @total_ordering from (a > b) or (a == b)."""
    ...

def _le_from_gt(self, other):
    """Return a <= b.  Computed by @total_ordering from (not a > b)."""
    ...

def _le_from_ge(self, other):
    """Return a <= b.  Computed by @total_ordering from (not a >= b) or (a == b)."""
    ...

def _gt_from_ge(self, other):
    """Return a > b.  Computed by @total_ordering from (a >= b) and (a != b)."""
    ...

def _lt_from_ge(self, other):
    """Return a < b.  Computed by @total_ordering from (not a >= b)."""
    ...

def total_ordering(cls):
    """Class decorator that fills in missing ordering methods"""
    ...

def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    ...

def reduce(function, sequence, initial):
    """
    
        reduce(function, iterable[, initial]) -> value
    
        Apply a function of two arguments cumulatively to the items of a sequence
        or iterable, from left to right, so as to reduce the iterable to a single
        value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the iterable in the calculation, and serves as a default when the
        iterable is empty.
        
    """
    ...

def partial():
    """partial"""
    ...

def partialmethod():
    """partialmethod"""
    ...

def _unwrap_partial(func):
    ...

def _HashedSeq():
    """_HashedSeq"""
    ...

def _make_key(args, kwds, typed, kwd_mark, fasttypes, tuple, type, len):
    """
    Make a cache key from optionally typed positional and keyword arguments
    
        The key is constructed in a way that is flat as possible rather than
        as a nested structure that would take more memory.
    
        If there is only a single argument and its data type is known to cache
        its hash value, then that argument is returned without a wrapper.  This
        saves space and improves lookup speed.
    
        
    """
    ...

def lru_cache(maxsize, typed):
    """
    Least-recently-used cache decorator.
    
        If *maxsize* is set to None, the LRU features are disabled and the cache
        can grow without bound.
    
        If *typed* is True, arguments of different types will be cached separately.
        For example, f(3.0) and f(3) will be treated as distinct calls with
        distinct results.
    
        Arguments to the cached function must be hashable.
    
        View the cache statistics named tuple (hits, misses, maxsize, currsize)
        with f.cache_info().  Clear the cache and statistics with f.cache_clear().
        Access the underlying function with f.__wrapped__.
    
        See:  https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
    
        
    """
    ...

def _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo):
    ...

def cache(user_function):
    """Simple lightweight unbounded cache.  Sometimes called "memoize"."""
    ...

def _c3_merge(sequences):
    """
    Merges MROs in *sequences* to a single MRO using the C3 algorithm.
    
        Adapted from https://www.python.org/download/releases/2.3/mro/.
    
        
    """
    ...

def _c3_mro(cls, abcs):
    """
    Computes the method resolution order using extended C3 linearization.
    
        If no *abcs* are given, the algorithm works exactly like the built-in C3
        linearization used for method resolution.
    
        If given, *abcs* is a list of abstract base classes that should be inserted
        into the resulting MRO. Unrelated ABCs are ignored and don't end up in the
        result. The algorithm inserts ABCs where their functionality is introduced,
        i.e. issubclass(cls, abc) returns True for the class itself but returns
        False for all its direct base classes. Implicit ABCs for a given class
        (either registered or inferred from the presence of a special method like
        __len__) are inserted directly after the last ABC explicitly listed in the
        MRO of said class. If two implicit ABCs end up next to each other in the
        resulting MRO, their ordering depends on the order of types in *abcs*.
    
        
    """
    ...

def _compose_mro(cls, types):
    """
    Calculates the method resolution order for a given class *cls*.
    
        Includes relevant abstract base classes (with their respective bases) from
        the *types* iterable. Uses a modified C3 linearization algorithm.
    
        
    """
    ...

def _find_impl(cls, registry):
    """
    Returns the best matching implementation from *registry* for type *cls*.
    
        Where there is no registered implementation for a specific type, its method
        resolution order is used to find a more generic implementation.
    
        Note: if *registry* does not contain an implementation for the base
        *object* type, this function may return None.
    
        
    """
    ...

def singledispatch(func):
    """
    Single-dispatch generic function decorator.
    
        Transforms a function into a generic function, which can have different
        behaviours depending upon the type of its first argument. The decorated
        function acts as the default implementation, and additional
        implementations can be registered using the register() attribute of the
        generic function.
        
    """
    ...

def singledispatchmethod():
    """singledispatchmethod"""
    ...

def cached_property():
    """cached_property"""
    ...
