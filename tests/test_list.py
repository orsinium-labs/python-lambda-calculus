import pytest

from lambdas import ZERO, ONE, TWO, THREE, FOUR
from lambdas import ADD, LTE
from lambdas import LIST, APPEND, PREPEND, REVERSE, MAP, RANGE, REDUCE, FILTER
from lambdas import decode_number, decode_list


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
    ([], 0),
    ([ONE], 1),
    ([ONE, TWO], 3),
    ([ONE, TWO, THREE], 6),
])
def test_reduce(given, expected):
    lst = LIST
    for el in given:
        lst = PREPEND(lst)(el)
    assert decode_number(REDUCE(ADD)(lst)(ZERO)) == expected


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


@pytest.mark.parametrize('given, expected', [
    ([ONE], []),
    ([ONE, ONE], []),
    ([FOUR], [4]),
    ([ONE, TWO], [2]),
    ([THREE, ONE, TWO], [3, 2]),
])
def test_filter(given, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    result = FILTER(LTE(TWO))(lst)
    decoded = [decode_number(n) for n in decode_list(result)]
    assert decoded == expected
