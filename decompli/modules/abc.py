# Module: abc
# Pseudo-source reconstructed from bytecode (no decompiler)


def abstractmethod(funcobj):
    """
    A decorator indicating abstract methods.
    
        Requires that the metaclass is ABCMeta or derived from it.  A
        class that has a metaclass derived from ABCMeta cannot be
        instantiated unless all of its abstract methods are overridden.
        The abstract methods can be called using any of the normal
        'super' call mechanisms.  abstractmethod() may be used to declare
        abstract methods for properties and descriptors.
    
        Usage:
    
            class C(metaclass=ABCMeta):
                @abstractmethod
                def my_abstract_method(self, arg1, arg2, argN):
                    ...
        
    """
    ...

def abstractclassmethod():
    """abstractclassmethod"""
    ...

def abstractstaticmethod():
    """abstractstaticmethod"""
    ...

def abstractproperty():
    """abstractproperty"""
    ...

def ABCMeta():
    """ABCMeta"""
    ...

def update_abstractmethods(cls):
    """
    Recalculate the set of abstract methods of an abstract class.
    
        If a class has had one of its abstract methods implemented after the
        class was created, the method will not be considered implemented until
        this function is called. Alternatively, if a new abstract method has been
        added to the class, it will only be considered an abstract method of the
        class after this function is called.
    
        This function should be called before any use is made of the class,
        usually in class decorators that add methods to the subject class.
    
        Returns cls, to allow usage as a class decorator.
    
        If cls is not an instance of ABCMeta, does nothing.
        
    """
    ...

def ABC():
    """ABC"""
    ...
