#!/usr/bin/env python3

from pyaspect import Advice

class Logger(Advice):
    def __init__(self, value):
        self.value = value

    def before(self, *args, **kwargs):
        print("Entering {value}".format(value=self.value))

    def after(self, *args, **kwargs):
        print("Exiting {value}".format(value=self.value))

    def exception(self, exception):
        print("Ooops ! {exception}".format(exception=exception))
        raise exception
