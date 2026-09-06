# Module: control
# Pseudo-source reconstructed from bytecode (no decompiler)


def Control():
    """Control"""
    ...

def strip_control_codes(text, _translate_table):
    """
    Remove control codes from text.
    
        Args:
            text (str): A string possibly contain control codes.
    
        Returns:
            str: String with control codes removed.
        
    """
    ...

def escape_control_codes(text, _translate_table):
    """
    Replace control codes with their "escaped" equivalent in the given text.
        (e.g. "" becomes "\b")
    
        Args:
            text (str): A string possibly containing control codes.
    
        Returns:
            str: String with control codes replaced with their escaped version.
        
    """
    ...
