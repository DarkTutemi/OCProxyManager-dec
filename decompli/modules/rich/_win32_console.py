# Module: _win32_console
# Pseudo-source reconstructed from bytecode (no decompiler)


def LegacyWindowsError():
    """LegacyWindowsError"""
    ...

def WindowsCoordinates():
    """WindowsCoordinates"""
    ...

def CONSOLE_SCREEN_BUFFER_INFO():
    """CONSOLE_SCREEN_BUFFER_INFO"""
    ...

def CONSOLE_CURSOR_INFO():
    """CONSOLE_CURSOR_INFO"""
    ...

def GetStdHandle(handle):
    """
    Retrieves a handle to the specified standard device (standard input, standard output, or standard error).
    
        Args:
            handle (int): Integer identifier for the handle. Defaults to -11 (stdout).
    
        Returns:
            wintypes.HANDLE: The handle
        
    """
    ...

def GetConsoleMode(std_handle):
    """
    Retrieves the current input mode of a console's input buffer
        or the current output mode of a console screen buffer.
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
    
        Raises:
            LegacyWindowsError: If any error occurs while calling the Windows console API.
    
        Returns:
            int: Value representing the current console mode as documented at
                https://docs.microsoft.com/en-us/windows/console/getconsolemode#parameters
        
    """
    ...

def FillConsoleOutputCharacter(std_handle, char, length, start):
    """
    Writes a character to the console screen buffer a specified number of times, beginning at the specified coordinates.
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
            char (str): The character to write. Must be a string of length 1.
            length (int): The number of times to write the character.
            start (WindowsCoordinates): The coordinates to start writing at.
    
        Returns:
            int: The number of characters written.
        
    """
    ...

def FillConsoleOutputAttribute(std_handle, attributes, length, start):
    """
    Sets the character attributes for a specified number of character cells,
        beginning at the specified coordinates in a screen buffer.
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
            attributes (int): Integer value representing the foreground and background colours of the cells.
            length (int): The number of cells to set the output attribute of.
            start (WindowsCoordinates): The coordinates of the first cell whose attributes are to be set.
    
        Returns:
            int: The number of cells whose attributes were actually set.
        
    """
    ...

def SetConsoleTextAttribute(std_handle, attributes):
    """
    Set the colour attributes for all text written after this function is called.
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
            attributes (int): Integer value representing the foreground and background colours.
    
    
        Returns:
            bool: True if the attribute was set successfully, otherwise False.
        
    """
    ...

def GetConsoleScreenBufferInfo(std_handle):
    """
    Retrieves information about the specified console screen buffer.
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
    
        Returns:
            CONSOLE_SCREEN_BUFFER_INFO: A CONSOLE_SCREEN_BUFFER_INFO ctype struct contain information about
                screen size, cursor position, colour attributes, and more.
    """
    ...

def SetConsoleCursorPosition(std_handle, coords):
    """
    Set the position of the cursor in the console screen
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
            coords (WindowsCoordinates): The coordinates to move the cursor to.
    
        Returns:
            bool: True if the function succeeds, otherwise False.
        
    """
    ...

def GetConsoleCursorInfo(std_handle, cursor_info):
    """
    Get the cursor info - used to get cursor visibility and width
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
            cursor_info (CONSOLE_CURSOR_INFO): CONSOLE_CURSOR_INFO ctype struct that receives information
                about the console's cursor.
    
        Returns:
              bool: True if the function succeeds, otherwise False.
        
    """
    ...

def SetConsoleCursorInfo(std_handle, cursor_info):
    """
    Set the cursor info - used for adjusting cursor visibility and width
    
        Args:
            std_handle (wintypes.HANDLE): A handle to the console input buffer or the console screen buffer.
            cursor_info (CONSOLE_CURSOR_INFO): CONSOLE_CURSOR_INFO ctype struct containing the new cursor info.
    
        Returns:
              bool: True if the function succeeds, otherwise False.
        
    """
    ...

def SetConsoleTitle(title):
    """
    Sets the title of the current console window
    
        Args:
            title (str): The new title of the console window.
    
        Returns:
            bool: True if the function succeeds, otherwise False.
        
    """
    ...

def LegacyWindowsTerm():
    """LegacyWindowsTerm"""
    ...
