#!/usr/bin/env python3

from functions import dummy1, dummy2, Dummy
from weaving import weave
weave()

from pprint import pprint

print(Dummy.__dict__)

dummy = Dummy()
dummy.dummy()

dummy1("Frédéric", "Bisson")
dummy2("Frédéric", "Bisson")

