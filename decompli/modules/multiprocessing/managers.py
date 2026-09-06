# Module: managers
# Pseudo-source reconstructed from bytecode (no decompiler)


def reduce_array(a):
    ...

def rebuild_as_list(obj):
    ...

def Token():
    """Token"""
    ...

def dispatch(c, id, methodname, args, kwds):
    """
    
        Send a message to manager using connection `c` and return response
        
    """
    ...

def convert_to_error(kind, result):
    ...

def RemoteError():
    """RemoteError"""
    ...

def all_methods(obj):
    """
    
        Return a list of names of methods of `obj`
        
    """
    ...

def public_methods(obj):
    """
    
        Return a list of names of methods of `obj` which do not start with '_'
        
    """
    ...

def Server():
    """Server"""
    ...

def State():
    """State"""
    ...

def BaseManager():
    """BaseManager"""
    ...

def ProcessLocalSet():
    """ProcessLocalSet"""
    ...

def BaseProxy():
    """BaseProxy"""
    ...

def RebuildProxy(func, token, serializer, kwds):
    """
    
        Function used for unpickling proxy objects.
        
    """
    ...

def MakeProxyType(name, exposed, _cache):
    """
    
        Return a proxy type whose methods are given by `exposed`
        
    """
    ...

def AutoProxy(token, serializer, manager, authkey, exposed, incref, manager_owned):
    """
    
        Return an auto-proxy for `token`
        
    """
    ...

def Namespace():
    """Namespace"""
    ...

def Value():
    """Value"""
    ...

def Array(typecode, sequence, lock):
    ...

def IteratorProxy():
    """IteratorProxy"""
    ...

def AcquirerProxy():
    """AcquirerProxy"""
    ...

def ConditionProxy():
    """ConditionProxy"""
    ...

def EventProxy():
    """EventProxy"""
    ...

def BarrierProxy():
    """BarrierProxy"""
    ...

def NamespaceProxy():
    """NamespaceProxy"""
    ...

def ValueProxy():
    """ValueProxy"""
    ...

def ListProxy():
    """ListProxy"""
    ...

def PoolProxy():
    """PoolProxy"""
    ...

def SyncManager():
    """SyncManager"""
    ...

def _SharedMemoryTracker():
    """_SharedMemoryTracker"""
    ...

def SharedMemoryServer():
    """SharedMemoryServer"""
    ...

def SharedMemoryManager():
    """SharedMemoryManager"""
    ...
