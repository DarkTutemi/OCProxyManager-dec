# Module: markup
# Pseudo-source reconstructed from bytecode (no decompiler)


def Tag():
    """Tag"""
    ...

def escape(markup, _escape):
    """
    Escapes text so that it won't be interpreted as markup.
    
        Args:
            markup (str): Content to be inserted in to markup.
    
        Returns:
            str: Markup with square brackets escaped.
        
    """
    ...

def _parse(markup):
    """
    Parse markup in to an iterable of tuples of (position, text, tag).
    
        Args:
            markup (str): A string containing console markup
    
        
    """
    ...

def render(markup, style, emoji, emoji_variant):
    """
    Render console markup in to a Text instance.
    
        Args:
            markup (str): A string containing console markup.
            style: (Union[str, Style]): The style to use.
            emoji (bool, optional): Also render emoji code. Defaults to True.
            emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.
    
    
        Raises:
            MarkupError: If there is a syntax error in the markup.
    
        Returns:
            Text: A test instance.
        
    """
    ...
