# Module: case
# Pseudo-source reconstructed from bytecode (no decompiler)


def SkipTest():
    """SkipTest"""
    ...

def _ShouldStop():
    """_ShouldStop"""
    ...

def _UnexpectedSuccess():
    """_UnexpectedSuccess"""
    ...

def _Outcome():
    """_Outcome"""
    ...

def _addSkip(result, test_case, reason):
    ...

def _addError(result, test, exc_info):
    ...

def _id(obj):
    ...

def _enter_context(cm, addcleanup):
    ...

def addModuleCleanup(function, *args, **kwargs):
    """
    Same as addCleanup, except the cleanup items are called even if
        setUpModule fails (unlike tearDownModule).
    """
    ...

def enterModuleContext(cm):
    """Same as enterContext, but module-wide."""
    ...

def doModuleCleanups():
    """
    Execute all module cleanup functions. Normally called for you after
        tearDownModule.
    """
    ...

def skip(reason):
    """
    
        Unconditionally skip a test.
        
    """
    ...

def skipIf(condition, reason):
    """
    
        Skip a test if the condition is true.
        
    """
    ...

def skipUnless(condition, reason):
    """
    
        Skip a test unless the condition is true.
        
    """
    ...

def expectedFailure(test_item):
    ...

def _is_subtype(expected, basetype):
    ...

def _BaseTestCaseContext():
    """_BaseTestCaseContext"""
    ...

def _AssertRaisesBaseContext():
    """_AssertRaisesBaseContext"""
    ...

def _AssertRaisesContext():
    """_AssertRaisesContext"""
    ...

def _AssertWarnsContext():
    """_AssertWarnsContext"""
    ...

def _OrderedChainMap():
    """_OrderedChainMap"""
    ...

def TestCase():
    """TestCase"""
    ...

def FunctionTestCase():
    """FunctionTestCase"""
    ...

def _SubTest():
    """_SubTest"""
    ...
