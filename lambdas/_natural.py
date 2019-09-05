from ._bool import AND, TRUE, FALSE, IDENTITY

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
SEVEN = INC(SIX)
EIGHT = MUL(FOUR)(TWO)
NINE  = POW(THREE)(TWO)
TEN   = MUL(FIVE)(TWO)

# checks
ISZERO = lambda a: a(lambda _: FALSE)(TRUE)
GTE = lambda a: lambda b: ISZERO(SUB(b)(a))
LTE = lambda a: lambda b: ISZERO(SUB(a)(b))
GT  = lambda a: lambda b: ISZERO(SUB(INC(b))(a))
LT  = lambda a: lambda b: ISZERO(SUB(INC(a))(b))
EQ  = lambda a: lambda b: AND(GTE(a)(b))(LTE(a)(b))

# advanced arithmetic
MIN  = lambda a: lambda b: LTE(a)(b)(a)(b)
MAX  = lambda a: lambda b: GTE(a)(b)(a)(b)
