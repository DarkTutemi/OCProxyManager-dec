# Module: syntax
# Pseudo-source reconstructed from bytecode (no decompiler)


def SyntaxTheme():
    """SyntaxTheme"""
    ...

def PygmentsSyntaxTheme():
    """PygmentsSyntaxTheme"""
    ...

def ANSISyntaxTheme():
    """ANSISyntaxTheme"""
    ...

def _SyntaxHighlightRange():
    """_SyntaxHighlightRange"""
    ...

def PaddingProperty():
    """PaddingProperty"""
    ...

def Syntax():
    """Syntax"""
    ...

def _get_code_index_for_syntax_position(newlines_offsets, position):
    """
    
        Returns the index of the code string for the given positions.
    
        Args:
            newlines_offsets (Sequence[int]): The offset of each newline character found in the code snippet.
            position (SyntaxPosition): The position to search for.
    
        Returns:
            Optional[int]: The index of the code string for this position, or `None`
                if the given position's line number is out of range (if it's the column that is out of range
                we silently clamp its value so that it reaches the end of the line)
        
    """
    ...
