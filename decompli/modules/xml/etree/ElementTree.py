# Module: ElementTree
# Pseudo-source reconstructed from bytecode (no decompiler)


def ParseError():
    """ParseError"""
    ...

def iselement(element):
    """Return True if *element* appears to be an Element."""
    ...

def Element():
    """Element"""
    ...

def SubElement(parent, tag, attrib, **extra):
    """
    Subelement factory which creates an element instance, and appends it
        to an existing parent.
    
        The element tag, attribute names, and attribute values can be either
        bytes or Unicode strings.
    
        *parent* is the parent element, *tag* is the subelements name, *attrib* is
        an optional directory containing element attributes, *extra* are
        additional attributes given as keyword arguments.
    
        
    """
    ...

def Comment(text):
    """
    Comment element factory.
    
        This function creates a special element which the standard serializer
        serializes as an XML comment.
    
        *text* is a string containing the comment string.
    
        
    """
    ...

def ProcessingInstruction(target, text):
    """
    Processing Instruction element factory.
    
        This function creates a special element which the standard serializer
        serializes as an XML comment.
    
        *target* is a string containing the processing instruction, *text* is a
        string containing the processing instruction contents, if any.
    
        
    """
    ...

def QName():
    """QName"""
    ...

def ElementTree():
    """ElementTree"""
    ...

def _get_writer(file_or_filename, encoding):
    ...

def _namespaces(elem, default_namespace):
    ...

def _serialize_xml(write, elem, qnames, namespaces, short_empty_elements, **kwargs):
    ...

def _serialize_html(write, elem, qnames, namespaces, **kwargs):
    ...

def _serialize_text(write, elem):
    ...

def register_namespace(prefix, uri):
    """
    Register a namespace prefix.
    
        The registry is global, and any existing mapping for either the
        given prefix or the namespace URI will be removed.
    
        *prefix* is the namespace prefix, *uri* is a namespace uri. Tags and
        attributes in this namespace will be serialized with prefix if possible.
    
        ValueError is raised if prefix is reserved or is invalid.
    
        
    """
    ...

def _raise_serialization_error(text):
    ...

def _escape_cdata(text):
    ...

def _escape_attrib(text):
    ...

def _escape_attrib_html(text):
    ...

def tostring(element, encoding, method, *, xml_declaration=None, default_namespace=None, short_empty_elements=None):
    """
    Generate string representation of XML element.
    
        All subelements are included.  If encoding is "unicode", a string
        is returned. Otherwise a bytestring is returned.
    
        *element* is an Element instance, *encoding* is an optional output
        encoding defaulting to US-ASCII, *method* is an optional output which can
        be one of "xml" (default), "html", "text" or "c14n", *default_namespace*
        sets the default XML namespace (for "xmlns").
    
        Returns an (optionally) encoded string containing the XML data.
    
        
    """
    ...

def _ListDataStream():
    """_ListDataStream"""
    ...

def tostringlist(element, encoding, method, *, xml_declaration=None, default_namespace=None, short_empty_elements=None):
    ...

def dump(elem):
    """
    Write element tree or element structure to sys.stdout.
    
        This function should be used for debugging only.
    
        *elem* is either an ElementTree, or a single Element.  The exact output
        format is implementation dependent.  In this version, it's written as an
        ordinary XML file.
    
        
    """
    ...

def indent(tree, space, level):
    """
    Indent an XML document by inserting newlines and indentation space
        after elements.
    
        *tree* is the ElementTree or Element to modify.  The (root) element
        itself will not be changed, but the tail text of all elements in its
        subtree will be adapted.
    
        *space* is the whitespace to insert for each indentation level, two
        space characters by default.
    
        *level* is the initial indentation level. Setting this to a higher
        value than 0 can be used for indenting subtrees that are more deeply
        nested inside of a document.
        
    """
    ...

def parse(source, parser):
    """
    Parse XML document into element tree.
    
        *source* is a filename or file object containing XML data,
        *parser* is an optional parser instance defaulting to XMLParser.
    
        Return an ElementTree instance.
    
        
    """
    ...

def iterparse(source, events, parser):
    """
    Incrementally parse XML document into ElementTree.
    
        This class also reports what's going on to the user based on the
        *events* it is initialized with.  The supported events are the strings
        "start", "end", "start-ns" and "end-ns" (the "ns" events are used to get
        detailed namespace information).  If *events* is omitted, only
        "end" events are reported.
    
        *source* is a filename or file object containing XML data, *events* is
        a list of events to report back, *parser* is an optional parser instance.
    
        Returns an iterator providing (event, elem) pairs.
    
        
    """
    ...

def XMLPullParser():
    """XMLPullParser"""
    ...

def XML(text, parser):
    """
    Parse XML document from string constant.
    
        This function can be used to embed "XML Literals" in Python code.
    
        *text* is a string containing XML data, *parser* is an
        optional parser instance, defaulting to the standard XMLParser.
    
        Returns an Element instance.
    
        
    """
    ...

def XMLID(text, parser):
    """
    Parse XML document from string constant for its IDs.
    
        *text* is a string containing XML data, *parser* is an
        optional parser instance, defaulting to the standard XMLParser.
    
        Returns an (Element, dict) tuple, in which the
        dict maps element id:s to elements.
    
        
    """
    ...

def fromstringlist(sequence, parser):
    """
    Parse XML document from sequence of string fragments.
    
        *sequence* is a list of other sequence, *parser* is an optional parser
        instance, defaulting to the standard XMLParser.
    
        Returns an Element instance.
    
        
    """
    ...

def TreeBuilder():
    """TreeBuilder"""
    ...

def XMLParser():
    """XMLParser"""
    ...

def canonicalize(xml_data, *, out=None, from_file=None, **options):
    """
    Convert XML to its C14N 2.0 serialised form.
    
        If *out* is provided, it must be a file or file-like object that receives
        the serialised canonical XML output (text, not bytes) through its ``.write()``
        method.  To write to a file, open it in text mode with encoding "utf-8".
        If *out* is not provided, this function returns the output as text string.
    
        Either *xml_data* (an XML string) or *from_file* (a file path or
        file-like object) must be provided as input.
    
        The configuration options are the same as for the ``C14NWriterTarget``.
        
    """
    ...

def C14NWriterTarget():
    """C14NWriterTarget"""
    ...

def _escape_cdata_c14n(text):
    ...

def _escape_attrib_c14n(text):
    ...
