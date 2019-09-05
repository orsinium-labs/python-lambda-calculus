import pytest

from lambdas import ONE, TWO, THREE, FOUR, FIVE, SIX
from lambdas import FAC, FIB, DIV, MOD, MIN, MAX
from lambdas import decode_number


@pytest.mark.parametrize('given, expected', [
    (THREE, 6),
    (FOUR,  24),
])
def test_fac(given, expected):
    assert decode_number(FAC(given)) == expected


@pytest.mark.parametrize('given, expected', [
    (ONE,   1),
    (TWO,   1),
    (THREE, 2),
    (FOUR,  3),
    (FIVE,  5),
    (SIX,   8),
])
def test_fib(given, expected):
    assert decode_number(FIB(given)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,  ONE, 1),
    (TWO,  ONE, 2),
    (FOUR, TWO, 2),
    (SIX,  TWO, 3),
    (FIVE, TWO, 2),
])
def test_div(left, right, expected):
    assert decode_number(DIV(left)(right)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE, 0),
    (THREE, TWO, 1),
    (FIVE,  TWO, 1),
])
def test_mod(left, right, expected):
    assert decode_number(MOD(left)(right)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE,    1),
    (TWO,   ONE,    1),
    (ONE,   TWO,    1),
    (THREE, FIVE,   3),
    (FIVE,  THREE,  3),
])
def test_min(left, right, expected):
    assert decode_number(MIN(left)(right)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE,    1),
    (TWO,   ONE,    2),
    (ONE,   TWO,    2),
    (THREE, FIVE,   5),
    (FIVE,  THREE,  5),
])
def test_max(left, right, expected):
    assert decode_number(MAX(left)(right)) == expected
