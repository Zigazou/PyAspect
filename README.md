PyAspect
========

A small module to experiment Aspect Oriented Programming in Python 3.

Aspect Oriented Programming aims to solve the cross-cutting concerns problems
for which traditional languages do not offer a straightforward answer.

PyAspect has been developped for experimenting Aspect Oriented Programming in
Python. It is therefore simple. It uses MonkeyPatching techniques

Example
-------

The test directory contains an example which demonstrates how to apply a
cross-cutting concern without touching the source code of the module to be
patched.

To run it under Linux :

    cd test
    ./test.sh

Note
----

PyAspect does not work correctly under Python 2, especially for methods since
their handling has changed in Python 3.

