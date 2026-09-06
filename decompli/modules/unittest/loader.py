# Module: loader
# Pseudo-source reconstructed from bytecode (no decompiler)


def _FailedTest():
    """_FailedTest"""
    ...

def _make_failed_import_test(name, suiteClass):
    ...

def _make_failed_load_tests(name, exception, suiteClass):
    ...

def _make_failed_test(methodname, exception, suiteClass, message):
    ...

def _make_skipped_test(methodname, exception, suiteClass):
    ...

def _jython_aware_splitext(path):
    ...

def TestLoader():
    """TestLoader"""
    ...

def _makeLoader(prefix, sortUsing, suiteClass, testNamePatterns):
    ...

def getTestCaseNames(testCaseClass, prefix, sortUsing, testNamePatterns):
    ...

def makeSuite(testCaseClass, prefix, sortUsing, suiteClass):
    ...

def findTestCases(module, prefix, sortUsing, suiteClass):
    ...
