# Module: codeop
# Pseudo-source reconstructed from bytecode (no decompiler)


def _maybe_compile(compiler, source, filename, symbol):
    ...

def _is_syntax_error(err1, err2):
    ...

def _compile(source, filename, symbol, incomplete_input):
    ...

def compile_command(source, filename, symbol):
    """
    Compile a command and determine whether it is incomplete.
    
        Arguments:
    
        source -- the source string; may contain \n characters
        filename -- optional filename from which source was read; default
                    "<input>"
        symbol -- optional grammar start symbol; "single" (default), "exec"
                  or "eval"
    
        Return value / exceptions raised:
    
        - Return a code object if the command is complete and valid
        - Return None if the command is incomplete
        - Raise SyntaxError, ValueError or OverflowError if the command is a
          syntax error (OverflowError and ValueError can be produced by
          malformed literals).
        
    """
    ...

def Compile():
    """Compile"""
    ...

def CommandCompiler():
    """CommandCompiler"""
    ...
