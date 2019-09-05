import pytest

from lambdas import TRUE, FALSE
from lambdas import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX
from lambdas import ADD, INC, MUL, POW, DEC, SUB
from lambdas import ISZERO, GTE, LTE, GT, LT, EQ
from lambdas import decode_number


@pytest.mark.parametrize('given, expected', [
    (ONE,   1),
    (TWO,   2),
    (THREE, 3),
    (FOUR,  4),
    (FIVE,  5),
    (SIX,   6),
])
def test_numbers(given, expected):
    assert decode_number(given) == expected


@pytest.mark.parametrize('given, expected', [
    (ZERO,  1),
    (ONE,   2),
    (TWO,   3),
    (THREE, 4),
])
def test_inc(given, expected):
    assert decode_number(INC(given)) == expected


@pytest.mark.parametrize('given, expected', [
    (ZERO,  0),
    (ONE,   0),
    (TWO,   1),
    (THREE, 2),
])
def test_dec(given, expected):
    assert decode_number(DEC(given)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE, ONE,   2),
    (TWO, THREE, 5),
    (THREE, TWO, 5),
])
def test_add(left, right, expected):
    assert decode_number(ADD(left)(right)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE, 0),
    (TWO,   ONE, 1),
    (THREE, TWO, 1),
    (FOUR,  ONE, 3),
])
def test_sub(left, right, expected):
    assert decode_number(SUB(left)(right)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE, ONE,   1),
    (TWO, THREE, 6),
    (THREE, TWO, 6),
])
def test_mul(left, right, expected):
    assert decode_number(MUL(left)(right)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE,   1),
    (TWO,   ONE,   2),
    (ONE,   TWO,   1),
    (THREE, TWO,   9),
    (THREE, THREE, 27),
])
def test_pow(left, right, expected):
    assert decode_number(POW(left)(right)) == expected


@pytest.mark.parametrize('given, expected', [
    (ZERO, TRUE),
    (ONE,  FALSE),
    (TWO,  FALSE),
])
def test_iszero(given, expected):
    assert ISZERO(given) is expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE,    TRUE),
    (TWO,   THREE,  FALSE),
    (THREE, TWO,    TRUE),
    (FOUR,  TWO,    TRUE),
])
def test_gte(left, right, expected):
    assert GTE(left)(right) is expected
    assert LT(left)(right) is not expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE,    FALSE),
    (TWO,   THREE,  FALSE),
    (THREE, TWO,    TRUE),
    (FOUR,  TWO,    TRUE),
])
def test_gt(left, right, expected):
    assert GT(left)(right) is expected
    assert LTE(left)(right) is not expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE, ONE, TRUE),
    (TWO, TWO, TRUE),
    (TWO, ONE, FALSE),
    (ONE, TWO, FALSE),
])
def test_eq(left, right, expected):
    assert EQ(left)(right) is expected
