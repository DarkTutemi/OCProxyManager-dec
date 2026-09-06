# Module: dis
# Pseudo-source reconstructed from bytecode (no decompiler)


def _try_compile(source, name):
    """
    Attempts to compile the given source, first as an expression and
           then as a statement if the first approach fails.
    
           Utility function to accept strings in functions that otherwise
           expect code objects
        
    """
    ...

def dis(x, *, file=None, depth=None, show_caches=None, adaptive=None):
    """
    Disassemble classes, methods, functions, and other compiled objects.
    
        With no argument, disassemble the last traceback.
    
        Compiled objects currently include generator objects, async generator
        objects, and coroutine objects, all of which store their code object
        in a special attribute.
        
    """
    ...

def distb(tb, *, file=None, show_caches=None, adaptive=None):
    """Disassemble a traceback (default: last traceback)."""
    ...

def pretty_flags(flags):
    """Return pretty representation of code flags."""
    ...

def _Unknown():
    """_Unknown"""
    ...

def _get_code_object(x):
    """Helper to handle methods, compiled or raw code objects, and strings."""
    ...

def _deoptop(op):
    ...

def _get_code_array(co, adaptive):
    ...

def code_info(x):
    """Formatted details of methods, functions, or code."""
    ...

def _format_code_info(co):
    ...

def show_code(co, *, file=None):
    """
    Print details of methods, functions, or code to *file*.
    
        If *file* is not provided, the output is printed on stdout.
        
    """
    ...

def Instruction():
    """Instruction"""
    ...

def get_instructions(x, *, first_line=None, show_caches=None, adaptive=None):
    """
    Iterator for the opcodes in methods, functions or code
    
        Generates a series of Instruction named tuples giving the details of
        each operations in the supplied code.
    
        If *first_line* is not None, it indicates the line number that should
        be reported for the first source line in the disassembled code.
        Otherwise, the source line information (if any) is taken directly from
        the disassembled code object.
        
    """
    ...

def _get_const_value(op, arg, co_consts):
    """
    Helper to get the value of the const in a hasconst op.
    
           Returns the dereferenced constant if this is possible.
           Otherwise (if it is a LOAD_CONST and co_consts is not
           provided) returns the dis.UNKNOWN sentinel.
        
    """
    ...

def _get_const_info(op, arg, co_consts):
    """
    Helper to get optional details about const references
    
           Returns the dereferenced constant and its repr if the value
           can be calculated.
           Otherwise returns the sentinel value dis.UNKNOWN for the value
           and an empty string for its repr.
        
    """
    ...

def _get_name_info(name_index, get_name, **extrainfo):
    """
    Helper to get optional details about named references
    
           Returns the dereferenced name as both value and repr if the name
           list is defined.
           Otherwise returns the sentinel value dis.UNKNOWN for the value
           and an empty string for its repr.
        
    """
    ...

def _parse_varint(iterator):
    ...

def _parse_exception_table(code):
    ...

def _is_backward_jump(op):
    ...

def _get_instructions_bytes(code, varname_from_oparg, names, co_consts, linestarts, line_offset, exception_entries, co_positions, show_caches):
    """
    Iterate over the instructions in a bytecode string.
    
        Generates a sequence of Instruction namedtuples giving the details of each
        opcode.  Additional information about the code's runtime environment
        (e.g. variable names, co_consts) can be specified using optional
        arguments.
    
        
    """
    ...

def disassemble(co, lasti, *, file=None, show_caches=None, adaptive=None):
    """Disassemble a code object."""
    ...

def _disassemble_recursive(co, *, file=None, depth=None, show_caches=None, adaptive=None):
    ...

def _disassemble_bytes(code, lasti, varname_from_oparg, names, co_consts, linestarts, *, file=None, line_offset=None, exception_entries=None, co_positions=None, show_caches=None):
    ...

def _disassemble_str(source, **kwargs):
    """Compile the source string, then disassemble the code object."""
    ...

def _unpack_opargs(code):
    ...

def findlabels(code):
    """
    Detect all offsets in a byte code which are jump targets.
    
        Return the list of offsets.
    
        
    """
    ...

def findlinestarts(code):
    """
    Find the offsets in a byte code which are start of lines in the source.
    
        Generate pairs (offset, lineno)
        
    """
    ...

def _find_imports(co):
    """
    Find import statements in the code
    
        Generate triplets (name, level, fromlist) where
        name is the imported module and level, fromlist are
        the corresponding args to __import__.
        
    """
    ...

def _find_store_names(co):
    """
    Find names of variables which are written in the code
    
        Generate sequence of strings
        
    """
    ...

def Bytecode():
    """Bytecode"""
    ...

def main():
    ...
