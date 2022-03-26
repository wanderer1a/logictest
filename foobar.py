#!/usr/bin/env python

def foobar():
    for i in range(1, 101):
        printable = True
        if i % 3 == 0:
            printable = False
            print('foo', end='')
        if i % 5 == 0:
            printable = False
            print('bar', end='')
        if printable:
            print(f'{i}', end='')
        if i < 100:
            print(', ', end='')


if __name__ == '__main__':
    foobar()
