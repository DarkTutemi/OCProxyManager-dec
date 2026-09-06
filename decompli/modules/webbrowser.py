# Module: webbrowser
# Pseudo-source reconstructed from bytecode (no decompiler)


def Error():
    """Error"""
    ...

def register(name, klass, instance, *, preferred=None):
    """Register a browser connector."""
    ...

def get(using):
    """Return a browser launcher instance appropriate for the environment."""
    ...

def open(url, new, autoraise):
    """
    Display url using the default browser.
    
        If possible, open url in a location determined by new.
        - 0: the same browser window (the default).
        - 1: a new browser window.
        - 2: a new browser page ("tab").
        If possible, autoraise raises the window (the default) or not.
        
    """
    ...

def open_new(url):
    """
    Open url in a new window of the default browser.
    
        If not possible, then open url in the only browser window.
        
    """
    ...

def open_new_tab(url):
    """
    Open url in a new page ("tab") of the default browser.
    
        If not possible, then the behavior becomes equivalent to open_new().
        
    """
    ...

def _synthesize(browser, *, preferred=None):
    """
    Attempt to synthesize a controller based on existing controllers.
    
        This is useful to create a controller when a user specifies a path to
        an entry in the BROWSER environment variable -- we can copy a general
        controller to operate using a specific installation of the desired
        browser in this way.
    
        If we can't create a controller in this way, or if there is no
        executable for the requested browser, return [None, None].
    
        
    """
    ...

def BaseBrowser():
    """BaseBrowser"""
    ...

def GenericBrowser():
    """GenericBrowser"""
    ...

def BackgroundBrowser():
    """BackgroundBrowser"""
    ...

def UnixBrowser():
    """UnixBrowser"""
    ...

def Mozilla():
    """Mozilla"""
    ...

def Netscape():
    """Netscape"""
    ...

def Galeon():
    """Galeon"""
    ...

def Chrome():
    """Chrome"""
    ...

def Opera():
    """Opera"""
    ...

def Elinks():
    """Elinks"""
    ...

def Konqueror():
    """Konqueror"""
    ...

def Grail():
    """Grail"""
    ...

def register_X_browsers():
    ...

def register_standard_browsers():
    ...

def WindowsDefault():
    """WindowsDefault"""
    ...

def MacOSX():
    """MacOSX"""
    ...

def MacOSXOSAScript():
    """MacOSXOSAScript"""
    ...

def main():
    ...
