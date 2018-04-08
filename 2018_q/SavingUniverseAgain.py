#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

#sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def calc_damage(P):
    damage = 0
    strength = 1
    for op in P:
        if op == 'S':
            damage += strength
        elif op == 'C':
            strength *= 2
    return damage

def count_(P):
    tbl = {}
    count_c = 0
    for op in P:
        if op == 'S':
            if count_c not in tbl:
                tbl[count_c] = 0
            tbl[count_c] += 1
        elif op == 'C':
            count_c += 1
    return tbl

def solve(D, P):
    damage = calc_damage(P)
    tbl = count_(P)
    count = 0
    while damage > D:
        r = sorted(tbl.items(), reverse=True)
        if len(r) == 0 or r[0][0] == 0:
            break

        damage -= pow(2, r[0][0]-1)
        tbl[r[0][0]] -= 1
        if tbl[r[0][0]] == 0:
            tbl.pop(r[0][0])

        if r[0][0]-1 not in tbl:
            tbl[r[0][0]-1] = 0
        tbl[r[0][0]-1] += 1
        count += 1

    return count if damage <= D else 'IMPOSSIBLE'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = sys.stdin

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        elms = f.readline().rstrip().split()
        answer = solve(int(elms[0]), list(elms[1]))
        print("Case #{}: {}".format(i+1, answer), file=sys.stdout)

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1], reverse=True)
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

