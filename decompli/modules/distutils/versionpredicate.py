# Module: versionpredicate
# Pseudo-source reconstructed from bytecode (no decompiler)


def splitUp(pred):
    """
    Parse a single version comparison.
    
        Return (comparison string, StrictVersion)
        
    """
    ...

def VersionPredicate():
    """VersionPredicate"""
    ...

def split_provision(value):
    """
    Return the name and optional version number of a provision.
    
        The version number, if given, will be returned as a `StrictVersion`
        instance, otherwise it will be `None`.
    
        >>> split_provision('mypkg')
        ('mypkg', None)
        >>> split_provision(' mypkg( 1.2 ) ')
        ('mypkg', StrictVersion ('1.2'))
        
    """
    ...
