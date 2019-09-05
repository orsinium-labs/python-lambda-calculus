from ._bool import TRUE, FALSE

# pair
CONS = lambda a: lambda b: lambda c: c(a)(b)
CAR  = lambda p: p(TRUE)
CDR  = lambda p: p(FALSE)

# The Billion Dollar Mistake
NULL   = lambda _: TRUE
ISNULL = lambda _: lambda _: FALSE
