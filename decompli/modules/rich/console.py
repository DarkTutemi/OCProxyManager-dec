# Module: console
# Pseudo-source reconstructed from bytecode (no decompiler)


def NoChange():
    """NoChange"""
    ...

def ConsoleDimensions():
    """ConsoleDimensions"""
    ...

def ConsoleOptions():
    """ConsoleOptions"""
    ...

def RichCast():
    """RichCast"""
    ...

def ConsoleRenderable():
    """ConsoleRenderable"""
    ...

def CaptureError():
    """CaptureError"""
    ...

def NewLine():
    """NewLine"""
    ...

def ScreenUpdate():
    """ScreenUpdate"""
    ...

def Capture():
    """Capture"""
    ...

def ThemeContext():
    """ThemeContext"""
    ...

def PagerContext():
    """PagerContext"""
    ...

def ScreenContext():
    """ScreenContext"""
    ...

def Group():
    """Group"""
    ...

def group(fit):
    """
    A decorator that turns an iterable of renderables in to a group.
    
        Args:
            fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
        
    """
    ...

def _is_jupyter():
    """Check if we're running in a Jupyter notebook."""
    ...

def ConsoleThreadLocals():
    """ConsoleThreadLocals"""
    ...

def RenderHook():
    """RenderHook"""
    ...

def get_windows_console_features():
    ...

def detect_legacy_windows():
    """Detect legacy Windows."""
    ...

def Console():
    """Console"""
    ...

def _svg_hash(svg_main_code):
    """
    Returns a unique hash for the given SVG main code.
    
        Args:
            svg_main_code (str): The content we're going to inject in the SVG envelope.
    
        Returns:
            str: a hash of the given content
        
    """
    ...
