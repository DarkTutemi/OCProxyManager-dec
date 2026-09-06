# Module: contentmanager
# Pseudo-source reconstructed from bytecode (no decompiler)


def ContentManager():
    """ContentManager"""
    ...

def get_text_content(msg, errors):
    ...

def get_non_text_content(msg):
    ...

def get_message_content(msg):
    ...

def get_and_fixup_unknown_message_content(msg):
    ...

def _prepare_set(msg, maintype, subtype, headers):
    ...

def _finalize_set(msg, disposition, filename, cid, params):
    ...

def _encode_base64(data, max_line_length):
    ...

def _encode_text(string, charset, cte, policy):
    ...

def set_text_content(msg, string, subtype, charset, cte, disposition, filename, cid, params, headers):
    ...

def set_message_content(msg, message, subtype, cte, disposition, filename, cid, params, headers):
    ...

def set_bytes_content(msg, data, maintype, subtype, cte, disposition, filename, cid, params, headers):
    ...
