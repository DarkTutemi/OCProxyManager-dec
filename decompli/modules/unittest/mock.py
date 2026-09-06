# Module: mock
# Pseudo-source reconstructed from bytecode (no decompiler)


def InvalidSpecError():
    """InvalidSpecError"""
    ...

def _is_async_obj(obj):
    ...

def _is_async_func(func):
    ...

def _is_instance_mock(obj):
    ...

def _is_exception(obj):
    ...

def _extract_mock(obj):
    ...

def _get_signature_object(func, as_instance, eat_self):
    """
    
        Given an arbitrary, possibly callable object, try to create a suitable
        signature object.
        Return a (reduced func, signature) tuple, or None.
        
    """
    ...

def _check_signature(func, mock, skipfirst, instance):
    ...

def _copy_func_details(func, funcopy):
    ...

def _callable(obj):
    ...

def _is_list(obj):
    ...

def _instance_callable(obj):
    """
    Given an object, return True if the object is callable.
        For classes, return True if instances would be callable.
    """
    ...

def _set_signature(mock, original, instance):
    ...

def _setup_func(funcopy, mock, sig):
    ...

def _setup_async_mock(mock):
    ...

def _is_magic(name):
    ...

def _SentinelObject():
    """_SentinelObject"""
    ...

def _Sentinel():
    """_Sentinel"""
    ...

def _delegating_property(name):
    ...

def _CallList():
    """_CallList"""
    ...

def _check_and_set_parent(parent, value, name, new_name):
    ...

def _MockIter():
    """_MockIter"""
    ...

def Base():
    """Base"""
    ...

def NonCallableMock():
    """NonCallableMock"""
    ...

def _AnyComparer():
    """_AnyComparer"""
    ...

def _try_iter(obj):
    ...

def CallableMixin():
    """CallableMixin"""
    ...

def Mock():
    """Mock"""
    ...

def _check_spec_arg_typos(kwargs_to_check):
    ...

def _patch():
    """_patch"""
    ...

def _get_target(target):
    ...

def _patch_object(target, attribute, new, spec, create, spec_set, autospec, new_callable, *, unsafe=None, **kwargs):
    """
    
        patch the named member (`attribute`) on an object (`target`) with a mock
        object.
    
        `patch.object` can be used as a decorator, class decorator or a context
        manager. Arguments `new`, `spec`, `create`, `spec_set`,
        `autospec` and `new_callable` have the same meaning as for `patch`. Like
        `patch`, `patch.object` takes arbitrary keyword arguments for configuring
        the mock object it creates.
    
        When used as a class decorator `patch.object` honours `patch.TEST_PREFIX`
        for choosing which methods to wrap.
        
    """
    ...

def _patch_multiple(target, spec, create, spec_set, autospec, new_callable, **kwargs):
    """
    Perform multiple patches in a single call. It takes the object to be
        patched (either as an object or a string to fetch the object by importing)
        and keyword arguments for the patches::
    
            with patch.multiple(settings, FIRST_PATCH='one', SECOND_PATCH='two'):
                ...
    
        Use `DEFAULT` as the value if you want `patch.multiple` to create
        mocks for you. In this case the created mocks are passed into a decorated
        function by keyword, and a dictionary is returned when `patch.multiple` is
        used as a context manager.
    
        `patch.multiple` can be used as a decorator, class decorator or a context
        manager. The arguments `spec`, `spec_set`, `create`,
        `autospec` and `new_callable` have the same meaning as for `patch`. These
        arguments will be applied to *all* patches done by `patch.multiple`.
    
        When used as a class decorator `patch.multiple` honours `patch.TEST_PREFIX`
        for choosing which methods to wrap.
        
    """
    ...

def patch(target, new, spec, create, spec_set, autospec, new_callable, *, unsafe=None, **kwargs):
    """
    
        `patch` acts as a function decorator, class decorator or a context
        manager. Inside the body of the function or with statement, the `target`
        is patched with a `new` object. When the function/with statement exits
        the patch is undone.
    
        If `new` is omitted, then the target is replaced with an
        `AsyncMock if the patched object is an async function or a
        `MagicMock` otherwise. If `patch` is used as a decorator and `new` is
        omitted, the created mock is passed in as an extra argument to the
        decorated function. If `patch` is used as a context manager the created
        mock is returned by the context manager.
    
        `target` should be a string in the form `'package.module.ClassName'`. The
        `target` is imported and the specified object replaced with the `new`
        object, so the `target` must be importable from the environment you are
        calling `patch` from. The target is imported when the decorated function
        is executed, not at decoration time.
    
        The `spec` and `spec_set` keyword arguments are passed to the `MagicMock`
        if patch is creating one for you.
    
        In addition you can pass `spec=True` or `spec_set=True`, which causes
        patch to pass in the object being mocked as the spec/spec_set object.
    
        `new_callable` allows you to specify a different class, or callable object,
        that will be called to create the `new` object. By default `AsyncMock` is
        used for async functions and `MagicMock` for the rest.
    
        A more powerful form of `spec` is `autospec`. If you set `autospec=True`
        then the mock will be created with a spec from the object being replaced.
        All attributes of the mock will also have the spec of the corresponding
        attribute of the object being replaced. Methods and functions being
        mocked will have their arguments checked and will raise a `TypeError` if
        they are called with the wrong signature. For mocks replacing a class,
        their return value (the 'instance') will have the same spec as the class.
    
        Instead of `autospec=True` you can pass `autospec=some_object` to use an
        arbitrary object as the spec instead of the one being replaced.
    
        By default `patch` will fail to replace attributes that don't exist. If
        you pass in `create=True`, and the attribute doesn't exist, patch will
        create the attribute for you when the patched function is called, and
        delete it again afterwards. This is useful for writing tests against
        attributes that your production code creates at runtime. It is off by
        default because it can be dangerous. With it switched on you can write
        passing tests against APIs that don't actually exist!
    
        Patch can be used as a `TestCase` class decorator. It works by
        decorating each test method in the class. This reduces the boilerplate
        code when your test methods share a common patchings set. `patch` finds
        tests by looking for method names that start with `patch.TEST_PREFIX`.
        By default this is `test`, which matches the way `unittest` finds tests.
        You can specify an alternative prefix by setting `patch.TEST_PREFIX`.
    
        Patch can be used as a context manager, with the with statement. Here the
        patching applies to the indented block after the with statement. If you
        use "as" then the patched object will be bound to the name after the
        "as"; very useful if `patch` is creating a mock object for you.
    
        Patch will raise a `RuntimeError` if passed some common misspellings of
        the arguments autospec and spec_set. Pass the argument `unsafe` with the
        value True to disable that check.
    
        `patch` takes arbitrary keyword arguments. These will be passed to
        `AsyncMock` if the patched object is asynchronous, to `MagicMock`
        otherwise or to `new_callable` if specified.
    
        `patch.dict(...)`, `patch.multiple(...)` and `patch.object(...)` are
        available for alternate use-cases.
        
    """
    ...

def _patch_dict():
    """_patch_dict"""
    ...

def _clear_dict(in_dict):
    ...

def _patch_stopall():
    """Stop all active patches. LIFO to unroll nested patches."""
    ...

def _get_method(name, func):
    """Turns a callable object (like a mock) into a real function"""
    ...

def _get_eq(self):
    ...

def _get_ne(self):
    ...

def _get_iter(self):
    ...

def _get_async_iter(self):
    ...

def _set_return_value(mock, method, name):
    ...

def MagicMixin():
    """MagicMixin"""
    ...

def NonCallableMagicMock():
    """NonCallableMagicMock"""
    ...

def AsyncMagicMixin():
    """AsyncMagicMixin"""
    ...

def MagicMock():
    """MagicMock"""
    ...

def MagicProxy():
    """MagicProxy"""
    ...

def AsyncMockMixin():
    """AsyncMockMixin"""
    ...

def AsyncMock():
    """AsyncMock"""
    ...

def _ANY():
    """_ANY"""
    ...

def _format_call_signature(name, args, kwargs):
    ...

def _Call():
    """_Call"""
    ...

def create_autospec(spec, spec_set, instance, _parent, _name, *, unsafe=None, **kwargs):
    """
    Create a mock object using another object as a spec. Attributes on the
        mock will use the corresponding attribute on the `spec` object as their
        spec.
    
        Functions or methods being mocked will have their arguments checked
        to check that they are called with the correct signature.
    
        If `spec_set` is True then attempting to set attributes that don't exist
        on the spec object will raise an `AttributeError`.
    
        If a class is used as a spec then the return value of the mock (the
        instance of the class) will have the same spec. You can use a class as the
        spec for an instance object by passing `instance=True`. The returned mock
        will only be callable if instances of the mock are callable.
    
        `create_autospec` will raise a `RuntimeError` if passed some common
        misspellings of the arguments autospec and spec_set. Pass the argument
        `unsafe` with the value True to disable that check.
    
        `create_autospec` also takes arbitrary keyword arguments that are passed to
        the constructor of the created mock.
    """
    ...

def _must_skip(spec, entry, is_type):
    """
    
        Return whether we should skip the first argument on spec's `entry`
        attribute.
        
    """
    ...

def _SpecState():
    """_SpecState"""
    ...

def _to_stream(read_data):
    ...

def mock_open(mock, read_data):
    """
    
        A helper function to create a mock to replace the use of `open`. It works
        for `open` called directly or used as a context manager.
    
        The `mock` argument is the mock object to configure. If `None` (the
        default) then a `MagicMock` will be created for you, with the API limited
        to methods or attributes available on standard file handles.
    
        `read_data` is a string for the `read`, `readline` and `readlines` of the
        file handle to return.  This is an empty string by default.
        
    """
    ...

def PropertyMock():
    """PropertyMock"""
    ...

def seal(mock):
    """
    Disable the automatic generation of child mocks.
    
        Given an input Mock, seals it to ensure no further mocks will be generated
        when accessing an attribute that was not already defined.
    
        The operation recursively seals the mock passed in, meaning that
        the mock itself, any mocks generated by accessing one of its attributes,
        and all assigned mocks without a name or spec will be sealed.
        
    """
    ...

def _AsyncIterator():
    """_AsyncIterator"""
    ...
