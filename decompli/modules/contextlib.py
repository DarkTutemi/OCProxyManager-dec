# Module: contextlib
# Pseudo-source reconstructed from bytecode (no decompiler)


def AbstractContextManager():
    """AbstractContextManager"""
    ...

def AbstractAsyncContextManager():
    """AbstractAsyncContextManager"""
    ...

def ContextDecorator():
    """ContextDecorator"""
    ...

def AsyncContextDecorator():
    """AsyncContextDecorator"""
    ...

def _GeneratorContextManagerBase():
    """_GeneratorContextManagerBase"""
    ...

def _GeneratorContextManager():
    """_GeneratorContextManager"""
    ...

def _AsyncGeneratorContextManager():
    """_AsyncGeneratorContextManager"""
    ...

def contextmanager(func):
    """
    @contextmanager decorator.
    
        Typical usage:
    
            @contextmanager
            def some_generator(<arguments>):
                <setup>
                try:
                    yield <value>
                finally:
                    <cleanup>
    
        This makes this:
    
            with some_generator(<arguments>) as <variable>:
                <body>
    
        equivalent to this:
    
            <setup>
            try:
                <variable> = <value>
                <body>
            finally:
                <cleanup>
        
    """
    ...

def asynccontextmanager(func):
    """
    @asynccontextmanager decorator.
    
        Typical usage:
    
            @asynccontextmanager
            async def some_async_generator(<arguments>):
                <setup>
                try:
                    yield <value>
                finally:
                    <cleanup>
    
        This makes this:
    
            async with some_async_generator(<arguments>) as <variable>:
                <body>
    
        equivalent to this:
    
            <setup>
            try:
                <variable> = <value>
                <body>
            finally:
                <cleanup>
        
    """
    ...

def closing():
    """closing"""
    ...

def aclosing():
    """aclosing"""
    ...

def _RedirectStream():
    """_RedirectStream"""
    ...

def redirect_stdout():
    """redirect_stdout"""
    ...

def redirect_stderr():
    """redirect_stderr"""
    ...

def suppress():
    """suppress"""
    ...

def _BaseExitStack():
    """_BaseExitStack"""
    ...

def ExitStack():
    """ExitStack"""
    ...

def AsyncExitStack():
    """AsyncExitStack"""
    ...

def nullcontext():
    """nullcontext"""
    ...

def chdir():
    """chdir"""
    ...
