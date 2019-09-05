import pytest

from lambdas import SIGN, UNSIGN, NEG, ISPOS, ISNEG, SADD, SSUB, SMUL
from lambdas import TRUE, FALSE
from lambdas import ONE, TWO, THREE, FOUR
from lambdas import CONS, CAR, CDR
from lambdas import decode_number


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
