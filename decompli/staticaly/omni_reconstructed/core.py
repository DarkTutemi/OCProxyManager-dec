"""Module: core

Static reconstruction from the Nuitka constants blob + native
code objects. EXACT from the binary: imports, class/function
structure, signatures, type annotations, bases, docstrings, and
every constant / string / numeric literal. Function BODIES are
compiled to native machine code (no Python bytecode is stored),
so they appear as placeholders; the faithful per-function
operation trace is in the matching .nbc file.
"""

# const: 'environ'
# const: 'origin'
# const: 'has_location'
# const: 'submodule_search_locations'
# const: 'core\\__init__.py'
# const: '<module core>'
