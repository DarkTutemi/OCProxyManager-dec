# Module: gettext
# Pseudo-source reconstructed from bytecode (no decompiler)


def _tokenize(plural):
    ...

def _error(value):
    ...

def _parse(tokens, priority):
    ...

def _as_int(n):
    ...

def c2py(plural):
    """
    Gets a C expression as used in PO files for plural forms and returns a
        Python function that implements an equivalent expression.
        
    """
    ...

def _expand_lang(loc):
    ...

def NullTranslations():
    """NullTranslations"""
    ...

def GNUTranslations():
    """GNUTranslations"""
    ...

def find(domain, localedir, languages, all):
    ...

def translation(domain, localedir, languages, class_, fallback):
    ...

def install(domain, localedir, *, names=None):
    ...

def textdomain(domain):
    ...

def bindtextdomain(domain, localedir):
    ...

def dgettext(domain, message):
    ...

def dngettext(domain, msgid1, msgid2, n):
    ...

def dpgettext(domain, context, message):
    ...

def dnpgettext(domain, context, msgid1, msgid2, n):
    ...

def gettext(message):
    ...

def ngettext(msgid1, msgid2, n):
    ...

def pgettext(context, message):
    ...

def npgettext(context, msgid1, msgid2, n):
    ...
