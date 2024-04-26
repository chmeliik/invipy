# Inspired by sillysaurus3 in https://news.ycombinator.com/item?id=11727909

ZERO = "\u200e"
ONE = "\u200f"


def encode_byte(normal_byte: int) -> str:
    encoded_byte = ""
    for shift in range(8):
        if (normal_byte >> shift) & 1:
            encoded_byte += ONE
        else:
            encoded_byte += ZERO
    return encoded_byte


def decode_byte(encoded_byte: str) -> int:
    normal_byte = 0
    for i, c in enumerate(encoded_byte):
        if c == ONE:
            normal_byte += 2**i
    return normal_byte


def encode(normal_str: str) -> str:
    normal_bytes = normal_str.encode("utf-8")
    encoded_bytes = map(encode_byte, normal_bytes)
    return "".join(encoded_bytes)


def decode(encoded_str: str) -> str:
    encoded_bytes = (encoded_str[i : i + 8] for i in range(0, len(encoded_str), 8))
    normal_bytes = map(decode_byte, encoded_bytes)
    return bytes(normal_bytes).decode("utf-8")


if __name__ == "__main__":
    import sys

    print(encode(sys.stdin.read()), end="")
