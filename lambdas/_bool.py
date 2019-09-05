IDENTITY = lambda a: a
IF = IDENTITY

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
