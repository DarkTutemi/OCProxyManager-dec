# Module: client
# Pseudo-source reconstructed from bytecode (no decompiler)


def escape(s):
    ...

def Error():
    """Error"""
    ...

def ProtocolError():
    """ProtocolError"""
    ...

def ResponseError():
    """ResponseError"""
    ...

def Fault():
    """Fault"""
    ...

def _try(fmt):
    ...

def _iso8601_format(value):
    ...

def _strftime(value):
    ...

def DateTime():
    """DateTime"""
    ...

def _datetime(data):
    ...

def _datetime_type(data):
    ...

def Binary():
    """Binary"""
    ...

def _binary(data):
    ...

def ExpatParser():
    """ExpatParser"""
    ...

def Marshaller():
    """Marshaller"""
    ...

def Unmarshaller():
    """Unmarshaller"""
    ...

def _MultiCallMethod():
    """_MultiCallMethod"""
    ...

def MultiCallIterator():
    """MultiCallIterator"""
    ...

def MultiCall():
    """MultiCall"""
    ...

def getparser(use_datetime, use_builtin_types):
    """
    getparser() -> parser, unmarshaller
    
        Create an instance of the fastest available parser, and attach it
        to an unmarshalling object.  Return both objects.
        
    """
    ...

def dumps(params, methodname, methodresponse, encoding, allow_none):
    """
    data [,options] -> marshalled data
    
        Convert an argument tuple or a Fault instance to an XML-RPC
        request (or response, if the methodresponse option is used).
    
        In addition to the data object, the following options can be given
        as keyword arguments:
    
            methodname: the method name for a methodCall packet
    
            methodresponse: true to create a methodResponse packet.
            If this option is used with a tuple, the tuple must be
            a singleton (i.e. it can contain only one element).
    
            encoding: the packet encoding (default is UTF-8)
    
        All byte strings in the data structure are assumed to use the
        packet encoding.  Unicode strings are automatically converted,
        where necessary.
        
    """
    ...

def loads(data, use_datetime, use_builtin_types):
    """
    data -> unmarshalled data, method name
    
        Convert an XML-RPC packet to unmarshalled data plus a method
        name (None if not present).
    
        If the XML-RPC packet represents a fault condition, this function
        raises a Fault exception.
        
    """
    ...

def gzip_encode(data):
    """
    data -> gzip encoded data
    
        Encode data using the gzip content encoding as described in RFC 1952
        
    """
    ...

def gzip_decode(data, max_decode):
    """
    gzip encoded data -> unencoded data
    
        Decode data using the gzip content encoding as described in RFC 1952
        
    """
    ...

def GzipDecodedResponse():
    """GzipDecodedResponse"""
    ...

def _Method():
    """_Method"""
    ...

def Transport():
    """Transport"""
    ...

def SafeTransport():
    """SafeTransport"""
    ...

def ServerProxy():
    """ServerProxy"""
    ...
