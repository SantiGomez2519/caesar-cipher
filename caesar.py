# English alphabet: 26 letters
ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_SIZE = len(ALPHABET_LOWER)


def _normalize_key(key: int) -> int:
    return key % ALPHABET_SIZE


def encrypt(text: str, key: int) -> str:
    key = _normalize_key(key)
    result = []
    for c in text:
        if c in ALPHABET_LOWER:
            idx = (ALPHABET_LOWER.index(c) + key) % ALPHABET_SIZE # new index after shift
            result.append(ALPHABET_LOWER[idx])
        elif c in ALPHABET_UPPER:
            idx = (ALPHABET_UPPER.index(c) + key) % ALPHABET_SIZE # new index after shift
            result.append(ALPHABET_UPPER[idx])
        else:
            result.append(c)
    return "".join(result)


def decrypt(text: str, key: int) -> str:
    key = _normalize_key(key)
    result = []
    for c in text:
        if c in ALPHABET_LOWER:
            idx = (ALPHABET_LOWER.index(c) - key) % ALPHABET_SIZE # new index after shift
            result.append(ALPHABET_LOWER[idx])
        elif c in ALPHABET_UPPER:
            idx = (ALPHABET_UPPER.index(c) - key) % ALPHABET_SIZE # new index after shift
            result.append(ALPHABET_UPPER[idx])
        else:
            result.append(c)
    return "".join(result)
