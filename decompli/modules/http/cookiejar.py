# Module: cookiejar
# Pseudo-source reconstructed from bytecode (no decompiler)


def _debug(*args):
    ...

def _warn_unhandled_exception():
    ...

def _timegm(tt):
    ...

def time2isoz(t):
    """
    Return a string representing time in seconds since epoch, t.
    
        If the function is called without an argument, it will use the current
        time.
    
        The format of the returned string is like "YYYY-MM-DD hh:mm:ssZ",
        representing Universal Time (UTC, aka GMT).  An example of this format is:
    
        1994-11-24 08:49:37Z
    
        
    """
    ...

def time2netscape(t):
    """
    Return a string representing time in seconds since epoch, t.
    
        If the function is called without an argument, it will use the current
        time.
    
        The format of the returned string is like this:
    
        Wed, DD-Mon-YYYY HH:MM:SS GMT
    
        
    """
    ...

def offset_from_tz_string(tz):
    ...

def _str2time(day, mon, yr, hr, min, sec, tz):
    ...

def http2time(text):
    """
    Returns time in seconds since epoch of time represented by a string.
    
        Return value is an integer.
    
        None is returned if the format of str is unrecognized, the time is outside
        the representable range, or the timezone string is not recognized.  If the
        string contains no timezone, UTC is assumed.
    
        The timezone in the string may be numerical (like "-0800" or "+0100") or a
        string timezone (like "UTC", "GMT", "BST" or "EST").  Currently, only the
        timezone strings equivalent to UTC (zero offset) are known to the function.
    
        The function loosely parses the following formats:
    
        Wed, 09 Feb 1994 22:23:32 GMT       -- HTTP format
        Tuesday, 08-Feb-94 14:15:29 GMT     -- old rfc850 HTTP format
        Tuesday, 08-Feb-1994 14:15:29 GMT   -- broken rfc850 HTTP format
        09 Feb 1994 22:23:32 GMT            -- HTTP format (no weekday)
        08-Feb-94 14:15:29 GMT              -- rfc850 format (no weekday)
        08-Feb-1994 14:15:29 GMT            -- broken rfc850 format (no weekday)
    
        The parser ignores leading and trailing whitespace.  The time may be
        absent.
    
        If the year is given with only 2 digits, the function will select the
        century that makes the year closest to the current date.
    
        
    """
    ...

def iso2time(text):
    """
    
        As for http2time, but parses the ISO 8601 formats:
    
        1994-02-03 14:15:29 -0100    -- ISO 8601 format
        1994-02-03 14:15:29          -- zone is optional
        1994-02-03                   -- only date
        1994-02-03T14:15:29          -- Use T as separator
        19940203T141529Z             -- ISO 8601 compact format
        19940203                     -- only date
    
        
    """
    ...

def unmatched(match):
    """Return unmatched part of re.Match object."""
    ...

def split_header_words(header_values):
    """
    Parse header values into a list of lists containing key,value pairs.
    
        The function knows how to deal with ",", ";" and "=" as well as quoted
        values after "=".  A list of space separated tokens are parsed as if they
        were separated by ";".
    
        If the header_values passed as argument contains multiple values, then they
        are treated as if they were a single value separated by comma ",".
    
        This means that this function is useful for parsing header fields that
        follow this syntax (BNF as from the HTTP/1.1 specification, but we relax
        the requirement for tokens).
    
          headers           = #header
          header            = (token | parameter) *( [";"] (token | parameter))
    
          token             = 1*<any CHAR except CTLs or separators>
          separators        = "(" | ")" | "<" | ">" | "@"
                            | "," | ";" | ":" | "\" | <">
                            | "/" | "[" | "]" | "?" | "="
                            | "{" | "}" | SP | HT
    
          quoted-string     = ( <"> *(qdtext | quoted-pair ) <"> )
          qdtext            = <any TEXT except <">>
          quoted-pair       = "\" CHAR
    
          parameter         = attribute "=" value
          attribute         = token
          value             = token | quoted-string
    
        Each header is represented by a list of key/value pairs.  The value for a
        simple token (not part of a parameter) is None.  Syntactically incorrect
        headers will not necessarily be parsed as you would want.
    
        This is easier to describe with some examples:
    
        >>> split_header_words(['foo="bar"; port="80,81"; discard, bar=baz'])
        [[('foo', 'bar'), ('port', '80,81'), ('discard', None)], [('bar', 'baz')]]
        >>> split_header_words(['text/html; charset="iso-8859-1"'])
        [[('text/html', None), ('charset', 'iso-8859-1')]]
        >>> split_header_words([r'Basic realm="\"foo\bar\""'])
        [[('Basic', None), ('realm', '"foobar"')]]
    
        
    """
    ...

def join_header_words(lists):
    """
    Do the inverse (almost) of the conversion done by split_header_words.
    
        Takes a list of lists of (key, value) pairs and produces a single header
        value.  Attribute values are quoted if needed.
    
        >>> join_header_words([[("text/plain", None), ("charset", "iso-8859-1")]])
        'text/plain; charset="iso-8859-1"'
        >>> join_header_words([[("text/plain", None)], [("charset", "iso-8859-1")]])
        'text/plain, charset="iso-8859-1"'
    
        
    """
    ...

def strip_quotes(text):
    ...

def parse_ns_headers(ns_headers):
    """
    Ad-hoc parser for Netscape protocol cookie-attributes.
    
        The old Netscape cookie format for Set-Cookie can for instance contain
        an unquoted "," in the expires field, so we have to use this ad-hoc
        parser instead of split_header_words.
    
        XXX This may not make the best possible effort to parse all the crap
        that Netscape Cookie headers contain.  Ronald Tschalar's HTTPClient
        parser is probably better, so could do worse than following that if
        this ever gives any trouble.
    
        Currently, this is also used for parsing RFC 2109 cookies.
    
        
    """
    ...

def is_HDN(text):
    """Return True if text is a host domain name."""
    ...

def domain_match(A, B):
    """
    Return True if domain A domain-matches domain B, according to RFC 2965.
    
        A and B may be host domain names or IP addresses.
    
        RFC 2965, section 1:
    
        Host names can be specified either as an IP address or a HDN string.
        Sometimes we compare one host name with another.  (Such comparisons SHALL
        be case-insensitive.)  Host A's name domain-matches host B's if
    
             *  their host name strings string-compare equal; or
    
             * A is a HDN string and has the form NB, where N is a non-empty
                name string, B has the form .B', and B' is a HDN string.  (So,
                x.y.com domain-matches .Y.com but not Y.com.)
    
        Note that domain-match is not a commutative operation: a.b.c.com
        domain-matches .c.com, but not the reverse.
    
        
    """
    ...

def liberal_is_HDN(text):
    """
    Return True if text is a sort-of-like a host domain name.
    
        For accepting/blocking domains.
    
        
    """
    ...

def user_domain_match(A, B):
    """
    For blocking/accepting domains.
    
        A and B may be host domain names or IP addresses.
    
        
    """
    ...

def request_host(request):
    """
    Return request-host, as defined by RFC 2965.
    
        Variation from RFC: returned value is lowercased, for convenient
        comparison.
    
        
    """
    ...

def eff_request_host(request):
    """
    Return a tuple (request-host, effective request-host name).
    
        As defined by RFC 2965, except both are lowercased.
    
        
    """
    ...

def request_path(request):
    """Path component of request-URI, as defined by RFC 2965."""
    ...

def request_port(request):
    ...

def uppercase_escaped_char(match):
    ...

def escape_path(path):
    """Escape any invalid characters in HTTP URL, and uppercase all escapes."""
    ...

def reach(h):
    """
    Return reach of host h, as defined by RFC 2965, section 1.
    
        The reach R of a host name H is defined as follows:
    
           *  If
    
              -  H is the host domain name of a host; and,
    
              -  H has the form A.B; and
    
              -  A has no embedded (that is, interior) dots; and
    
              -  B has at least one embedded dot, or B is the string "local".
                 then the reach of H is .B.
    
           *  Otherwise, the reach of H is H.
    
        >>> reach("www.acme.com")
        '.acme.com'
        >>> reach("acme.com")
        'acme.com'
        >>> reach("acme.local")
        '.local'
    
        
    """
    ...

def is_third_party(request):
    """
    
    
        RFC 2965, section 3.3.6:
    
            An unverifiable transaction is to a third-party host if its request-
            host U does not domain-match the reach R of the request-host O in the
            origin transaction.
    
        
    """
    ...

def Cookie():
    """Cookie"""
    ...

def CookiePolicy():
    """CookiePolicy"""
    ...

def DefaultCookiePolicy():
    """DefaultCookiePolicy"""
    ...

def deepvalues(mapping):
    """Iterates over nested mapping, depth-first"""
    ...

def Absent():
    """Absent"""
    ...

def CookieJar():
    """CookieJar"""
    ...

def LoadError():
    """LoadError"""
    ...

def FileCookieJar():
    """FileCookieJar"""
    ...

def lwp_cookie_str(cookie):
    """
    Return string representation of Cookie in the LWP cookie file format.
    
        Actually, the format is extended a bit -- see module docstring.
    
        
    """
    ...

def LWPCookieJar():
    """LWPCookieJar"""
    ...

def MozillaCookieJar():
    """MozillaCookieJar"""
    ...
