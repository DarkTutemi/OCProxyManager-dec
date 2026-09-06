# Module: ipaddress
# Pseudo-source reconstructed from bytecode (no decompiler)


def AddressValueError():
    """AddressValueError"""
    ...

def NetmaskValueError():
    """NetmaskValueError"""
    ...

def ip_address(address):
    """
    Take an IP string/int and return an object of the correct type.
    
        Args:
            address: A string or integer, the IP address.  Either IPv4 or
              IPv6 addresses may be supplied; integers less than 2**32 will
              be considered to be IPv4 by default.
    
        Returns:
            An IPv4Address or IPv6Address object.
    
        Raises:
            ValueError: if the *address* passed isn't either a v4 or a v6
              address
    
        
    """
    ...

def ip_network(address, strict):
    """
    Take an IP string/int and return an object of the correct type.
    
        Args:
            address: A string or integer, the IP network.  Either IPv4 or
              IPv6 networks may be supplied; integers less than 2**32 will
              be considered to be IPv4 by default.
    
        Returns:
            An IPv4Network or IPv6Network object.
    
        Raises:
            ValueError: if the string passed isn't either a v4 or a v6
              address. Or if the network has host bits set.
    
        
    """
    ...

def ip_interface(address):
    """
    Take an IP string/int and return an object of the correct type.
    
        Args:
            address: A string or integer, the IP address.  Either IPv4 or
              IPv6 addresses may be supplied; integers less than 2**32 will
              be considered to be IPv4 by default.
    
        Returns:
            An IPv4Interface or IPv6Interface object.
    
        Raises:
            ValueError: if the string passed isn't either a v4 or a v6
              address.
    
        Notes:
            The IPv?Interface classes describe an Address on a particular
            Network, so they're basically a combination of both the Address
            and Network classes.
    
        
    """
    ...

def v4_int_to_packed(address):
    """
    Represent an address as 4 packed bytes in network (big-endian) order.
    
        Args:
            address: An integer representation of an IPv4 IP address.
    
        Returns:
            The integer address packed as 4 bytes in network (big-endian) order.
    
        Raises:
            ValueError: If the integer is negative or too large to be an
              IPv4 IP address.
    
        
    """
    ...

def v6_int_to_packed(address):
    """
    Represent an address as 16 packed bytes in network (big-endian) order.
    
        Args:
            address: An integer representation of an IPv6 IP address.
    
        Returns:
            The integer address packed as 16 bytes in network (big-endian) order.
    
        
    """
    ...

def _split_optional_netmask(address):
    """Helper to split the netmask and raise AddressValueError if needed"""
    ...

def _find_address_range(addresses):
    """
    Find a sequence of sorted deduplicated IPv#Address.
    
        Args:
            addresses: a list of IPv#Address objects.
    
        Yields:
            A tuple containing the first and last IP addresses in the sequence.
    
        
    """
    ...

def _count_righthand_zero_bits(number, bits):
    """
    Count the number of zero bits on the right hand side.
    
        Args:
            number: an integer.
            bits: maximum number of bits to count.
    
        Returns:
            The number of zero bits on the right hand side of the number.
    
        
    """
    ...

def summarize_address_range(first, last):
    """
    Summarize a network range given the first and last IP addresses.
    
        Example:
            >>> list(summarize_address_range(IPv4Address('192.0.2.0'),
            ...                              IPv4Address('192.0.2.130')))
            ...                                #doctest: +NORMALIZE_WHITESPACE
            [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'),
             IPv4Network('192.0.2.130/32')]
    
        Args:
            first: the first IPv4Address or IPv6Address in the range.
            last: the last IPv4Address or IPv6Address in the range.
    
        Returns:
            An iterator of the summarized IPv(4|6) network objects.
    
        Raise:
            TypeError:
                If the first and last objects are not IP addresses.
                If the first and last objects are not the same version.
            ValueError:
                If the last object is not greater than the first.
                If the version of the first address is not 4 or 6.
    
        
    """
    ...

def _collapse_addresses_internal(addresses):
    """
    Loops through the addresses, collapsing concurrent netblocks.
    
        Example:
    
            ip1 = IPv4Network('192.0.2.0/26')
            ip2 = IPv4Network('192.0.2.64/26')
            ip3 = IPv4Network('192.0.2.128/26')
            ip4 = IPv4Network('192.0.2.192/26')
    
            _collapse_addresses_internal([ip1, ip2, ip3, ip4]) ->
              [IPv4Network('192.0.2.0/24')]
    
            This shouldn't be called directly; it is called via
              collapse_addresses([]).
    
        Args:
            addresses: A list of IPv4Network's or IPv6Network's
    
        Returns:
            A list of IPv4Network's or IPv6Network's depending on what we were
            passed.
    
        
    """
    ...

def collapse_addresses(addresses):
    """
    Collapse a list of IP objects.
    
        Example:
            collapse_addresses([IPv4Network('192.0.2.0/25'),
                                IPv4Network('192.0.2.128/25')]) ->
                               [IPv4Network('192.0.2.0/24')]
    
        Args:
            addresses: An iterator of IPv4Network or IPv6Network objects.
    
        Returns:
            An iterator of the collapsed IPv(4|6)Network objects.
    
        Raises:
            TypeError: If passed a list of mixed version objects.
    
        
    """
    ...

def get_mixed_type_key(obj):
    """
    Return a key suitable for sorting between networks and addresses.
    
        Address and Network objects are not sortable by default; they're
        fundamentally different so the expression
    
            IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')
    
        doesn't make any sense.  There are some times however, where you may wish
        to have ipaddress sort these for you anyway. If you need to do this, you
        can use this function as the key= argument to sorted().
    
        Args:
          obj: either a Network or Address object.
        Returns:
          appropriate key.
    
        
    """
    ...

def _IPAddressBase():
    """_IPAddressBase"""
    ...

def _BaseAddress():
    """_BaseAddress"""
    ...

def _BaseNetwork():
    """_BaseNetwork"""
    ...

def _BaseConstants():
    """_BaseConstants"""
    ...

def _BaseV4():
    """_BaseV4"""
    ...

def IPv4Address():
    """IPv4Address"""
    ...

def IPv4Interface():
    """IPv4Interface"""
    ...

def IPv4Network():
    """IPv4Network"""
    ...

def _IPv4Constants():
    """_IPv4Constants"""
    ...

def _BaseV6():
    """_BaseV6"""
    ...

def IPv6Address():
    """IPv6Address"""
    ...

def IPv6Interface():
    """IPv6Interface"""
    ...

def IPv6Network():
    """IPv6Network"""
    ...

def _IPv6Constants():
    """_IPv6Constants"""
    ...
