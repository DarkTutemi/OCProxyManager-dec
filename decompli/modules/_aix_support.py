# Module: _aix_support
# Pseudo-source reconstructed from bytecode (no decompiler)


def _aix_tag(vrtl, bd):
    ...

def _aix_vrtl(vrmf):
    ...

def _aix_bos_rte():
    """
    
        Return a Tuple[str, int] e.g., ['7.1.4.34', 1806]
        The fileset bos.rte represents the current AIX run-time level. It's VRMF and
        builddate reflect the current ABI levels of the runtime environment.
        If no builddate is found give a value that will satisfy pep425 related queries
        
    """
    ...

def aix_platform():
    """
    
        AIX filesets are identified by four decimal values: V.R.M.F.
        V (version) and R (release) can be retrieved using ``uname``
        Since 2007, starting with AIX 5.3 TL7, the M value has been
        included with the fileset bos.rte and represents the Technology
        Level (TL) of AIX. The F (Fix) value also increases, but is not
        relevant for comparing releases and binary compatibility.
        For binary compatibility the so-called builddate is needed.
        Again, the builddate of an AIX release is associated with bos.rte.
        AIX ABI compatibility is described  as guaranteed at: https://www.ibm.com/    support/knowledgecenter/en/ssw_aix_72/install/binary_compatability.html
    
        For pep425 purposes the AIX platform tag becomes:
        "aix-{:1x}{:1d}{:02d}-{:04d}-{}".format(v, r, tl, builddate, bitsize)
        e.g., "aix-6107-1415-32" for AIX 6.1 TL7 bd 1415, 32-bit
        and, "aix-6107-1415-64" for AIX 6.1 TL7 bd 1415, 64-bit
        
    """
    ...

def _aix_bgt():
    ...

def aix_buildtag():
    """
    
        Return the platform_tag of the system Python was built on.
        
    """
    ...
