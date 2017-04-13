#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

class Node(object):
    def __init__(self, hedge_i):
        self.hedge_i = i
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None

    def next(self, fm, hedges):
        if self.left == fm:
            return self.top if hedges[self.hedge_i] == '/' else self.bottom
        if self.top == fm:
            return self.left if hedges[self.hedge_i] == '/' else self.right
        if self.right == fm:
            return self.bottom if hedges[self.hedge_i] == '/' else self.top
        if self.bottom == fm:
            return self.right if hedges[self.hedge_i] == '/' else self.left

        print self.hedge_i, fm, '\n', self.left, self.top, self.right, self.bottom
        return None

def create_garden(R, C):
    nodes = [[Node(j*R+i) for i in range(C)] for j in range(R)]

    for i in range(R):
        for j in range(C):
            node = nodes[i][j]
            node.left = nodes[i][j-1] if j>0 else R*2+C+(C-i)
            node.right = nodes[i][j+1] if j<C-1 else R+i+1
            node.top = nodes[i-1][j] if i>0 else j+1
            node.bottom = nodes[i+1][j] if i<R-1 else R+C+(R-j)
            print '*', node.left, node.right, node.top, node.bottom

    return nodes

def is_connected(garden, hedges, c1, c2):
    if c1 <= R:
        node = garden[0][c1-1]
    elif c1 <= R+C:
        node = garden[c1-C-1][C-1]
    elif c1 <= R*2+C:
        node = garden[R-1][C-(c1-(R+C))]
    else:
        node = garden[R-(c1-(R*2+C))][0]
    fm = c1

    while True:
        node = node.next(fm, hedges)
        if type(node) == int:
            return node == c2
        fm = node


def solve(R, C, courties):
    garden = create_garden(R, C)
    hedges = [' ']*(R*C)
    for i in range(1<<(R*C)):
        for j in range(R*C):
            if (i>>j)&1:
                hedges[j] = '/'
            else:
                hedges[j] = '\\'

        for k in range(len(courties)/2):
            if not is_connected(garden, hedges, courties[k*2], courties[k*2+1]):
                break
        else:
            # all connected !!
            return hedges

    return None

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

