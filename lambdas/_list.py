from ._bool import TRUE, FALSE, OR, NOT
from ._pair import CONS, CAR, CDR
from ._combinators import Y
from ._natural import DEC, INC, GTE, ISZERO, ZERO


LIST = CONS(TRUE)(TRUE)
PREPEND = lambda xs: lambda x: CONS(FALSE)(CONS(x)(xs))
EMPTY = lambda xs: CAR(xs)
HEAD = lambda xs: CAR(CDR(xs))
TAIL = lambda xs: CDR(CDR(xs))
APPEND = Y(
    lambda f: lambda xs: lambda x: EMPTY(xs)
    (lambda _: PREPEND(xs)(x))
    (lambda _: CONS(FALSE)(CONS(HEAD(xs))(f(TAIL(xs))(x))))
    (TRUE)
)
REVERSE = Y(
    lambda f: lambda xs: EMPTY(xs)
    (lambda _: LIST)
    (lambda _: APPEND(f(TAIL(xs)))(HEAD(xs)))
    (TRUE)
)
# MAP(a)(xs): apply `a` function to every element in `xs` list.
# Return list of results for every element.
MAP = Y(
    lambda f: lambda a: lambda xs: EMPTY(xs)
    (lambda _: LIST)
    (lambda _: PREPEND(f(a)(TAIL(xs)))(a(HEAD(xs))))
    (TRUE)
)
RANGE = Y(
    lambda f: lambda a: lambda b: GTE(a)(b)
    (lambda _: LIST)
    (lambda _: PREPEND(f(INC(a))(b))(a))
    (TRUE)
)
# REDUCE(r)(l)(v):
# 1. Apply pass head of `l` and `v` into `r` and save result into `v`.
# 2. Do it for every element into lest from left to right.
# 3. Return `v` (accumulated value)
REDUCE = FOLD = Y(
    lambda f: lambda r: lambda l: lambda v: EMPTY(l)
    (lambda _: v)  # if list is empty, return accumulated value (v)
    # pass accumulated value (v) and head into reducer (r)
    # do reucing on tail of list (l) with a new accumulated value (v)
    (lambda _: f(r)(TAIL(l))(r(HEAD(l))(v)))
    (TRUE)
)
FILTER = lambda f: lambda l: (
    REDUCE
    (lambda x: lambda xs: f(x)(APPEND(xs)(x))(xs))
    (l)
    (LIST)
)
DROP = lambda n: lambda l: n(TAIL)(l)
TAKE = Y(lambda f: lambda n: lambda l: (
    OR(EMPTY(l))(ISZERO(n))
    (lambda _: LIST)
    (lambda _: (
        PREPEND(f(DEC(n))(TAIL(l)))
        (HEAD(l))
    ))
    (TRUE)
))
LENGTH = lambda l: REDUCE(lambda x: lambda n: INC(n))(l)(ZERO)
INDEX = Y(lambda f: lambda n: lambda l: (
    ISZERO(n)
    (lambda _: HEAD(l))
    (lambda _: f(DEC(n))(TAIL(l)))
    (TRUE)
))
ANY = Y(lambda f: lambda l: (
    EMPTY(l)
    (lambda _: FALSE)
    (lambda _: HEAD(l)(TRUE)(f(TAIL(l))))
    (TRUE)
))
ALL = Y(lambda f: lambda l: (
    EMPTY(l)
    (lambda _: TRUE)
    (lambda _: NOT(HEAD(l))(FALSE)(f(TAIL(l))))
    (TRUE)
))
