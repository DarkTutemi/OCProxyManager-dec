# Module: util
# Pseudo-source reconstructed from bytecode (no decompiler)


def _get_build_version():
    """
    Return the version of MSVC that was used to build Python.
    
            For Python 2.3 and up, the version number is included in
            sys.version.  For earlier versions, assume the compiler is MSVC 6.
            
    """
    ...

def find_msvcrt():
    """Return the name of the VC runtime dll"""
    ...

def find_library(name):
    ...

def _is_elf(filename):
    """Return True if the given file is an ELF file"""
    ...

def _findLib_gcc(name):
    ...

def _get_soname(f):
    ...

def _num_version(libname):
    ...

def _findLib_crle(name, is64):
    ...

def _findSoname_ldconfig(name):
    ...

def _findLib_ld(name):
    ...

def test():
    ...
