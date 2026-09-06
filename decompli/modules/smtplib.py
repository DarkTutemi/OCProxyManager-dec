# Module: smtplib
# Pseudo-source reconstructed from bytecode (no decompiler)


def SMTPException():
    """SMTPException"""
    ...

def SMTPNotSupportedError():
    """SMTPNotSupportedError"""
    ...

def SMTPServerDisconnected():
    """SMTPServerDisconnected"""
    ...

def SMTPResponseException():
    """SMTPResponseException"""
    ...

def SMTPSenderRefused():
    """SMTPSenderRefused"""
    ...

def SMTPRecipientsRefused():
    """SMTPRecipientsRefused"""
    ...

def SMTPDataError():
    """SMTPDataError"""
    ...

def SMTPConnectError():
    """SMTPConnectError"""
    ...

def SMTPHeloError():
    """SMTPHeloError"""
    ...

def SMTPAuthenticationError():
    """SMTPAuthenticationError"""
    ...

def quoteaddr(addrstring):
    """
    Quote a subset of the email addresses defined by RFC 821.
    
        Should be able to handle anything email.utils.parseaddr can handle.
        
    """
    ...

def _addr_only(addrstring):
    ...

def quotedata(data):
    """
    Quote data for email.
    
        Double leading '.', and change Unix newline '\n', or Mac '\r' into
        internet CRLF end-of-line.
        
    """
    ...

def _quote_periods(bindata):
    ...

def _fix_eols(data):
    ...

def SMTP():
    """SMTP"""
    ...

def SMTP_SSL():
    """SMTP_SSL"""
    ...

def LMTP():
    """LMTP"""
    ...

def prompt(prompt):
    ...
