

IDENTITY = lambda a: a

# boolean values
TRUE  = lambda a: lambda b: a
FALSE = lambda a: lambda b: b

# base boolean operations
OR  = lambda a: lambda b: a(TRUE)(b)
AND = lambda a: lambda b: a(b)(FALSE)
NOT = lambda a: a(FALSE)(TRUE)

# additional boolean operations
XOR = lambda a: lambda b: a(b(FALSE)(TRUE))(b(TRUE)(FALSE))

# arithmetic
INC = lambda n: lambda a: lambda b: a(n(a)(b))
ADD = lambda a: lambda b: a(INC)(b)
MUL = lambda a: lambda b: lambda c: a(b(c))
DEC = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(IDENTITY)
SUB = lambda a: lambda b: b(DEC)(a)
POW = lambda a: lambda b: b(a)

# numbers
ZERO  = FALSE
ONE   = IDENTITY
TWO   = lambda a: lambda b: a(a(b))
THREE = lambda a: lambda b: a(a(a(b)))
FOUR  = INC(THREE)
FIVE  = ADD(TWO)(THREE)
SIX   = MUL(TWO)(THREE)

# checks
ISZERO = lambda a: a(lambda _: FALSE)(TRUE)
GTE = lambda a: lambda b: ISZERO(SUB(b)(a))
LTE = lambda a: lambda b: ISZERO(SUB(a)(b))
GT  = lambda a: lambda b: ISZERO(SUB(INC(b))(a))
LT  = lambda a: lambda b: ISZERO(SUB(INC(a))(b))
EQ  = lambda a: lambda b: AND(GTE(a)(b))(LTE(a)(b))

# combinators
I = IDENTITY
K = lambda a: lambda b: a
S = lambda a: lambda b: lambda c: a(c)(b(c))
Y = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))

# pair
CONS = lambda a: lambda b: lambda c: c(a)(b)
CAR  = lambda p: p(TRUE)
CDR  = lambda p: p(FALSE)


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
DIV = Y(
    lambda f: lambda a: lambda b: LTE(a)(b)
    (lambda _: ONE)
    (lambda _: ADD(ONE)(f(SUB(a)(b))(b)))
    (ZERO)
)


# helpers

def make_number(f) -> int:
    incr = lambda x: x + 1
    return f(incr)(0)
