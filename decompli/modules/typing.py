# Module: typing
# Pseudo-source reconstructed from bytecode (no decompiler)


def _idfunc(_, x):
    ...

def _type_convert(arg, module, *, allow_special_forms=None):
    """For converting None to type(None), and strings to ForwardRef."""
    ...

def _type_check(arg, msg, is_argument, module, *, allow_special_forms=None):
    """
    Check that the argument is a type, and return it (internal helper).
    
        As a special case, accept None and return type(None) instead. Also wrap strings
        into ForwardRef instances. Consider several corner cases, for example plain
        special forms like Union are not valid, while Union[int, str] is OK, etc.
        The msg argument is a human-readable error message, e.g.::
    
            "Union[arg, ...]: arg should be a type."
    
        We append the repr() of the actual value (truncated to 100 chars).
        
    """
    ...

def _is_param_expr(arg):
    ...

def _should_unflatten_callable_args(typ, args):
    """
    Internal helper for munging collections.abc.Callable's __args__.
    
        The canonical representation for a Callable's __args__ flattens the
        argument types, see https://github.com/python/cpython/issues/86361.
    
        For example::
    
            >>> import collections.abc
            >>> P = ParamSpec('P')
            >>> collections.abc.Callable[[int, int], str].__args__ == (int, int, str)
            True
            >>> collections.abc.Callable[P, str].__args__ == (P, str)
            True
    
        As a result, if we need to reconstruct the Callable from its __args__,
        we need to unflatten it.
        
    """
    ...

def _type_repr(obj):
    """
    Return the repr() of an object, special-casing types (internal helper).
    
        If obj is a type, we return a shorter version than the default
        type.__repr__, based on the module and qualified name, which is
        typically enough to uniquely identify a type.  For everything
        else, we fall back on repr(obj).
        
    """
    ...

def _collect_parameters(args):
    """
    Collect all type variables and parameter specifications in args
        in order of first appearance (lexicographic order).
    
        For example::
    
            >>> P = ParamSpec('P')
            >>> T = TypeVar('T')
            >>> _collect_parameters((T, Callable[P, T]))
            (~T, ~P)
        
    """
    ...

def _check_generic(cls, parameters, elen):
    """
    Check correct count for parameters of a generic cls (internal helper).
    
        This gives a nice error message in case of count mismatch.
        
    """
    ...

def _unpack_args(args):
    ...

def _deduplicate(params, *, unhashable_fallback=None):
    ...

def _deduplicate_unhashable(unhashable_params):
    ...

def _compare_args_orderless(first_args, second_args):
    ...

def _remove_dups_flatten(parameters):
    """
    Internal helper for Union creation and substitution.
    
        Flatten Unions among parameters, then remove duplicates.
        
    """
    ...

def _flatten_literal_params(parameters):
    """Internal helper for Literal creation: flatten Literals among parameters."""
    ...

def _tp_cache(func, *, typed=None):
    """
    Internal wrapper caching __getitem__ of generic types.
    
        For non-hashable arguments, the original function is used as a fallback.
        
    """
    ...

def _eval_type(t, globalns, localns, recursive_guard):
    """
    Evaluate all forward references in the given type t.
    
        For use of globalns and localns see the docstring for get_type_hints().
        recursive_guard is used to prevent infinite recursion with a recursive
        ForwardRef.
        
    """
    ...

def _Final():
    """_Final"""
    ...

def _Immutable():
    """_Immutable"""
    ...

def _NotIterable():
    """_NotIterable"""
    ...

def _SpecialForm():
    """_SpecialForm"""
    ...

def _LiteralSpecialForm():
    """_LiteralSpecialForm"""
    ...

def _AnyMeta():
    """_AnyMeta"""
    ...

def Any():
    """Any"""
    ...

def NoReturn(self, parameters):
    """
    Special type indicating functions that never return.
    
        Example::
    
            from typing import NoReturn
    
            def stop() -> NoReturn:
                raise Exception('no way')
    
        NoReturn can also be used as a bottom type, a type that
        has no values. Starting in Python 3.11, the Never type should
        be used for this concept instead. Type checkers should treat the two
        equivalently.
        
    """
    ...

def Never(self, parameters):
    """
    The bottom type, a type that has no members.
    
        This can be used to define a function that should never be
        called, or a function that never returns::
    
            from typing import Never
    
            def never_call_me(arg: Never) -> None:
                pass
    
            def int_or_str(arg: int | str) -> None:
                never_call_me(arg)  # type checker error
                match arg:
                    case int():
                        print("It's an int")
                    case str():
                        print("It's a str")
                    case _:
                        never_call_me(arg)  # OK, arg is of type Never
        
    """
    ...

def Self(self, parameters):
    """
    Used to spell the type of "self" in classes.
    
        Example::
    
            from typing import Self
    
            class Foo:
                def return_self(self) -> Self:
                    ...
                    return self
    
        This is especially useful for:
            - classmethods that are used as alternative constructors
            - annotating an `__enter__` method which returns self
        
    """
    ...

def LiteralString(self, parameters):
    """
    Represents an arbitrary literal string.
    
        Example::
    
            from typing import LiteralString
    
            def run_query(sql: LiteralString) -> None:
                ...
    
            def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
                run_query("SELECT * FROM students")  # OK
                run_query(literal_string)  # OK
                run_query("SELECT * FROM " + literal_string)  # OK
                run_query(arbitrary_string)  # type checker error
                run_query(  # type checker error
                    f"SELECT * FROM students WHERE name = {arbitrary_string}"
                )
    
        Only string literals and other LiteralStrings are compatible
        with LiteralString. This provides a tool to help prevent
        security issues such as SQL injection.
        
    """
    ...

def ClassVar(self, parameters):
    """
    Special type construct to mark class variables.
    
        An annotation wrapped in ClassVar indicates that a given
        attribute is intended to be used as a class variable and
        should not be set on instances of that class.
    
        Usage::
    
            class Starship:
                stats: ClassVar[dict[str, int]] = {} # class variable
                damage: int = 10                     # instance variable
    
        ClassVar accepts only types and cannot be further subscribed.
    
        Note that ClassVar is not a class itself, and should not
        be used with isinstance() or issubclass().
        
    """
    ...

def Final(self, parameters):
    """
    Special typing construct to indicate final names to type checkers.
    
        A final name cannot be re-assigned or overridden in a subclass.
    
        For example::
    
            MAX_SIZE: Final = 9000
            MAX_SIZE += 1  # Error reported by type checker
    
            class Connection:
                TIMEOUT: Final[int] = 10
    
            class FastConnector(Connection):
                TIMEOUT = 1  # Error reported by type checker
    
        There is no runtime checking of these properties.
        
    """
    ...

def Union(self, parameters):
    """
    Union type; Union[X, Y] means either X or Y.
    
        On Python 3.10 and higher, the | operator
        can also be used to denote unions;
        X | Y means the same thing to the type checker as Union[X, Y].
    
        To define a union, use e.g. Union[int, str]. Details:
        - The arguments must be types and there must be at least one.
        - None as an argument is a special case and is replaced by
          type(None).
        - Unions of unions are flattened, e.g.::
    
            assert Union[Union[int, str], float] == Union[int, str, float]
    
        - Unions of a single argument vanish, e.g.::
    
            assert Union[int] == int  # The constructor actually returns int
    
        - Redundant arguments are skipped, e.g.::
    
            assert Union[int, str, int] == Union[int, str]
    
        - When comparing unions, the argument order is ignored, e.g.::
    
            assert Union[int, str] == Union[str, int]
    
        - You cannot subclass or instantiate a union.
        - You can use Optional[X] as a shorthand for Union[X, None].
        
    """
    ...

def Optional(self, parameters):
    """Optional[X] is equivalent to Union[X, None]."""
    ...

def Literal(self, *parameters):
    """
    Special typing form to define literal types (a.k.a. value types).
    
        This form can be used to indicate to type checkers that the corresponding
        variable or function parameter has a value equivalent to the provided
        literal (or one of several literals)::
    
            def validate_simple(data: Any) -> Literal[True]:  # always returns True
                ...
    
            MODE = Literal['r', 'rb', 'w', 'wb']
            def open_helper(file: str, mode: MODE) -> str:
                ...
    
            open_helper('/some/path', 'r')  # Passes type check
            open_helper('/other/path', 'typo')  # Error in type checker
    
        Literal[...] cannot be subclassed. At runtime, an arbitrary value
        is allowed as type argument to Literal[...], but type checkers may
        impose restrictions.
        
    """
    ...

def TypeAlias(self, parameters):
    """
    Special form for marking type aliases.
    
        Use TypeAlias to indicate that an assignment should
        be recognized as a proper type alias definition by type
        checkers.
    
        For example::
    
            Predicate: TypeAlias = Callable[..., bool]
    
        It's invalid when used anywhere except as in the example above.
        
    """
    ...

def Concatenate(self, parameters):
    """
    Special form for annotating higher-order functions.
    
        ``Concatenate`` can be used in conjunction with ``ParamSpec`` and
        ``Callable`` to represent a higher-order function which adds, removes or
        transforms the parameters of a callable.
    
        For example::
    
            Callable[Concatenate[int, P], int]
    
        See PEP 612 for detailed information.
        
    """
    ...

def TypeGuard(self, parameters):
    """
    Special typing construct for marking user-defined type guard functions.
    
        ``TypeGuard`` can be used to annotate the return type of a user-defined
        type guard function.  ``TypeGuard`` only accepts a single type argument.
        At runtime, functions marked this way should return a boolean.
    
        ``TypeGuard`` aims to benefit *type narrowing* -- a technique used by static
        type checkers to determine a more precise type of an expression within a
        program's code flow.  Usually type narrowing is done by analyzing
        conditional code flow and applying the narrowing to a block of code.  The
        conditional expression here is sometimes referred to as a "type guard".
    
        Sometimes it would be convenient to use a user-defined boolean function
        as a type guard.  Such a function should use ``TypeGuard[...]`` as its
        return type to alert static type checkers to this intention.
    
        Using  ``-> TypeGuard`` tells the static type checker that for a given
        function:
    
        1. The return value is a boolean.
        2. If the return value is ``True``, the type of its argument
           is the type inside ``TypeGuard``.
    
           For example::
    
               def is_str(val: Union[str, float]):
                   # "isinstance" type guard
                   if isinstance(val, str):
                       # Type of ``val`` is narrowed to ``str``
                       ...
                   else:
                       # Else, type of ``val`` is narrowed to ``float``.
                       ...
    
        Strict type narrowing is not enforced -- ``TypeB`` need not be a narrower
        form of ``TypeA`` (it can even be a wider form) and this may lead to
        type-unsafe results.  The main reason is to allow for things like
        narrowing ``List[object]`` to ``List[str]`` even though the latter is not
        a subtype of the former, since ``List`` is invariant.  The responsibility of
        writing type-safe type guards is left to the user.
    
        ``TypeGuard`` also works with type variables.  For more information, see
        PEP 647 (User-Defined Type Guards).
        
    """
    ...

def ForwardRef():
    """ForwardRef"""
    ...

def _is_unpacked_typevartuple(x):
    ...

def _is_typevar_like(x):
    ...

def _PickleUsingNameMixin():
    """_PickleUsingNameMixin"""
    ...

def _BoundVarianceMixin():
    """_BoundVarianceMixin"""
    ...

def TypeVar():
    """TypeVar"""
    ...

def TypeVarTuple():
    """TypeVarTuple"""
    ...

def ParamSpecArgs():
    """ParamSpecArgs"""
    ...

def ParamSpecKwargs():
    """ParamSpecKwargs"""
    ...

def ParamSpec():
    """ParamSpec"""
    ...

def _is_dunder(attr):
    ...

def _BaseGenericAlias():
    """_BaseGenericAlias"""
    ...

def _GenericAlias():
    """_GenericAlias"""
    ...

def _SpecialGenericAlias():
    """_SpecialGenericAlias"""
    ...

def _CallableGenericAlias():
    """_CallableGenericAlias"""
    ...

def _CallableType():
    """_CallableType"""
    ...

def _TupleType():
    """_TupleType"""
    ...

def _UnionGenericAlias():
    """_UnionGenericAlias"""
    ...

def _value_and_type_iter(parameters):
    ...

def _LiteralGenericAlias():
    """_LiteralGenericAlias"""
    ...

def _ConcatenateGenericAlias():
    """_ConcatenateGenericAlias"""
    ...

def Unpack(self, parameters):
    """
    Type unpack operator.
    
        The type unpack operator takes the child types from some container type,
        such as `tuple[int, str]` or a `TypeVarTuple`, and 'pulls them out'.
    
        For example::
    
            # For some generic class `Foo`:
            Foo[Unpack[tuple[int, str]]]  # Equivalent to Foo[int, str]
    
            Ts = TypeVarTuple('Ts')
            # Specifies that `Bar` is generic in an arbitrary number of types.
            # (Think of `Ts` as a tuple of an arbitrary number of individual
            #  `TypeVar`s, which the `Unpack` is 'pulling out' directly into the
            #  `Generic[]`.)
            class Bar(Generic[Unpack[Ts]]): ...
            Bar[int]  # Valid
            Bar[int, str]  # Also valid
    
        From Python 3.11, this can also be done using the `*` operator::
    
            Foo[*tuple[int, str]]
            class Bar(Generic[*Ts]): ...
    
        Note that there is only some runtime checking of this operator. Not
        everything the runtime allows may be accepted by static type checkers.
    
        For more information, see PEP 646.
        
    """
    ...

def _UnpackGenericAlias():
    """_UnpackGenericAlias"""
    ...

def Generic():
    """Generic"""
    ...

def _TypingEllipsis():
    """_TypingEllipsis"""
    ...

def _get_protocol_attrs(cls):
    """
    Collect protocol members from a protocol class objects.
    
        This includes names actually defined in the class dictionary, as well
        as names that appear in annotations. Special names (above) are skipped.
        
    """
    ...

def _is_callable_members_only(cls):
    ...

def _no_init_or_replace_init(self, *args, **kwargs):
    ...

def _caller(depth, default):
    ...

def _allow_reckless_class_checks(depth):
    """
    Allow instance and class checks for special stdlib modules.
    
        The abc and functools modules indiscriminately call isinstance() and
        issubclass() on the whole MRO of a user class, which may contain protocols.
        
    """
    ...

def _ProtocolMeta():
    """_ProtocolMeta"""
    ...

def Protocol():
    """Protocol"""
    ...

def _AnnotatedAlias():
    """_AnnotatedAlias"""
    ...

def Annotated():
    """Annotated"""
    ...

def runtime_checkable(cls):
    """
    Mark a protocol class as a runtime protocol.
    
        Such protocol can be used with isinstance() and issubclass().
        Raise TypeError if applied to a non-protocol class.
        This allows a simple-minded structural check very similar to
        one trick ponies in collections.abc such as Iterable.
    
        For example::
    
            @runtime_checkable
            class Closable(Protocol):
                def close(self): ...
    
            assert isinstance(open('/some/file'), Closable)
    
        Warning: this will check only the presence of the required methods,
        not their type signatures!
        
    """
    ...

def cast(typ, val):
    """
    Cast a value to a type.
    
        This returns the value unchanged.  To the type checker this
        signals that the return value has the designated type, but at
        runtime we intentionally don't check anything (we want this
        to be as fast as possible).
        
    """
    ...

def assert_type(val, typ):
    """
    Ask a static type checker to confirm that the value is of the given type.
    
        At runtime this does nothing: it returns the first argument unchanged with no
        checks or side effects, no matter the actual type of the argument.
    
        When a static type checker encounters a call to assert_type(), it
        emits an error if the value is not of the specified type::
    
            def greet(name: str) -> None:
                assert_type(name, str)  # OK
                assert_type(name, int)  # type checker error
        
    """
    ...

def get_type_hints(obj, globalns, localns, include_extras):
    """
    Return type hints for an object.
    
        This is often the same as obj.__annotations__, but it handles
        forward references encoded as string literals and recursively replaces all
        'Annotated[T, ...]' with 'T' (unless 'include_extras=True').
    
        The argument may be a module, class, method, or function. The annotations
        are returned as a dictionary. For classes, annotations include also
        inherited members.
    
        TypeError is raised if the argument is not of a type that can contain
        annotations, and an empty dictionary is returned if no annotations are
        present.
    
        BEWARE -- the behavior of globalns and localns is counterintuitive
        (unless you are familiar with how eval() and exec() work).  The
        search order is locals first, then globals.
    
        - If no dict arguments are passed, an attempt is made to use the
          globals from obj (or the respective module's globals for classes),
          and these are also used as the locals.  If the object does not appear
          to have globals, an empty dictionary is used.  For classes, the search
          order is globals first then locals.
    
        - If one dict argument is passed, it is used for both globals and
          locals.
    
        - If two dict arguments are passed, they specify globals and
          locals, respectively.
        
    """
    ...

def _strip_annotations(t):
    """Strip the annotations from a given type."""
    ...

def get_origin(tp):
    """
    Get the unsubscripted version of a type.
    
        This supports generic types, Callable, Tuple, Union, Literal, Final, ClassVar,
        Annotated, and others. Return None for unsupported types.
    
        Examples::
    
            >>> P = ParamSpec('P')
            >>> assert get_origin(Literal[42]) is Literal
            >>> assert get_origin(int) is None
            >>> assert get_origin(ClassVar[int]) is ClassVar
            >>> assert get_origin(Generic) is Generic
            >>> assert get_origin(Generic[T]) is Generic
            >>> assert get_origin(Union[T, int]) is Union
            >>> assert get_origin(List[Tuple[T, T]][int]) is list
            >>> assert get_origin(P.args) is P
        
    """
    ...

def get_args(tp):
    """
    Get type arguments with all substitutions performed.
    
        For unions, basic simplifications used by Union constructor are performed.
    
        Examples::
    
            >>> T = TypeVar('T')
            >>> assert get_args(Dict[str, int]) == (str, int)
            >>> assert get_args(int) == ()
            >>> assert get_args(Union[int, Union[T, int], str][int]) == (int, str)
            >>> assert get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
            >>> assert get_args(Callable[[], T][int]) == ([], int)
        
    """
    ...

def is_typeddict(tp):
    """
    Check if an annotation is a TypedDict class.
    
        For example::
    
            >>> from typing import TypedDict
            >>> class Film(TypedDict):
            ...     title: str
            ...     year: int
            ...
            >>> is_typeddict(Film)
            True
            >>> is_typeddict(dict)
            False
        
    """
    ...

def assert_never(arg):
    """
    Statically assert that a line of code is unreachable.
    
        Example::
    
            def int_or_str(arg: int | str) -> None:
                match arg:
                    case int():
                        print("It's an int")
                    case str():
                        print("It's a str")
                    case _:
                        assert_never(arg)
    
        If a type checker finds that a call to assert_never() is
        reachable, it will emit an error.
    
        At runtime, this throws an exception when called.
        
    """
    ...

def no_type_check(arg):
    """
    Decorator to indicate that annotations are not type hints.
    
        The argument must be a class or function; if it is a class, it
        applies recursively to all methods and classes defined in that class
        (but not to methods defined in its superclasses or subclasses).
    
        This mutates the function(s) or class(es) in place.
        
    """
    ...

def no_type_check_decorator(decorator):
    """
    Decorator to give another decorator the @no_type_check effect.
    
        This wraps the decorator with something that wraps the decorated
        function in @no_type_check.
        
    """
    ...

def _overload_dummy(*args, **kwds):
    """Helper for @overload to raise when called."""
    ...

def overload(func):
    """
    Decorator for overloaded functions/methods.
    
        In a stub file, place two or more stub definitions for the same
        function in a row, each decorated with @overload.
    
        For example::
    
            @overload
            def utf8(value: None) -> None: ...
            @overload
            def utf8(value: bytes) -> bytes: ...
            @overload
            def utf8(value: str) -> bytes: ...
    
        In a non-stub file (i.e. a regular .py file), do the same but
        follow it with an implementation.  The implementation should *not*
        be decorated with @overload::
    
            @overload
            def utf8(value: None) -> None: ...
            @overload
            def utf8(value: bytes) -> bytes: ...
            @overload
            def utf8(value: str) -> bytes: ...
            def utf8(value):
                ...  # implementation goes here
    
        The overloads for a function can be retrieved at runtime using the
        get_overloads() function.
        
    """
    ...

def get_overloads(func):
    """Return all defined overloads for *func* as a sequence."""
    ...

def clear_overloads():
    """Clear all overloads in the registry."""
    ...

def final(f):
    """
    Decorator to indicate final methods and final classes.
    
        Use this decorator to indicate to type checkers that the decorated
        method cannot be overridden, and decorated class cannot be subclassed.
    
        For example::
    
            class Base:
                @final
                def done(self) -> None:
                    ...
            class Sub(Base):
                def done(self) -> None:  # Error reported by type checker
                    ...
    
            @final
            class Leaf:
                ...
            class Other(Leaf):  # Error reported by type checker
                ...
    
        There is no runtime checking of these properties. The decorator
        attempts to set the ``__final__`` attribute to ``True`` on the decorated
        object to allow runtime introspection.
        
    """
    ...

def SupportsInt():
    """SupportsInt"""
    ...

def SupportsFloat():
    """SupportsFloat"""
    ...

def SupportsComplex():
    """SupportsComplex"""
    ...

def SupportsBytes():
    """SupportsBytes"""
    ...

def SupportsIndex():
    """SupportsIndex"""
    ...

def SupportsAbs():
    """SupportsAbs"""
    ...

def SupportsRound():
    """SupportsRound"""
    ...

def _make_nmtuple(name, types, module, defaults):
    ...

def NamedTupleMeta():
    """NamedTupleMeta"""
    ...

def NamedTuple(typename, fields, **kwargs):
    """
    Typed version of namedtuple.
    
        Usage::
    
            class Employee(NamedTuple):
                name: str
                id: int
    
        This is equivalent to::
    
            Employee = collections.namedtuple('Employee', ['name', 'id'])
    
        The resulting class has an extra __annotations__ attribute, giving a
        dict that maps field names to types.  (The field names are also in
        the _fields attribute, which is part of the namedtuple API.)
        An alternative equivalent functional syntax is also accepted::
    
            Employee = NamedTuple('Employee', [('name', str), ('id', int)])
        
    """
    ...

def _namedtuple_mro_entries(bases):
    ...

def _TypedDictMeta():
    """_TypedDictMeta"""
    ...

def TypedDict(typename, fields, *, total=None, **kwargs):
    """
    A simple typed namespace. At runtime it is equivalent to a plain dict.
    
        TypedDict creates a dictionary type such that a type checker will expect all
        instances to have a certain set of keys, where each key is
        associated with a value of a consistent type. This expectation
        is not checked at runtime.
    
        Usage::
    
            >>> class Point2D(TypedDict):
            ...     x: int
            ...     y: int
            ...     label: str
            ...
            >>> a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
            >>> b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check
            >>> Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
            True
    
        The type info can be accessed via the Point2D.__annotations__ dict, and
        the Point2D.__required_keys__ and Point2D.__optional_keys__ frozensets.
        TypedDict supports an additional equivalent form::
    
            Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})
    
        By default, all keys must be present in a TypedDict. It is possible
        to override this by specifying totality::
    
            class Point2D(TypedDict, total=False):
                x: int
                y: int
    
        This means that a Point2D TypedDict can have any of the keys omitted. A type
        checker is only expected to support a literal False or True as the value of
        the total argument. True is the default, and makes all items defined in the
        class body be required.
    
        The Required and NotRequired special forms can also be used to mark
        individual keys as being required or not required::
    
            class Point2D(TypedDict):
                x: int               # the "x" key must always be present (Required is the default)
                y: NotRequired[int]  # the "y" key can be omitted
    
        See PEP 655 for more details on Required and NotRequired.
        
    """
    ...

def Required(self, parameters):
    """
    Special typing construct to mark a TypedDict key as required.
    
        This is mainly useful for total=False TypedDicts.
    
        For example::
    
            class Movie(TypedDict, total=False):
                title: Required[str]
                year: int
    
            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )
    
        There is no runtime checking that a required key is actually provided
        when instantiating a related TypedDict.
        
    """
    ...

def NotRequired(self, parameters):
    """
    Special typing construct to mark a TypedDict key as potentially missing.
    
        For example::
    
            class Movie(TypedDict):
                title: str
                year: NotRequired[int]
    
            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )
        
    """
    ...

def NewType():
    """NewType"""
    ...

def IO():
    """IO"""
    ...

def BinaryIO():
    """BinaryIO"""
    ...

def TextIO():
    """TextIO"""
    ...

def _DeprecatedType():
    """_DeprecatedType"""
    ...

def io():
    """io"""
    ...

def re():
    """re"""
    ...

def reveal_type(obj):
    """
    Ask a static type checker to reveal the inferred type of an expression.
    
        When a static type checker encounters a call to ``reveal_type()``,
        it will emit the inferred type of the argument::
    
            x: int = 1
            reveal_type(x)
    
        Running a static type checker (e.g., mypy) on this example
        will produce output similar to 'Revealed type is "builtins.int"'.
    
        At runtime, the function prints the runtime type of the
        argument and returns the argument unchanged.
        
    """
    ...

def dataclass_transform(*, eq_default=None, order_default=None, kw_only_default=None, field_specifiers=None, **kwargs):
    """
    Decorator to mark an object as providing dataclass-like behaviour.
    
        The decorator can be applied to a function, class, or metaclass.
    
        Example usage with a decorator function::
    
            T = TypeVar("T")
    
            @dataclass_transform()
            def create_model(cls: type[T]) -> type[T]:
                ...
                return cls
    
            @create_model
            class CustomerModel:
                id: int
                name: str
    
        On a base class::
    
            @dataclass_transform()
            class ModelBase: ...
    
            class CustomerModel(ModelBase):
                id: int
                name: str
    
        On a metaclass::
    
            @dataclass_transform()
            class ModelMeta(type): ...
    
            class ModelBase(metaclass=ModelMeta): ...
    
            class CustomerModel(ModelBase):
                id: int
                name: str
    
        The ``CustomerModel`` classes defined above will
        be treated by type checkers similarly to classes created with
        ``@dataclasses.dataclass``.
        For example, type checkers will assume these classes have
        ``__init__`` methods that accept ``id`` and ``name``.
    
        The arguments to this decorator can be used to customize this behavior:
        - ``eq_default`` indicates whether the ``eq`` parameter is assumed to be
            ``True`` or ``False`` if it is omitted by the caller.
        - ``order_default`` indicates whether the ``order`` parameter is
            assumed to be True or False if it is omitted by the caller.
        - ``kw_only_default`` indicates whether the ``kw_only`` parameter is
            assumed to be True or False if it is omitted by the caller.
        - ``field_specifiers`` specifies a static list of supported classes
            or functions that describe fields, similar to ``dataclasses.field()``.
        - Arbitrary other keyword arguments are accepted in order to allow for
            possible future extensions.
    
        At runtime, this decorator records its arguments in the
        ``__dataclass_transform__`` attribute on the decorated object.
        It has no other runtime effect.
    
        See PEP 681 for more details.
        
    """
    ...
