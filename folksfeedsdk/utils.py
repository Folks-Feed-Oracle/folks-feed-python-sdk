import base64


def gs_to_int(gs, byte_index=-1):
    decoded_value = base64.b64decode(gs)
    if byte_index == -1:
        return int.from_bytes(decoded_value, byteorder="big")
    return int.from_bytes(decoded_value[0 + 8 * byte_index : 8 + 8 * byte_index], byteorder="big")
