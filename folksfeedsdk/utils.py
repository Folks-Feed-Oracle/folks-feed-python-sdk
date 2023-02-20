import base64


def gs_to_int(gs, offset: int = None, size: int = None):
    decoded_value = base64.b64decode(gs)
    if size == None:
        return int.from_bytes(decoded_value, byteorder="big")
    return int.from_bytes(decoded_value[offset : offset + size], byteorder="big")
