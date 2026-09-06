# Module: parse
# Pseudo-source reconstructed from bytecode (no decompiler)


def clear_cache():
    """Clear internal performance caches. Undocumented; some tests want it."""
    ...

def _noop(obj):
    ...

def _encode_result(obj, encoding, errors):
    ...

def _decode_args(args, encoding, errors):
    ...

def _coerce_args(*args):
    ...

def _ResultMixinStr():
    """_ResultMixinStr"""
    ...

def _ResultMixinBytes():
    """_ResultMixinBytes"""
    ...

def _NetlocResultMixinBase():
    """_NetlocResultMixinBase"""
    ...

def _NetlocResultMixinStr():
    """_NetlocResultMixinStr"""
    ...

def _NetlocResultMixinBytes():
    """_NetlocResultMixinBytes"""
    ...

def DefragResult():
    """DefragResult"""
    ...

def SplitResult():
    """SplitResult"""
    ...

def ParseResult():
    """ParseResult"""
    ...

def DefragResultBytes():
    """DefragResultBytes"""
    ...

def SplitResultBytes():
    """SplitResultBytes"""
    ...

def ParseResultBytes():
    """ParseResultBytes"""
    ...

def _fix_result_transcoding():
    ...

def urlparse(url, scheme, allow_fragments):
    """
    Parse a URL into 6 components:
        <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    
        The result is a named 6-tuple with fields corresponding to the
        above. It is either a ParseResult or ParseResultBytes object,
        depending on the type of the url parameter.
    
        The username, password, hostname, and port sub-components of netloc
        can also be accessed as attributes of the returned object.
    
        The scheme argument provides the default value of the scheme
        component when no scheme is found in url.
    
        If allow_fragments is False, no attempt is made to separate the
        fragment component from the previous component, which can be either
        path or query.
    
        Note that % escapes are not expanded.
        
    """
    ...

def _splitparams(url):
    ...

def _splitnetloc(url, start):
    ...

def _checknetloc(netloc):
    ...

def _check_bracketed_host(hostname):
    ...

def urlsplit(url, scheme, allow_fragments):
    """
    Parse a URL into 5 components:
        <scheme>://<netloc>/<path>?<query>#<fragment>
    
        The result is a named 5-tuple with fields corresponding to the
        above. It is either a SplitResult or SplitResultBytes object,
        depending on the type of the url parameter.
    
        The username, password, hostname, and port sub-components of netloc
        can also be accessed as attributes of the returned object.
    
        The scheme argument provides the default value of the scheme
        component when no scheme is found in url.
    
        If allow_fragments is False, no attempt is made to separate the
        fragment component from the previous component, which can be either
        path or query.
    
        Note that % escapes are not expanded.
        
    """
    ...

def urlunparse(components):
    """
    Put a parsed URL back together again.  This may result in a
        slightly different, but equivalent URL, if the URL that was parsed
        originally had redundant delimiters, e.g. a ? with an empty query
        (the draft states that these are equivalent).
    """
    ...

def urlunsplit(components):
    """
    Combine the elements of a tuple as returned by urlsplit() into a
        complete URL as a string. The data argument can be any five-item iterable.
        This may result in a slightly different, but equivalent URL, if the URL that
        was parsed originally had unnecessary delimiters (for example, a ? with an
        empty query; the RFC states that these are equivalent).
    """
    ...

def urljoin(base, url, allow_fragments):
    """
    Join a base URL and a possibly relative URL to form an absolute
        interpretation of the latter.
    """
    ...

def urldefrag(url):
    """
    Removes any existing fragment from URL.
    
        Returns a tuple of the defragmented URL and the fragment.  If
        the URL contained no fragments, the second element is the
        empty string.
        
    """
    ...

def unquote_to_bytes(string):
    """unquote_to_bytes('abc%20def') -> b'abc def'."""
    ...

def unquote(string, encoding, errors):
    """
    Replace %xx escapes by their single-character equivalent. The optional
        encoding and errors parameters specify how to decode percent-encoded
        sequences into Unicode characters, as accepted by the bytes.decode()
        method.
        By default, percent-encoded sequences are decoded with UTF-8, and invalid
        sequences are replaced by a placeholder character.
    
        unquote('abc%20def') -> 'abc def'.
        
    """
    ...

def parse_qs(qs, keep_blank_values, strict_parsing, encoding, errors, max_num_fields, separator):
    """
    Parse a query given as a string argument.
    
            Arguments:
    
            qs: percent-encoded query string to be parsed
    
            keep_blank_values: flag indicating whether blank values in
                percent-encoded queries should be treated as blank strings.
                A true value indicates that blanks should be retained as
                blank strings.  The default false value indicates that
                blank values are to be ignored and treated as if they were
                not included.
    
            strict_parsing: flag indicating what to do with parsing errors.
                If false (the default), errors are silently ignored.
                If true, errors raise a ValueError exception.
    
            encoding and errors: specify how to decode percent-encoded sequences
                into Unicode characters, as accepted by the bytes.decode() method.
    
            max_num_fields: int. If set, then throws a ValueError if there
                are more than n fields read by parse_qsl().
    
            separator: str. The symbol to use for separating the query arguments.
                Defaults to &.
    
            Returns a dictionary.
        
    """
    ...

def parse_qsl(qs, keep_blank_values, strict_parsing, encoding, errors, max_num_fields, separator):
    """
    Parse a query given as a string argument.
    
            Arguments:
    
            qs: percent-encoded query string to be parsed
    
            keep_blank_values: flag indicating whether blank values in
                percent-encoded queries should be treated as blank strings.
                A true value indicates that blanks should be retained as blank
                strings.  The default false value indicates that blank values
                are to be ignored and treated as if they were  not included.
    
            strict_parsing: flag indicating what to do with parsing errors. If
                false (the default), errors are silently ignored. If true,
                errors raise a ValueError exception.
    
            encoding and errors: specify how to decode percent-encoded sequences
                into Unicode characters, as accepted by the bytes.decode() method.
    
            max_num_fields: int. If set, then throws a ValueError
                if there are more than n fields read by parse_qsl().
    
            separator: str. The symbol to use for separating the query arguments.
                Defaults to &.
    
            Returns a list, as G-d intended.
        
    """
    ...

def unquote_plus(string, encoding, errors):
    """
    Like unquote(), but also replace plus signs by spaces, as required for
        unquoting HTML form values.
    
        unquote_plus('%7e/abc+def') -> '~/abc def'
        
    """
    ...

def __getattr__(name):
    ...

def _Quoter():
    """_Quoter"""
    ...

def quote(string, safe, encoding, errors):
    """
    quote('abc def') -> 'abc%20def'
    
        Each part of a URL, e.g. the path info, the query, etc., has a
        different set of reserved characters that must be quoted. The
        quote function offers a cautious (not minimal) way to quote a
        string for most of these parts.
    
        RFC 3986 Uniform Resource Identifier (URI): Generic Syntax lists
        the following (un)reserved characters.
    
        unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
        reserved      = gen-delims / sub-delims
        gen-delims    = ":" / "/" / "?" / "#" / "[" / "]" / "@"
        sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
                      / "*" / "+" / "," / ";" / "="
    
        Each of the reserved characters is reserved in some component of a URL,
        but not necessarily in all of them.
    
        The quote function %-escapes all characters that are neither in the
        unreserved chars ("always safe") nor the additional chars set via the
        safe arg.
    
        The default for the safe arg is '/'. The character is reserved, but in
        typical usage the quote function is being called on a path where the
        existing slash characters are to be preserved.
    
        Python 3.7 updates from using RFC 2396 to RFC 3986 to quote URL strings.
        Now, "~" is included in the set of unreserved characters.
    
        string and safe may be either str or bytes objects. encoding and errors
        must not be specified if string is a bytes object.
    
        The optional encoding and errors parameters specify how to deal with
        non-ASCII characters, as accepted by the str.encode method.
        By default, encoding='utf-8' (characters are encoded with UTF-8), and
        errors='strict' (unsupported characters raise a UnicodeEncodeError).
        
    """
    ...

def quote_plus(string, safe, encoding, errors):
    """
    Like quote(), but also replace ' ' with '+', as required for quoting
        HTML form values. Plus signs in the original string are escaped unless
        they are included in safe. It also does not have safe default to '/'.
        
    """
    ...

def _byte_quoter_factory(safe):
    ...

def quote_from_bytes(bs, safe):
    """
    Like quote(), but accepts a bytes object rather than a str, and does
        not perform string-to-bytes encoding.  It always returns an ASCII string.
        quote_from_bytes(b'abc def?') -> 'abc%20def%3f'
        
    """
    ...

def urlencode(query, doseq, safe, encoding, errors, quote_via):
    """
    Encode a dict or sequence of two-element tuples into a URL query string.
    
        If any values in the query arg are sequences and doseq is true, each
        sequence element is converted to a separate parameter.
    
        If the query arg is a sequence of two-element tuples, the order of the
        parameters in the output will match the order of parameters in the
        input.
    
        The components of a query arg may each be either a string or a bytes type.
    
        The safe, encoding, and errors parameters are passed down to the function
        specified by quote_via (encoding and errors only if a component is a str).
        
    """
    ...

def to_bytes(url):
    ...

def _to_bytes(url):
    """to_bytes(u"URL") --> 'URL'."""
    ...

def unwrap(url):
    """
    Transform a string like '<URL:scheme://host/path>' into 'scheme://host/path'.
    
        The string is returned unchanged if it's not a wrapped URL.
        
    """
    ...

def splittype(url):
    ...

def _splittype(url):
    """splittype('type:opaquestring') --> 'type', 'opaquestring'."""
    ...

def splithost(url):
    ...

def _splithost(url):
    """splithost('//host[:port]/path') --> 'host[:port]', '/path'."""
    ...

def splituser(host):
    ...

def _splituser(host):
    """splituser('user[:passwd]@host[:port]') --> 'user[:passwd]', 'host[:port]'."""
    ...

def splitpasswd(user):
    ...

def _splitpasswd(user):
    """splitpasswd('user:passwd') -> 'user', 'passwd'."""
    ...

def splitport(host):
    ...

def _splitport(host):
    """splitport('host:port') --> 'host', 'port'."""
    ...

def splitnport(host, defport):
    ...

def _splitnport(host, defport):
    """
    Split host and port, returning numeric port.
        Return given default port if no ':' found; defaults to -1.
        Return numerical port if a valid number is found after ':'.
        Return None if ':' but not a valid number.
    """
    ...

def splitquery(url):
    ...

def _splitquery(url):
    """splitquery('/path?query') --> '/path', 'query'."""
    ...

def splittag(url):
    ...

def _splittag(url):
    """splittag('/path#tag') --> '/path', 'tag'."""
    ...

def splitattr(url):
    ...

def _splitattr(url):
    """
    splitattr('/path;attr1=value1;attr2=value2;...') ->
            '/path', ['attr1=value1', 'attr2=value2', ...].
    """
    ...

def splitvalue(attr):
    ...

def _splitvalue(attr):
    """splitvalue('attr=value') --> 'attr', 'value'."""
    ...
