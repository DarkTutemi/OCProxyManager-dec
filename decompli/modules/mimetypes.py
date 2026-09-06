# Module: mimetypes
# Pseudo-source reconstructed from bytecode (no decompiler)


def MimeTypes():
    """MimeTypes"""
    ...

def guess_type(url, strict):
    """
    Guess the type of a file based on its URL.
    
        Return value is a tuple (type, encoding) where type is None if the
        type can't be guessed (no or unknown suffix) or a string of the
        form type/subtype, usable for a MIME Content-type header; and
        encoding is None for no encoding or the name of the program used
        to encode (e.g. compress or gzip).  The mappings are table
        driven.  Encoding suffixes are case sensitive; type suffixes are
        first tried case sensitive, then case insensitive.
    
        The suffixes .tgz, .taz and .tz (case sensitive!) are all mapped
        to ".tar.gz".  (This is table-driven too, using the dictionary
        suffix_map).
    
        Optional `strict' argument when false adds a bunch of commonly found, but
        non-standard types.
        
    """
    ...

def guess_all_extensions(type, strict):
    """
    Guess the extensions for a file based on its MIME type.
    
        Return value is a list of strings giving the possible filename
        extensions, including the leading dot ('.').  The extension is not
        guaranteed to have been associated with any particular data
        stream, but would be mapped to the MIME type `type' by
        guess_type().  If no extension can be guessed for `type', None
        is returned.
    
        Optional `strict' argument when false adds a bunch of commonly found,
        but non-standard types.
        
    """
    ...

def guess_extension(type, strict):
    """
    Guess the extension for a file based on its MIME type.
    
        Return value is a string giving a filename extension, including the
        leading dot ('.').  The extension is not guaranteed to have been
        associated with any particular data stream, but would be mapped to the
        MIME type `type' by guess_type().  If no extension can be guessed for
        `type', None is returned.
    
        Optional `strict' argument when false adds a bunch of commonly found,
        but non-standard types.
        
    """
    ...

def add_type(type, ext, strict):
    """
    Add a mapping between a type and an extension.
    
        When the extension is already known, the new
        type will replace the old one. When the type
        is already known the extension will be added
        to the list of known extensions.
    
        If strict is true, information will be added to
        list of standard types, else to the list of non-standard
        types.
        
    """
    ...

def init(files):
    ...

def read_mime_types(file):
    ...

def _default_mime_types():
    ...

def _main():
    ...
