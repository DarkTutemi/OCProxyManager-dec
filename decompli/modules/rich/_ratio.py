# Module: _ratio
# Pseudo-source reconstructed from bytecode (no decompiler)


def Edge():
    """Edge"""
    ...

def ratio_resolve(total, edges):
    """
    Divide total space to satisfy size, ratio, and minimum_size, constraints.
    
        The returned list of integers should add up to total in most cases, unless it is
        impossible to satisfy all the constraints. For instance, if there are two edges
        with a minimum size of 20 each and `total` is 30 then the returned list will be
        greater than total. In practice, this would mean that a Layout object would
        clip the rows that would overflow the screen height.
    
        Args:
            total (int): Total number of characters.
            edges (List[Edge]): Edges within total space.
    
        Returns:
            List[int]: Number of characters for each edge.
        
    """
    ...

def ratio_reduce(total, ratios, maximums, values):
    """
    Divide an integer total in to parts based on ratios.
    
        Args:
            total (int): The total to divide.
            ratios (List[int]): A list of integer ratios.
            maximums (List[int]): List of maximums values for each slot.
            values (List[int]): List of values
    
        Returns:
            List[int]: A list of integers guaranteed to sum to total.
        
    """
    ...

def ratio_distribute(total, ratios, minimums):
    """
    Distribute an integer total in to parts based on ratios.
    
        Args:
            total (int): The total to divide.
            ratios (List[int]): A list of integer ratios.
            minimums (List[int]): List of minimum values for each slot.
    
        Returns:
            List[int]: A list of integers guaranteed to sum to total.
        
    """
    ...

def E():
    """E"""
    ...
