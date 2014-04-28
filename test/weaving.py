#!/usr/bin/env python3

from functions import dummy1, dummy2, Dummy
from pyaspect import apply_advice_to
from logger import Logger

def weave():
    apply_advice_to(Logger('dummy1'), dummy1)
    apply_advice_to(Logger('dummy2'), dummy2)
    apply_advice_to(Logger('Dummy'), Dummy.dummy)

