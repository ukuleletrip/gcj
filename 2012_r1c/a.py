#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def gcd(a, b):
    aa = max(a,b)
    bb = min(a,b)
    r = aa % bb
    while r:
        aa = bb
        bb = r
        r = aa % bb
    return bb

def lcm(a, b):
    g = gcd(a, b)
    return a*b/g

def is_prime(x):
    if x < 2: return False
    if x == 2: return True
    if x%2 == 0: return False
    i = 3
    while i**2 <= x:
        if x%i == 0: return False
        i += 2
    return True

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        n = int(f.readline())
        candies = map(int, f.readline().rstrip().split())

        print "Case #%d: %d" % (i+1, answer)

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1])
# items() return tapple, tapple[0] is k, tapple[1] is v
#
# import copy
# copy.copy()
# copy.deepcopy()
#
# a = [0]*100
#
# for tc in xrange(1, int(sys.stdin.readline())+1):
#   A, B = [int(w) for w in sys.stdin.readline().split()]
#   p = [float(w) for w in sys.stdin.readline().split()]

