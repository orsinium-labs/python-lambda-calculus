from ._bool import IDENTITY, TRUE

# combinators
I = IDENTITY
K = TRUE
S = lambda a: lambda b: lambda c: a(c)(b(c))
Y = lambda f: (
    (lambda x: f(lambda y: x(x)(y)))
    (lambda x: f(lambda y: x(x)(y)))
)
