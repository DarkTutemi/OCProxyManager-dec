# Module: cells
# Pseudo-source reconstructed from bytecode (no decompiler)


def CellTable():
    """CellTable"""
    ...

def get_character_cell_size(character, unicode_version):
    """
    Get the cell size of a character.
    
        Args:
            character (str): A single character.
            unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.
    
        Returns:
            int: Number of cells (0, 1 or 2) occupied by that character.
        
    """
    ...

def cached_cell_len(text, unicode_version):
    """
    Get the number of cells required to display text.
    
        This method always caches, which may use up a lot of memory. It is recommended to use
        `cell_len` over this method.
    
        Args:
            text (str): Text to display.
            unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.
    
        Returns:
            int: Get the number of cells required to display text.
        
    """
    ...

def cell_len(text, unicode_version):
    """
    Get the cell length of a string (length as it appears in the terminal).
    
        Args:
            text: String to measure.
            unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.
    
        Returns:
            Length of string in terminal cells.
        
    """
    ...

def _cell_len(text, unicode_version):
    """
    Get the cell length of a string (length as it appears in the terminal).
    
        Args:
            text: String to measure.
            unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.
    
        Returns:
            Length of string in terminal cells.
        
    """
    ...

def split_graphemes(text, unicode_version):
    """
    Divide text into spans that define a single grapheme, and additionally return the cell length of the whole string.
    
        The returned spans will cover every index in the string, with no gaps. It is possible for some graphemes to have a cell length of zero.
        This can occur for nonsense strings like two zero width joiners, or for control codes that don't contribute to the grapheme size.
    
        Args:
            text: String to split.
            unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.
    
        Returns:
            A tuple of a list of *spans* and the cell length of the entire string. A span is a list of tuples
                of three values consisting of (<START>, <END>, <CELL LENGTH>), where START and END are string indices,
                and CELL LENGTH is the cell length of the single grapheme.
        
    """
    ...

def _split_text(text, cell_position, unicode_version):
    """
    Split text by cell position.
    
        If the cell position falls within a double width character, it is converted to two spaces.
    
        Args:
            text: Text to split.
            cell_position Offset in cells.
            unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.
    
        Returns:
            Tuple to two split strings.
        
    """
    ...

def split_text(text, cell_position, unicode_version):
    """
    Split text by cell position.
    
        If the cell position falls within a double width character, it is converted to two spaces.
    
        Args:
            text: Text to split.
            cell_position Offset in cells.
            unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.
    
        Returns:
            Tuple to two split strings.
        
    """
    ...

def set_cell_size(text, total, unicode_version):
    """
    Adjust a string by cropping or padding with spaces such that it fits within the given number of cells.
    
        Args:
            text: String to adjust.
            total: Desired size in cells.
            unicode_version: Unicode version.
    
        Returns:
            A string with cell size equal to total.
        
    """
    ...

def chop_cells(text, width, unicode_version):
    """
    Split text into lines such that each line fits within the available (cell) width.
    
        Args:
            text: The text to fold such that it fits in the given width.
            width: The width available (number of cells).
    
        Returns:
            A list of strings such that each string in the list has cell width
            less than or equal to the available width.
        
    """
    ...
