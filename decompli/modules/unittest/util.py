# Module: util
# Pseudo-source reconstructed from bytecode (no decompiler)


def _shorten(s, prefixlen, suffixlen):
    ...

def _common_shorten_repr(*args):
    ...

def safe_repr(obj, short):
    ...

def strclass(cls):
    ...

def sorted_list_difference(expected, actual):
    """
    Finds elements in only one or the other of two, sorted input lists.
    
        Returns a two-element tuple of lists.    The first list contains those
        elements in the "expected" list but not in the "actual" list, and the
        second contains those elements in the "actual" list but not in the
        "expected" list.    Duplicate elements in either input list are ignored.
        
    """
    ...

def unorderable_list_difference(expected, actual):
    """
    Same behavior as sorted_list_difference but
        for lists of unorderable items (like dicts).
    
        As it does a linear search per item (remove) it
        has O(n*n) performance.
    """
    ...

def three_way_cmp(x, y):
    """Return -1 if x < y, 0 if x == y and 1 if x > y"""
    ...

def _count_diff_all_purpose(actual, expected):
    """Returns list of (cnt_act, cnt_exp, elem) triples where the counts differ"""
    ...

def _count_diff_hashable(actual, expected):
    """Returns list of (cnt_act, cnt_exp, elem) triples where the counts differ"""
    ...
