#!/usr/bin/python3

import pytest

from lambdas import AND, OR, TRUE, FALSE, NOT, XOR
from lambdas import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX
from lambdas import ADD, INC, MUL, POW, DEC, SUB, DIV, MOD
from lambdas import ISZERO, GTE, LTE, GT, LT, EQ
from lambdas import CONS, CAR, CDR
from lambdas import SIGN, UNSIGN, NEG, ISPOS, ISNEG, SADD, SSUB, SMUL
from lambdas import FAC, FIB
from lambdas import LIST, APPEND, PREPEND, REVERSE, MAP, RANGE
from lambdas import decode_number, decode_list


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  FALSE),
    (TRUE,  FALSE, FALSE),
    (TRUE,  TRUE,  TRUE),
])
def test_and(left, right, expected):
    assert AND(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (TRUE,  TRUE,  TRUE),
])
def test_or(left, right, expected):
    assert OR(left)(right) is expected


@pytest.mark.parametrize('given, expected', [
    (FALSE, TRUE),
    (TRUE, FALSE),
])
def test_not(given, expected):
    assert NOT(given) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (TRUE,  TRUE,  FALSE),
])
def test_xor(left, right, expected):
    assert XOR(left)(right) is expected


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


def test_pair():
    c = CONS(16)(42)
    assert CAR(c) == 16
    assert CDR(c) == 42


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


@pytest.mark.parametrize('given, expected', [
    (THREE, 3),
    (FOUR,  4),
])
def test_sign_unsign(given, expected):
    assert decode_number(UNSIGN(SIGN(given))) == expected


def test_sign_checks():
    s = SIGN(TWO)
    assert ISPOS(s) is TRUE
    assert ISNEG(s) is FALSE

    n = NEG(s)
    assert ISPOS(n) is FALSE
    assert ISNEG(n) is TRUE


@pytest.mark.parametrize('lsign, left, rsign, right, expsign, expvalue', [
    (TRUE, ONE, TRUE, ONE, TRUE, 2),  # 1 + 1 = 2
    (TRUE, ONE, FALSE, TWO, FALSE, 1),  # 1 - 2 = -1
    (FALSE, TWO, TRUE, ONE, FALSE, 1),  # -2 + 1 = -1
    (FALSE, TWO, FALSE, ONE, FALSE, 3),  # -2 - 1 = -3
])
def test_sadd(lsign, left, rsign, right, expsign, expvalue):
    lv = CONS(lsign)(left)
    rv = CONS(rsign)(right)
    res = SADD(lv)(rv)
    assert CAR(res) is expsign
    assert decode_number(CDR(res)) == expvalue


@pytest.mark.parametrize('lsign, left, rsign, right, expsign, expvalue', [
    (TRUE, TWO, TRUE, ONE, TRUE, 1),  # 2 - 1 = 1
    (TRUE, TWO, TRUE, THREE, FALSE, 1),  # 2 - 3 = -1
])
def test_ssub(lsign, left, rsign, right, expsign, expvalue):
    lv = CONS(lsign)(left)
    rv = CONS(rsign)(right)
    res = SSUB(lv)(rv)
    assert CAR(res) is expsign
    assert decode_number(CDR(res)) == expvalue


@pytest.mark.parametrize('lsign, left, rsign, right, expsign, expvalue', [
    (TRUE, TWO, TRUE, THREE, TRUE, 6),  # 2 * 3 = 6
    (TRUE, TWO, FALSE, THREE, FALSE, 6),  # 2 * (-3) = -6
    (FALSE, TWO, TRUE, THREE, FALSE, 6),  # -2 * 3 = -6
    (FALSE, TWO, FALSE, THREE, TRUE, 6),  # -2 * (-3) = 6
])
def test_smul(lsign, left, rsign, right, expsign, expvalue):
    lv = CONS(lsign)(left)
    rv = CONS(rsign)(right)
    res = SMUL(lv)(rv)
    assert CAR(res) is expsign
    assert decode_number(CDR(res)) == expvalue


@pytest.mark.parametrize('given', [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
])
def test_prepend(given):
    lst = LIST
    for el in reversed(given):
        lst = PREPEND(lst)(el)
    assert decode_list(lst) == given


@pytest.mark.parametrize('given', [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
])
def test_append(given):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    assert decode_list(lst) == given


@pytest.mark.parametrize('given', [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
])
def test_reverse(given):
    lst = LIST
    for el in given:
        lst = PREPEND(lst)(el)
    assert decode_list(REVERSE(lst)) == given


@pytest.mark.parametrize('given, expected', [
    ([], []),
    ([ONE], [3]),
    ([ONE, TWO, THREE], [3, 4, 5]),
])
def test_map(given, expected):
    lst = LIST
    for el in reversed(given):
        lst = PREPEND(lst)(el)
    result = MAP(ADD(TWO))(lst)
    decoded = [decode_number(n) for n in decode_list(result)]
    assert decoded == expected


@pytest.mark.parametrize('start, end, expected', [
    (ONE, ONE, []),
    (THREE, ONE, []),
    (ONE, THREE, [1, 2]),
])
def test_range(start, end, expected):
    result = RANGE(start)(end)
    decoded = [decode_number(n) for n in decode_list(result)]
    assert decoded == expected


if __name__ == '__main__':
    pytest.main()
