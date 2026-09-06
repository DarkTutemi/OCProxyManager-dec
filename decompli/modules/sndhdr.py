# Module: sndhdr
# Pseudo-source reconstructed from bytecode (no decompiler)


def what(filename):
    """Guess the type of a sound file."""
    ...

def whathdr(filename):
    """Recognize sound headers."""
    ...

def test_aifc(h, f):
    """AIFC and AIFF files"""
    ...

def test_au(h, f):
    """AU and SND files"""
    ...

def test_hcom(h, f):
    """HCOM file"""
    ...

def test_voc(h, f):
    """VOC file"""
    ...

def test_wav(h, f):
    """WAV file"""
    ...

def test_8svx(h, f):
    """8SVX file"""
    ...

def test_sndt(h, f):
    """SNDT file"""
    ...

def test_sndr(h, f):
    """SNDR file"""
    ...

def get_long_be(b):
    ...

def get_long_le(b):
    ...

def get_short_be(b):
    ...

def get_short_le(b):
    ...

def test():
    ...

def testall(list, recursive, toplevel):
    ...
