#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def evacuate(k, pp):
    pp[k] -= 1
#    if pp[k] == 0:
#        pp.pop(k)

def solve(N, P):
    pp = {}
    amount = 0
    for i in range(N):
        pp[chr(ord('A')+i)] = P[i]
        amount += P[i]

    opes = []
    while True:
        pps = list(dict(sorted(pp.items(), key=lambda x:x[1], reverse=True)).keys())
        if pp[pps[0]] == 0:
            break
        ope = pps[0]
        evacuate(pps[0], pp)
        amount -= 1

        if pp[pps[1]]/amount >= 0.5 and pp[pps[0]]/amount < 0.5 and \
           (len(pps) <= 2 or pp[pps[2]]/amount < 0.5):
            ope += pps[1]
            evacuate(pps[1], pp)
            amount -= 1

        opes.append(ope)

    return ' '.join(opes)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = sys.stdin

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        P = list(map(int, f.readline().rstrip().split()))

        answer = solve(N, P)

        print("Case #{}: {}".format(i+1, answer), file=sys.stdout)
        sys.stdout.flush()

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

