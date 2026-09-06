# Module: measure
# Pseudo-source reconstructed from bytecode (no decompiler)


def Measurement():
    """Measurement"""
    ...

def measure_renderables(console, options, renderables):
    """
    Get a measurement that would fit a number of renderables.
    
        Args:
            console (~rich.console.Console): Console instance.
            options (~rich.console.ConsoleOptions): Console options.
            renderables (Iterable[RenderableType]): One or more renderable objects.
    
        Returns:
            Measurement: Measurement object containing range of character widths required to
                contain all given renderables.
        
    """
    ...
