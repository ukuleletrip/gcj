#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def solve(N):
    if N > 0:
        i = 1
        digits = 0
        while True:
            n = N*i
            while n > 0:
                digits |= 1<<(n%10)
                if digits == 0x3ff:
                    return str(N*i)
                n /= 10
            i += 1

    return 'INSOMNIA'

if __name__ == '__main__':
    for i in range(1000000):
        answer = solve(i)
        print "Case #%d: %s" % (i+1, answer)


