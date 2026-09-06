# Module: runners
# Pseudo-source reconstructed from bytecode (no decompiler)


def _State():
    """_State"""
    ...

def Runner():
    """Runner"""
    ...

def run(main, *, debug=None):
    """
    Execute the coroutine and return the result.
    
        This function runs the passed coroutine, taking care of
        managing the asyncio event loop and finalizing asynchronous
        generators.
    
        This function cannot be called when another asyncio event loop is
        running in the same thread.
    
        If debug is True, the event loop will be run in debug mode.
    
        This function always creates a new event loop and closes it at the end.
        It should be used as a main entry point for asyncio programs, and should
        ideally only be called once.
    
        Example:
    
            async def main():
                await asyncio.sleep(1)
                print('hello')
    
            asyncio.run(main())
        
    """
    ...

def _cancel_all_tasks(loop):
    ...
