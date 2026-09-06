# Module: uuid
# Pseudo-source reconstructed from bytecode (no decompiler)


def SafeUUID():
    """SafeUUID"""
    ...

def UUID():
    """UUID"""
    ...

def _get_command_stdout(command, *args):
    ...

def _is_universal(mac):
    ...

def _find_mac_near_keyword(command, args, keywords, get_word_index):
    """
    Searches a command's output for a MAC address near a keyword.
    
        Each line of words in the output is case-insensitively searched for
        any of the given keywords.  Upon a match, get_word_index is invoked
        to pick a word from the line, given the index of the match.  For
        example, lambda i: 0 would get the first word on the line, while
        lambda i: i - 1 would get the word preceding the keyword.
        
    """
    ...

def _parse_mac(word):
    ...

def _find_mac_under_heading(command, args, heading):
    """
    Looks for a MAC address under a heading in a command's output.
    
        The first line of words in the output is searched for the given
        heading. Words at the same word index as the heading in subsequent
        lines are then examined to see if they look like MAC addresses.
        
    """
    ...

def _ifconfig_getnode():
    """Get the hardware address on Unix by running ifconfig."""
    ...

def _ip_getnode():
    """Get the hardware address on Unix by running ip."""
    ...

def _arp_getnode():
    """Get the hardware address on Unix by running arp."""
    ...

def _lanscan_getnode():
    """Get the hardware address on Unix by running lanscan."""
    ...

def _netstat_getnode():
    """Get the hardware address on Unix by running netstat."""
    ...

def _ipconfig_getnode():
    """[DEPRECATED] Get the hardware address on Windows."""
    ...

def _netbios_getnode():
    """[DEPRECATED] Get the hardware address on Windows."""
    ...

def _load_system_functions():
    """[DEPRECATED] Platform-specific functions loaded at import time"""
    ...

def _unix_getnode():
    """Get the hardware address on Unix using the _uuid extension module."""
    ...

def _windll_getnode():
    """Get the hardware address on Windows using the _uuid extension module."""
    ...

def _random_getnode():
    """Get a random node ID."""
    ...

def getnode():
    """
    Get the hardware address as a 48-bit positive integer.
    
        The first time this runs, it may launch a separate program, which could
        be quite slow.  If all attempts to obtain the hardware address fail, we
        choose a random 48-bit number with its eighth bit set to 1 as recommended
        in RFC 4122.
        
    """
    ...

def uuid1(node, clock_seq):
    """
    Generate a UUID from a host ID, sequence number, and the current time.
        If 'node' is not given, getnode() is used to obtain the hardware
        address.  If 'clock_seq' is given, it is used as the sequence number;
        otherwise a random 14-bit sequence number is chosen.
    """
    ...

def uuid3(namespace, name):
    """Generate a UUID from the MD5 hash of a namespace UUID and a name."""
    ...

def uuid4():
    """Generate a random UUID."""
    ...

def uuid5(namespace, name):
    """Generate a UUID from the SHA-1 hash of a namespace UUID and a name."""
    ...
