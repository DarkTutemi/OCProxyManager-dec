# Module: progress
# Pseudo-source reconstructed from bytecode (no decompiler)


def _TrackThread():
    """_TrackThread"""
    ...

def track(sequence, description, total, completed, auto_refresh, console, transient, get_time, refresh_per_second, style, complete_style, finished_style, pulse_style, update_period, disable, show_speed):
    """
    Track progress by iterating over a sequence.
    
        You can also track progress of an iterable, which might require that you additionally specify ``total``.
    
        Args:
            sequence (Iterable[ProgressType]): Values you wish to iterate over and track progress.
            description (str, optional): Description of task show next to progress bar. Defaults to "Working".
            total: (float, optional): Total number of steps. Default is len(sequence).
            completed (int, optional): Number of steps completed so far. Defaults to 0.
            auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
            transient: (bool, optional): Clear the progress on exit. Defaults to False.
            console (Console, optional): Console to write to. Default creates internal Console instance.
            refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
            style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
            complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
            finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
            pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
            update_period (float, optional): Minimum time (in seconds) between calls to update(). Defaults to 0.1.
            disable (bool, optional): Disable display of progress.
            show_speed (bool, optional): Show speed if total isn't known. Defaults to True.
        Returns:
            Iterable[ProgressType]: An iterable of the values in the sequence.
    
        
    """
    ...

def _Reader():
    """_Reader"""
    ...

def _ReadContext():
    """_ReadContext"""
    ...

def wrap_file(file, total, *, description=None, auto_refresh=None, console=None, transient=None, get_time=None, refresh_per_second=None, style=None, complete_style=None, finished_style=None, pulse_style=None, disable=None):
    """
    Read bytes from a file while tracking progress.
    
        Args:
            file (Union[str, PathLike[str], BinaryIO]): The path to the file to read, or a file-like object in binary mode.
            total (int): Total number of bytes to read.
            description (str, optional): Description of task show next to progress bar. Defaults to "Reading".
            auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
            transient: (bool, optional): Clear the progress on exit. Defaults to False.
            console (Console, optional): Console to write to. Default creates internal Console instance.
            refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
            style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
            complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
            finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
            pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
            disable (bool, optional): Disable display of progress.
        Returns:
            ContextManager[BinaryIO]: A context manager yielding a progress reader.
    
        
    """
    ...

def open(file, mode, buffering, encoding, errors, newline, *, total=None, description=None, auto_refresh=None, console=None, transient=None, get_time=None, refresh_per_second=None, style=None, complete_style=None, finished_style=None, pulse_style=None, disable=None):
    ...

def ProgressColumn():
    """ProgressColumn"""
    ...

def RenderableColumn():
    """RenderableColumn"""
    ...

def SpinnerColumn():
    """SpinnerColumn"""
    ...

def TextColumn():
    """TextColumn"""
    ...

def BarColumn():
    """BarColumn"""
    ...

def TimeElapsedColumn():
    """TimeElapsedColumn"""
    ...

def TaskProgressColumn():
    """TaskProgressColumn"""
    ...

def TimeRemainingColumn():
    """TimeRemainingColumn"""
    ...

def FileSizeColumn():
    """FileSizeColumn"""
    ...

def TotalFileSizeColumn():
    """TotalFileSizeColumn"""
    ...

def MofNCompleteColumn():
    """MofNCompleteColumn"""
    ...

def DownloadColumn():
    """DownloadColumn"""
    ...

def TransferSpeedColumn():
    """TransferSpeedColumn"""
    ...

def ProgressSample():
    """ProgressSample"""
    ...

def Task():
    """Task"""
    ...

def Progress():
    """Progress"""
    ...
