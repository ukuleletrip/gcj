#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def print_garden(garden):
    for r in garden:
        print ''.join(r)

def is_lover(courties, a, b):
    idx_a = courties.index(a)
    idx_b = courties.index(b)
    return (idx_a&~0x1) == (idx_b&~0x1)

def set_hedge(garden, hedge, r, c):
    if garden[r][c] != '.' and garden[r][c] != hedge:
        return False
    garden[r][c] = hedge
    return True

def solve(R, C, courties):
    garden = []
    for i in range(R):
        garden.append(['.']*C)

    # decide corners
    # top left
    hedge = '/' if is_lover(courties, 1, R*2+C*2) else '\\'
    if not set_hedge(garden, hedge, 0, 0):
        return None

    # top right
    hedge = '\\' if is_lover(courties, C, C+1) else '/'
    if not set_hedge(garden, hedge, 0, C-1):
        return None

    # bottom left
    hedge = '\\' if is_lover(courties, C*2+R, C*2+R+1) else '/'
    if not set_hedge(garden, hedge, R-1, 0):
        return None

    # bottom right
    hedge = '/' if is_lover(courties, R+C+1, R+C) else '\\'
    if not set_hedge(garden, hedge, R-1, C-1):
        return None

    return garden

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (R, C) = map(int, f.readline().rstrip().split())
        courtiers = map(int, f.readline().rstrip().split())

        garden = solve(R, C, courtiers)

        print "Case #%d:" % (i+1)
        if garden is None:
            print 'IMPOSSIBLE'
        else:
            print_garden(garden)

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
#
# array = [[0 for j in range(m)] for i in range(n)]

