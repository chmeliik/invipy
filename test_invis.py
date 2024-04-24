# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

from hypothesis import given
from hypothesis import strategies as st

import invis


@given(b=st.integers(min_value=0, max_value=255))
def test_roundtrip_encode_byte_decode_byte(b: int) -> None:
    encoded = invis.encode_byte(b)
    decoded = invis.decode_byte(encoded)
    assert b == decoded, (b, decoded)


@given(s=st.text())
def test_roundtrip_encode_decode(s: str) -> None:
    encoded = invis.encode(s)
    decoded = invis.decode(encoded)
    assert s == decoded, (s, decoded)
