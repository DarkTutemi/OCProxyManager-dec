# Module: ast
# Pseudo-source reconstructed from bytecode (no decompiler)


def parse(source, filename, mode, *, type_comments=None, feature_version=None):
    """
    
        Parse the source into an AST node.
        Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
        Pass type_comments=True to get back type comments where the syntax allows.
        
    """
    ...

def literal_eval(node_or_string):
    """
    
        Evaluate an expression node or a string containing only a Python
        expression.  The string or node provided may only consist of the following
        Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
        sets, booleans, and None.
    
        Caution: A complex expression can overflow the C stack and cause a crash.
        
    """
    ...

def dump(node, annotate_fields, include_attributes, *, indent=None):
    """
    
        Return a formatted dump of the tree in node.  This is mainly useful for
        debugging purposes.  If annotate_fields is true (by default),
        the returned string will show the names and the values for fields.
        If annotate_fields is false, the result string will be more compact by
        omitting unambiguous field names.  Attributes such as line
        numbers and column offsets are not dumped by default.  If this is wanted,
        include_attributes can be set to true.  If indent is a non-negative
        integer or string, then the tree will be pretty-printed with that indent
        level. None (the default) selects the single line representation.
        
    """
    ...

def copy_location(new_node, old_node):
    """
    
        Copy source location (`lineno`, `col_offset`, `end_lineno`, and `end_col_offset`
        attributes) from *old_node* to *new_node* if possible, and return *new_node*.
        
    """
    ...

def fix_missing_locations(node):
    """
    
        When you compile a node tree with compile(), the compiler expects lineno and
        col_offset attributes for every node that supports them.  This is rather
        tedious to fill in for generated nodes, so this helper adds these attributes
        recursively where not already set, by setting them to the values of the
        parent node.  It works recursively starting at *node*.
        
    """
    ...

def increment_lineno(node, n):
    """
    
        Increment the line number and end line number of each node in the tree
        starting at *node* by *n*. This is useful to "move code" to a different
        location in a file.
        
    """
    ...

def iter_fields(node):
    """
    
        Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
        that is present on *node*.
        
    """
    ...

def iter_child_nodes(node):
    """
    
        Yield all direct child nodes of *node*, that is, all fields that are nodes
        and all items of fields that are lists of nodes.
        
    """
    ...

def get_docstring(node, clean):
    """
    
        Return the docstring for the given node or None if no docstring can
        be found.  If the node provided does not have docstrings a TypeError
        will be raised.
    
        If *clean* is `True`, all tabs are expanded to spaces and any whitespace
        that can be uniformly removed from the second line onwards is removed.
        
    """
    ...

def _splitlines_no_ff(source):
    """
    Split a string into lines ignoring form feed and other chars.
    
        This mimics how the Python parser splits source code.
        
    """
    ...

def _pad_whitespace(source):
    """Replace all chars except '\f\t' in a line with spaces."""
    ...

def get_source_segment(source, node, *, padded=None):
    """
    Get source code segment of the *source* that generated *node*.
    
        If some location information (`lineno`, `end_lineno`, `col_offset`,
        or `end_col_offset`) is missing, return None.
    
        If *padded* is `True`, the first line of a multi-line statement will
        be padded with spaces to match its original position.
        
    """
    ...

def walk(node):
    """
    
        Recursively yield all descendant nodes in the tree starting at *node*
        (including *node* itself), in no specified order.  This is useful if you
        only want to modify nodes in place and don't care about the context.
        
    """
    ...

def NodeVisitor():
    """NodeVisitor"""
    ...

def NodeTransformer():
    """NodeTransformer"""
    ...

def _getter(self):
    """Deprecated. Use value instead."""
    ...

def _setter(self, value):
    ...

def _ABC():
    """_ABC"""
    ...

def _new(cls, *args, **kwargs):
    ...

def Num():
    """Num"""
    ...

def Str():
    """Str"""
    ...

def Bytes():
    """Bytes"""
    ...

def NameConstant():
    """NameConstant"""
    ...

def Ellipsis():
    """Ellipsis"""
    ...

def slice():
    """slice"""
    ...

def Index():
    """Index"""
    ...

def ExtSlice():
    """ExtSlice"""
    ...

def _dims_getter(self):
    """Deprecated. Use elts instead."""
    ...

def _dims_setter(self, value):
    ...

def Suite():
    """Suite"""
    ...

def AugLoad():
    """AugLoad"""
    ...

def AugStore():
    """AugStore"""
    ...

def Param():
    """Param"""
    ...

def _Precedence():
    """_Precedence"""
    ...

def _Unparser():
    """_Unparser"""
    ...

def unparse(ast_obj):
    ...

def main():
    ...
