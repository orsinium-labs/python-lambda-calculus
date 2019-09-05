from ._bool import TRUE
from ._list import EMPTY, HEAD, TAIL


def decode_number(f) -> int:
    incr = lambda x: x + 1
    return f(incr)(0)


def decode_list(encoded) -> list:
    decoded = []
    for _ in range(100):
        if EMPTY(encoded) is TRUE:
            return decoded
        decoded.append(HEAD(encoded))
        encoded = TAIL(encoded)
    raise RuntimeError('probably infinite list')
