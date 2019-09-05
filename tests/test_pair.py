from lambdas import CONS, CAR, CDR


def test_pair():
    c = CONS(16)(42)
    assert CAR(c) == 16
    assert CDR(c) == 42
