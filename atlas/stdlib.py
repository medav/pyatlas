from .. import model
from .primops import *
from .base import *
from .signal import *
import math
from contextlib import contextmanager

__all__ = [
    'Log2Floor',
    'Log2Ceil',
    'Cat',
    'Enum',
    'otherwise'
]

def Log2Floor(n):
    return int(math.floor(math.log2(n)))

def Log2Ceil(n):
    return int(math.ceil(math.log2(n)))

def Cat(signals):
    if len(signals) == 1:
        return signals[0]

    elif len(signals) == 2:
        n = Node('cat', signals)
        CurrentContext().AddNode(n)
        return n

    else:
        half = int(len(signals) / 2)
        n1 = Cat(signals[:half])
        n2 = Cat(signals[half:])
        return Cat([n1, n2])

class Enum():
    def __init__(self, _ids):
        self.count = len(_ids)
        self.bitwidth = Log2Ceil(self.count)

        i = 0
        for id in _ids:
            self.__dict__[id] = Const(i, self.bitwidth, False)
            i += 1

class OtherwiseObject(object):
    def __init__():
        pass

    def __enter__():
        self.signal = PreviousCondition()
        StartCondition(~self.signal)

    def __exit__(**kwargs):
        EndCondition(self.signal)

otherwise = OtherwiseObject()