#!/usr/bin/env python3

def dummy1(forename, surname):
    print("Dummy1 {forename} {surname}".format(
        forename=forename, surname=surname
    ))

def dummy2(forename, surname):
    print("Dummy2 {forename} {surname}".format(
        forename=forename, surname=surname
    ))
    
    # This will generate an exception !
    a = 1 / 0

class Dummy:
    def __init__(self):
        self.title = "dummy"

    def dummy(self):
        print("Dummy {title} !".format(title=self.title))

