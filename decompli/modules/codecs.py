# Module: codecs
# Pseudo-source reconstructed from bytecode (no decompiler)


def CodecInfo():
    """CodecInfo"""
    ...

def Codec():
    """Codec"""
    ...

def IncrementalEncoder():
    """IncrementalEncoder"""
    ...

def BufferedIncrementalEncoder():
    """BufferedIncrementalEncoder"""
    ...

def IncrementalDecoder():
    """IncrementalDecoder"""
    ...

def BufferedIncrementalDecoder():
    """BufferedIncrementalDecoder"""
    ...

def StreamWriter():
    """StreamWriter"""
    ...

def StreamReader():
    """StreamReader"""
    ...

def StreamReaderWriter():
    """StreamReaderWriter"""
    ...

def StreamRecoder():
    """StreamRecoder"""
    ...

def open(filename, mode, encoding, errors, buffering):
    """
     Open an encoded file using the given mode and return
            a wrapped version providing transparent encoding/decoding.
    
            Note: The wrapped version will only accept the object format
            defined by the codecs, i.e. Unicode objects for most builtin
            codecs. Output is also codec dependent and will usually be
            Unicode as well.
    
            If encoding is not None, then the
            underlying encoded files are always opened in binary mode.
            The default file mode is 'r', meaning to open the file in read mode.
    
            encoding specifies the encoding which is to be used for the
            file.
    
            errors may be given to define the error handling. It defaults
            to 'strict' which causes ValueErrors to be raised in case an
            encoding error occurs.
    
            buffering has the same meaning as for the builtin open() API.
            It defaults to -1 which means that the default buffer size will
            be used.
    
            The returned wrapped file object provides an extra attribute
            .encoding which allows querying the used encoding. This
            attribute is only available if an encoding was specified as
            parameter.
    
        
    """
    ...

def EncodedFile(file, data_encoding, file_encoding, errors):
    """
     Return a wrapped version of file which provides transparent
            encoding translation.
    
            Data written to the wrapped file is decoded according
            to the given data_encoding and then encoded to the underlying
            file using file_encoding. The intermediate data type
            will usually be Unicode but depends on the specified codecs.
    
            Bytes read from the file are decoded using file_encoding and then
            passed back to the caller encoded using data_encoding.
    
            If file_encoding is not given, it defaults to data_encoding.
    
            errors may be given to define the error handling. It defaults
            to 'strict' which causes ValueErrors to be raised in case an
            encoding error occurs.
    
            The returned wrapped file object provides two extra attributes
            .data_encoding and .file_encoding which reflect the given
            parameters of the same name. The attributes can be used for
            introspection by Python programs.
    
        
    """
    ...

def getencoder(encoding):
    """
     Lookup up the codec for the given encoding and return
            its encoder function.
    
            Raises a LookupError in case the encoding cannot be found.
    
        
    """
    ...

def getdecoder(encoding):
    """
     Lookup up the codec for the given encoding and return
            its decoder function.
    
            Raises a LookupError in case the encoding cannot be found.
    
        
    """
    ...

def getincrementalencoder(encoding):
    """
     Lookup up the codec for the given encoding and return
            its IncrementalEncoder class or factory function.
    
            Raises a LookupError in case the encoding cannot be found
            or the codecs doesn't provide an incremental encoder.
    
        
    """
    ...

def getincrementaldecoder(encoding):
    """
     Lookup up the codec for the given encoding and return
            its IncrementalDecoder class or factory function.
    
            Raises a LookupError in case the encoding cannot be found
            or the codecs doesn't provide an incremental decoder.
    
        
    """
    ...

def getreader(encoding):
    """
     Lookup up the codec for the given encoding and return
            its StreamReader class or factory function.
    
            Raises a LookupError in case the encoding cannot be found.
    
        
    """
    ...

def getwriter(encoding):
    """
     Lookup up the codec for the given encoding and return
            its StreamWriter class or factory function.
    
            Raises a LookupError in case the encoding cannot be found.
    
        
    """
    ...

def iterencode(iterator, encoding, errors, **kwargs):
    """
    
        Encoding iterator.
    
        Encodes the input strings from the iterator using an IncrementalEncoder.
    
        errors and kwargs are passed through to the IncrementalEncoder
        constructor.
        
    """
    ...

def iterdecode(iterator, encoding, errors, **kwargs):
    """
    
        Decoding iterator.
    
        Decodes the input strings from the iterator using an IncrementalDecoder.
    
        errors and kwargs are passed through to the IncrementalDecoder
        constructor.
        
    """
    ...

def make_identity_dict(rng):
    """
     make_identity_dict(rng) -> dict
    
            Return a dictionary where elements of the rng sequence are
            mapped to themselves.
    
        
    """
    ...

def make_encoding_map(decoding_map):
    """
     Creates an encoding map from a decoding map.
    
            If a target mapping in the decoding map occurs multiple
            times, then that target is mapped to None (undefined mapping),
            causing an exception when encountered by the charmap codec
            during translation.
    
            One example where this happens is cp875.py which decodes
            multiple character to \u001a.
    
        
    """
    ...
