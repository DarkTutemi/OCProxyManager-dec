# Module: encoders
# Pseudo-source reconstructed from bytecode (no decompiler)


def _qencode(s):
    ...

def encode_base64(msg):
    """
    Encode the message's payload in Base64.
    
        Also, add an appropriate Content-Transfer-Encoding header.
        
    """
    ...

def encode_quopri(msg):
    """
    Encode the message's payload in quoted-printable.
    
        Also, add an appropriate Content-Transfer-Encoding header.
        
    """
    ...

def encode_7or8bit(msg):
    """Set the Content-Transfer-Encoding header to 7bit or 8bit."""
    ...

def encode_noop(msg):
    """Do nothing."""
    ...
