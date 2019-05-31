

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


# helpers

def make_number(f) -> int:
    incr = lambda x: x + 1
    return f(incr)(0)
