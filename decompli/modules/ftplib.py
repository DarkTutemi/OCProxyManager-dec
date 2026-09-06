# Module: ftplib
# Pseudo-source reconstructed from bytecode (no decompiler)


def Error():
    """Error"""
    ...

def error_reply():
    """error_reply"""
    ...

def error_temp():
    """error_temp"""
    ...

def error_perm():
    """error_perm"""
    ...

def error_proto():
    """error_proto"""
    ...

def FTP():
    """FTP"""
    ...

def FTP_TLS():
    """FTP_TLS"""
    ...

def parse150(resp):
    """
    Parse the '150' response for a RETR request.
        Returns the expected transfer size or None; size is not guaranteed to
        be present in the 150 message.
        
    """
    ...

def parse227(resp):
    """
    Parse the '227' response for a PASV request.
        Raises error_proto if it does not contain '(h1,h2,h3,h4,p1,p2)'
        Return ('host.addr.as.numbers', port#) tuple.
    """
    ...

def parse229(resp, peer):
    """
    Parse the '229' response for an EPSV request.
        Raises error_proto if it does not contain '(|||port|)'
        Return ('host.addr.as.numbers', port#) tuple.
    """
    ...

def parse257(resp):
    """
    Parse the '257' response for a MKD or PWD request.
        This is a response to a MKD or PWD request: a directory name.
        Returns the directoryname in the 257 reply.
    """
    ...

def print_line(line):
    """Default retrlines callback to print a line."""
    ...

def ftpcp(source, sourcename, target, targetname, type):
    """Copy file from one FTP-instance to another."""
    ...

def test():
    """
    Test program.
        Usage: ftplib [-d] [-r[file]] host [-l[dir]] [-d[dir]] [-p] [file] ...
    
        Options:
          -d        increase debugging level
          -r[file]  set alternate ~/.netrc file
    
        Commands:
          -l[dir]   list directory
          -d[dir]   change the current directory
          -p        toggle passive and active mode
          file      retrieve the file and write it to stdout
        
    """
    ...
