# Module: _wrap
# Pseudo-source reconstructed from bytecode (no decompiler)


def words(text):
    """
    Yields each word from the text as a tuple
        containing (start_index, end_index, word). A "word" in this context may
        include the actual word and any whitespace to the right.
        
    """
    import re_word

def divide_line(text, width, fold):
    """
    Given a string of text, and a width (measured in cells), return a list
        of cell offsets which the string should be split at in order for it to fit
        within the given width.
    
        Args:
            text: The text to examine.
            width: The available cell width.
            fold: If True, words longer than `width` will be folded onto a new line.
    
        Returns:
            A list of indices to break the line at.
        
    """
    ...
