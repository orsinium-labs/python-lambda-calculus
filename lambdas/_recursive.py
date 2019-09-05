from ._natural import MUL, DEC, LTE, ONE, TWO, ADD, ISZERO, ZERO, INC, SUB, LT
from ._bool import NOT
from ._combinators import Y

# recursive
FAC = Y(
    lambda f: lambda n: ISZERO(n)
    (lambda _: ONE)
    (lambda _: MUL(n)(f(DEC(n))))
    (ZERO)
)
FIB = Y(
    lambda f: lambda n: LTE(n)(TWO)
    (lambda _: ONE)
    (lambda _: ADD(f(DEC(n)))(f(DEC(DEC(n)))))
    (ZERO)
)

# more arithmetic
DIV = Y(
    lambda f: lambda a: lambda b: LT(a)(b)
    (lambda _: ZERO)
    (lambda _: INC(f(SUB(a)(b))(b)))
    (ZERO)
)
MOD = Y(
    lambda f: lambda a: lambda b: LT(a)(b)
    (lambda _: a)
    (lambda _: f(SUB(a)(b))(b))
    (ZERO)
)
EVEN = lambda a: ISZERO(MOD(a)(TWO))
ODD  = lambda a: NOT(EVEN(a))
