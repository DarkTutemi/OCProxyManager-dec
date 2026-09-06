# Module: dataclasses
# Pseudo-source reconstructed from bytecode (no decompiler)


def FrozenInstanceError():
    """FrozenInstanceError"""
    ...

def _HAS_DEFAULT_FACTORY_CLASS():
    """_HAS_DEFAULT_FACTORY_CLASS"""
    ...

def _MISSING_TYPE():
    """_MISSING_TYPE"""
    ...

def _KW_ONLY_TYPE():
    """_KW_ONLY_TYPE"""
    ...

def _FIELD_BASE():
    """_FIELD_BASE"""
    ...

def _recursive_repr(user_function):
    ...

def InitVar():
    """InitVar"""
    ...

def Field():
    """Field"""
    ...

def _DataclassParams():
    """_DataclassParams"""
    ...

def field(*, default=None, default_factory=None, init=None, repr=None, hash=None, compare=None, metadata=None, kw_only=None):
    """
    Return an object to identify dataclass fields.
    
        default is the default value of the field.  default_factory is a
        0-argument function called to initialize a field's value.  If init
        is true, the field will be a parameter to the class's __init__()
        function.  If repr is true, the field will be included in the
        object's repr().  If hash is true, the field will be included in the
        object's hash().  If compare is true, the field will be used in
        comparison functions.  metadata, if specified, must be a mapping
        which is stored but not otherwise examined by dataclass.  If kw_only
        is true, the field will become a keyword-only parameter to
        __init__().
    
        It is an error to specify both default and default_factory.
        
    """
    ...

def _fields_in_init_order(fields):
    ...

def _tuple_str(obj_name, fields):
    ...

def _create_fn(name, args, body, *, globals=None, locals=None, return_type=None):
    ...

def _field_assign(frozen, name, value, self_name):
    ...

def _field_init(f, frozen, globals, self_name, slots):
    ...

def _init_param(f):
    ...

def _init_fn(fields, std_fields, kw_only_fields, frozen, has_post_init, self_name, globals, slots):
    ...

def _repr_fn(fields, globals):
    ...

def _frozen_get_del_attr(cls, fields, globals):
    ...

def _cmp_fn(name, op, self_tuple, other_tuple, globals):
    ...

def _hash_fn(fields, globals):
    ...

def _is_classvar(a_type, typing):
    ...

def _is_initvar(a_type, dataclasses):
    ...

def _is_kw_only(a_type, dataclasses):
    ...

def _is_type(annotation, cls, a_module, a_type, is_type_predicate):
    ...

def _get_field(cls, a_name, a_type, default_kw_only):
    ...

def _set_qualname(cls, value):
    ...

def _set_new_attribute(cls, name, value):
    ...

def _hash_set_none(cls, fields, globals):
    ...

def _hash_add(cls, fields, globals):
    ...

def _hash_exception(cls, fields, globals):
    ...

def _process_class(cls, init, repr, eq, order, unsafe_hash, frozen, match_args, kw_only, slots, weakref_slot):
    ...

def _dataclass_getstate(self):
    ...

def _dataclass_setstate(self, state):
    ...

def _get_slots(cls):
    import __dict__

def _add_slots(cls, is_frozen, weakref_slot):
    ...

def dataclass(cls, *, init=None, repr=None, eq=None, order=None, unsafe_hash=None, frozen=None, match_args=None, kw_only=None, slots=None, weakref_slot=None):
    """
    Add dunder methods based on the fields defined in the class.
    
        Examines PEP 526 __annotations__ to determine fields.
    
        If init is true, an __init__() method is added to the class. If repr
        is true, a __repr__() method is added. If order is true, rich
        comparison dunder methods are added. If unsafe_hash is true, a
        __hash__() method is added. If frozen is true, fields may not be
        assigned to after instance creation. If match_args is true, the
        __match_args__ tuple is added. If kw_only is true, then by default
        all fields are keyword-only. If slots is true, a new class with a
        __slots__ attribute is returned.
        
    """
    ...

def fields(class_or_instance):
    """
    Return a tuple describing the fields of this dataclass.
    
        Accepts a dataclass or an instance of one. Tuple elements are of
        type Field.
        
    """
    ...

def _is_dataclass_instance(obj):
    """Returns True if obj is an instance of a dataclass."""
    ...

def is_dataclass(obj):
    """
    Returns True if obj is a dataclass or an instance of a
        dataclass.
    """
    ...

def asdict(obj, *, dict_factory=None):
    """
    Return the fields of a dataclass instance as a new dictionary mapping
        field names to field values.
    
        Example usage::
    
          @dataclass
          class C:
              x: int
              y: int
    
          c = C(1, 2)
          assert asdict(c) == {'x': 1, 'y': 2}
    
        If given, 'dict_factory' will be used instead of built-in dict.
        The function applies recursively to field values that are
        dataclass instances. This will also look into built-in containers:
        tuples, lists, and dicts.
        
    """
    ...

def _asdict_inner(obj, dict_factory):
    ...

def astuple(obj, *, tuple_factory=None):
    """
    Return the fields of a dataclass instance as a new tuple of field values.
    
        Example usage::
    
          @dataclass
          class C:
              x: int
              y: int
    
          c = C(1, 2)
          assert astuple(c) == (1, 2)
    
        If given, 'tuple_factory' will be used instead of built-in tuple.
        The function applies recursively to field values that are
        dataclass instances. This will also look into built-in containers:
        tuples, lists, and dicts.
        
    """
    ...

def _astuple_inner(obj, tuple_factory):
    ...

def make_dataclass(cls_name, fields, *, bases=None, namespace=None, init=None, repr=None, eq=None, order=None, unsafe_hash=None, frozen=None, match_args=None, kw_only=None, slots=None, weakref_slot=None):
    """
    Return a new dynamically created dataclass.
    
        The dataclass name will be 'cls_name'.  'fields' is an iterable
        of either (name), (name, type) or (name, type, Field) objects. If type is
        omitted, use the string 'typing.Any'.  Field objects are created by
        the equivalent of calling 'field(name, type [, Field-info])'.::
    
          C = make_dataclass('C', ['x', ('y', int), ('z', int, field(init=False))], bases=(Base,))
    
        is equivalent to::
    
          @dataclass
          class C(Base):
              x: 'typing.Any'
              y: int
              z: int = field(init=False)
    
        For the bases and namespace parameters, see the builtin type() function.
    
        The parameters init, repr, eq, order, unsafe_hash, and frozen are passed to
        dataclass().
        
    """
    ...

def replace(obj, **changes):
    """
    Return a new object replacing specified fields with new values.
    
        This is especially useful for frozen classes.  Example usage::
    
          @dataclass(frozen=True)
          class C:
              x: int
              y: int
    
          c = C(1, 2)
          c1 = replace(c, x=3)
          assert c1.x == 3 and c1.y == 2
        
    """
    ...
