

IDENTITY = lambda a: a

# boolean values
TRUE  = lambda a: lambda b: a
FALSE = lambda a: lambda b: b

# base boolean operations
OR  = lambda a: lambda b: a(TRUE)(b)
AND = lambda a: lambda b: a(b)(FALSE)
NOT = lambda a: a(FALSE)(TRUE)

# additional boolean operations
XOR  = lambda a: lambda b: a(b(FALSE)(TRUE))(b(TRUE)(FALSE))
XNOR = lambda a: lambda b: NOT(XOR(a)(b))

# arithmetic
INC = lambda n: lambda a: lambda b: a(n(a)(b))
ADD = lambda a: lambda b: a(INC)(b)
MUL = lambda a: lambda b: lambda c: a(b(c))
DEC = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(IDENTITY)
SUB = lambda a: lambda b: b(DEC)(a)
POW = lambda a: lambda b: b(a)
DIFF = lambda a: lambda b: ADD(SUB(a)(b))(SUB(b)(a))

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

# The Billion Dollar Mistake
NULL   = lambda _: TRUE
ISNULL = lambda _: lambda _: FALSE

# signed numbers
SIGN   = lambda n: CONS(TRUE)(n)
NEG    = lambda p: CONS(NOT(CAR(p)))(CDR(p))
ISPOS  = lambda p: CAR(p)
ISNEG  = lambda p: NOT(CAR(p))
UNSIGN = lambda p: CDR(p)
SADD   = lambda a: lambda b: (
    XNOR(CAR(a))(CAR(b))
    (CONS(CAR(a))(ADD(CDR(a))(CDR(b))))  # same sign
    (
        CONS    # opposite sign
        (XOR(CAR(a))(LTE(CDR(a))(CDR(b))))  # calculate sign
        (DIFF(CDR(a))(CDR(b)))   # calculate value
    )
)
SSUB = lambda a: lambda b: SADD(a)(CONS(NOT(CAR(b)))(CDR(b)))
SMUL = lambda a: lambda b: CONS(XNOR(CAR(a))(CAR(b)))(MUL(CDR(a))(CDR(b)))

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


# helpers

def decode_number(f) -> int:
    incr = lambda x: x + 1
    return f(incr)(0)


# improve repr
for name, func in globals().copy().items():
    if '_' not in name and name.isupper():
        func.__qualname__ = name
