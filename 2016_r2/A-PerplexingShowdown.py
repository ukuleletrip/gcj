#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

#sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

MAX_N = 12
KINDS = 3

loser = { 'P' : 'R', 'R' : 'S', 'S' : 'P' }
tbl = { 'P' : [], 'R' : [], 'S' : [] }
for k in tbl:
    for i in range(MAX_N+1):
        tbl[k].append(None)
    tbl[k][0] = k

def get(k, n):
    if tbl[k][n] is not None:
        return tbl[k][n]
    a1 = get(k, n-1) + get(loser[k], n-1)
    a2 = get(loser[k], n-1) + get(k, n-1)
    a = a1 if a1 < a2 else a2
    tbl[k][n] = a
    return a

# 0=maru, 1=batsu, 2=sankaku
def get_next_kind(kind):
    if kind == 0:
        return (1, 1, 0)
    elif kind == 1:
        return (0, 1, 1)
    elif kind == 2:
        return (1, 0, 1)
    return None

def pre_solve():
    table = []
    for i in range(KINDS):
        table.append([0]*MAX_N)

    table[0][0] = 1

    for i in range(1, MAX_N):
        for j in range(KINDS):
            next_kind = get_next_kind(j)
            for k in range(len(next_kind)):
                table[k][i] += next_kind[k]*table[j][i-1]

    return table

def solve(N, P, R, S, table):
    for i in range(KINDS):
        if P == table[i%KINDS][N] and R == table[(i+1)%KINDS][N] and S == table[(i+2)%KINDS][N]:
            print 'top is %d' % (i)
            break
    else:
        return 'IMPOSSIBLE'
    return 'KUSO'

def solve2(N, R, P, S):
    for k in tbl:
        a = get(k, N)
        if a.count('R') == R and a.count('P') == P and a.count('S') == S:
            return a
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    f = open(sys.argv[1])

    table = pre_solve()
    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, R, P, S) = map(int, f.readline().rstrip().split())

        #answer = solve(N, P, R, S, table)
        answer = solve2(N, R, P, S)

        print "Case #%d: %s" % (i+1, answer)

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

