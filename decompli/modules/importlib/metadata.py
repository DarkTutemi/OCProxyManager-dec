# Module: metadata
# Pseudo-source reconstructed from bytecode (no decompiler)


def PackageNotFoundError():
    """PackageNotFoundError"""
    ...

def Sectioned():
    """Sectioned"""
    ...

def DeprecatedTuple():
    """DeprecatedTuple"""
    ...

def EntryPoint():
    """EntryPoint"""
    ...

def DeprecatedList():
    """DeprecatedList"""
    ...

def EntryPoints():
    """EntryPoints"""
    ...

def Deprecated():
    """Deprecated"""
    ...

def SelectableGroups():
    """SelectableGroups"""
    ...

def PackagePath():
    """PackagePath"""
    ...

def FileHash():
    """FileHash"""
    ...

def Distribution():
    """Distribution"""
    ...

def DistributionFinder():
    """DistributionFinder"""
    ...

def FastPath():
    """FastPath"""
    ...

def Lookup():
    """Lookup"""
    ...

def Prepared():
    """Prepared"""
    ...

def MetadataPathFinder():
    """MetadataPathFinder"""
    ...

def PathDistribution():
    """PathDistribution"""
    ...

def distribution(distribution_name):
    """
    Get the ``Distribution`` instance for the named package.
    
        :param distribution_name: The name of the distribution package as a string.
        :return: A ``Distribution`` instance (or subclass thereof).
        
    """
    ...

def distributions(**kwargs):
    """
    Get all ``Distribution`` instances in the current environment.
    
        :return: An iterable of ``Distribution`` instances.
        
    """
    ...

def metadata(distribution_name):
    """
    Get the metadata for the named package.
    
        :param distribution_name: The name of the distribution package to query.
        :return: A PackageMetadata containing the parsed metadata.
        
    """
    ...

def version(distribution_name):
    """
    Get the version string for the named package.
    
        :param distribution_name: The name of the distribution package to query.
        :return: The version string for the package as defined in the package's
            "Version" metadata key.
        
    """
    ...

def entry_points(**params):
    """
    Return EntryPoint objects for all installed packages.
    
        Pass selection parameters (group or name) to filter the
        result to entry points matching those properties (see
        EntryPoints.select()).
    
        For compatibility, returns ``SelectableGroups`` object unless
        selection parameters are supplied. In the future, this function
        will return ``EntryPoints`` instead of ``SelectableGroups``
        even when no selection parameters are supplied.
    
        For maximum future compatibility, pass selection parameters
        or invoke ``.select`` with parameters on the result.
    
        :return: EntryPoints or SelectableGroups for all installed packages.
        
    """
    ...

def files(distribution_name):
    """
    Return a list of files for the named package.
    
        :param distribution_name: The name of the distribution package to query.
        :return: List of files composing the distribution.
        
    """
    ...

def requires(distribution_name):
    """
    
        Return a list of requirements for the named package.
    
        :return: An iterator of requirements, suitable for
            packaging.requirement.Requirement.
        
    """
    ...

def packages_distributions():
    """
    
        Return a mapping of top-level packages to their
        distributions.
    
        >>> import collections.abc
        >>> pkgs = packages_distributions()
        >>> all(isinstance(dist, collections.abc.Sequence) for dist in pkgs.values())
        True
        
    """
    ...

def _top_level_declared(dist):
    ...

def _top_level_inferred(dist):
    ...
