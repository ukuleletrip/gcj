#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

#sys.maxint
#-sys.maxint-1

results = [ "O won",
            "X won",
            "Draw",
            "Game has not completed" ]

# const
F_V = 0x01
F_H = 0x02
F_LX = 0x04 # -45
F_RX = 0x08 # +45

class RowDirection(object):
    def __init__(self, flag):
        self.flag = flag
    def get_1st(self, x, y, field):
        return (None, None)
    def get_next(self, x, y, field):
        return (None, None)

class Vertical(RowDirection):
    def __init__(self):
        RowDirection.__init__(self, F_V)
    def get_1st(self, x, y, field):
        return (x, 0)
    def get_next(self, x, y, field):
        return (x, y+1) if y+1 <= len(field)-1 else (None, None)

class Horizontal(RowDirection):
    def __init__(self):
        RowDirection.__init__(self, F_H)
    def get_1st(self, x, y, field):
        return (0, y)
    def get_next(self, x, y, field):
        return (x+1, y) if x+1 <= len(field[y])-1 else (None, None)

class LeftCross(RowDirection):
    def __init__(self):
        RowDirection.__init__(self, F_LX)
    def get_1st(self, x, y, field):
        return (0, 0) if x == y else (None, None)
    def get_next(self, x, y, field):
        return (x+1, y+1) if y+1 <= len(field)-1 else (None, None)

class RightCross(RowDirection):
    def __init__(self):
        RowDirection.__init__(self, F_RX)
    def get_1st(self, x, y, field):
        return (len(field)-1, 0) if x+y == len(field)-1 else (None, None)
    def get_next(self, x, y, field):
        return (x-1, y+1) if x-1 >= 0 else (None, None)

def check(field, flags, x, y, rd):
    if flags[y][x]&rd.flag:
        return False
    result = True
    (i, j) = rd.get_1st(x, y, field)
    for k in range(len(field)):
        if i is None or j is None:
            result = False
            break
        flags[j][i] |= rd.flag
        if field[j][i] != field[y][x] and field[j][i] != 'T':
            result = False
        (i, j) = rd.get_next(i, j, field)
    return result

def doit(field):
    has_empty = False
    flags = [[0 for j in range(len(field[i]))] for i in range(len(field))]
    for y in range(len(field)):
        for x in range(len(field[i])):
            if field[y][x] == 'T':
                continue
            if field[y][x] == '.':
                has_empty = True
                continue
            if check(field, flags, x, y, Vertical()) or \
                    check(field, flags, x, y, Horizontal()) or \
                    check(field, flags, x, y, LeftCross()) or \
                    check(field, flags, x, y, RightCross()):
                return 0 if field[y][x] == 'O' else 1
    return 3 if has_empty else 2

if __name__ == '__main__':
    f = open(sys.argv[1])
    num_of_case = int(f.readline())
    for i in range(num_of_case):
        field = [None]*4
        for j in range(len(field)):
            field[j] = f.readline().rstrip()
        print "Case #%d: %s" % (i+1, results[doit(field)])
        # skip empty line
        f.readline()

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

