from ._bool import *
from ._combinators import *
from ._helpers import *
from ._list import *
from ._natural import *
from ._pair import *
from ._recursive import *
from ._signed import *


# improve repr
for name, func in globals().copy().items():
    if '_' not in name and name.isupper():
        func.__qualname__ = name
