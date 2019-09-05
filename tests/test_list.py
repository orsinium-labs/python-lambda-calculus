import pytest

from lambdas import ZERO, ONE, TWO, THREE, FOUR
from lambdas import ADD, LTE, FALSE, TRUE
from lambdas import LIST, APPEND, PREPEND, REVERSE, LENGTH, ANY, ALL
from lambdas import MAP, RANGE, REDUCE, FILTER, TAKE, DROP, INDEX
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


@pytest.mark.parametrize('given, number, expected', [
    ([1, 2, 3], ONE, [2, 3]),
])
def test_drop(given, number, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    result = DROP(number)(lst)
    assert decode_list(result) == expected


@pytest.mark.parametrize('given, number, expected', [
    ([1, 2, 3], TWO, [1, 2]),
    ([1, 2, 3], FOUR, [1, 2, 3]),
    ([1, 2, 3], ZERO, []),
    ([], TWO, []),
])
def test_take(given, number, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    result = TAKE(number)(lst)
    assert decode_list(result) == expected


@pytest.mark.parametrize('given, expected', [
    ([], 0),
    ([4], 1),
    ([4, 5], 2),
    ([1, 2, 3], 3),
])
def test_length(given, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    assert decode_number(LENGTH(lst)) == expected


@pytest.mark.parametrize('given, number, expected', [
    ([1, 2, 3], ONE, 2),
])
def test_index(given, number, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    result = INDEX(number)(lst)
    if expected is not None:
        assert result == expected


@pytest.mark.parametrize('given, expected', [
    ([], FALSE),
    ([FALSE, FALSE], FALSE),
    ([FALSE, TRUE], TRUE),
    ([TRUE, FALSE], TRUE),
    ([FALSE, TRUE, FALSE], TRUE),
])
def test_any(given, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    assert ANY(lst) is expected


@pytest.mark.parametrize('given, expected', [
    ([], TRUE),
    ([TRUE], TRUE),
    ([TRUE, TRUE], TRUE),
    ([FALSE, FALSE], FALSE),
    ([FALSE, TRUE], FALSE),
    ([TRUE, FALSE], FALSE),
    ([FALSE, TRUE, FALSE], FALSE),
])
def test_all(given, expected):
    lst = LIST
    for el in given:
        lst = APPEND(lst)(el)
    assert ALL(lst) is expected
