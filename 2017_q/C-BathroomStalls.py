#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def put(S):
    return (max(0, S/2-(1 if S%2==0 else 0)), S/2)


def solve(N, K):
    chose = 1
    prev_min_s = N
    prev_max_s = N
    wider = 0
    while True:
        (min_min_s, min_max_s) = put(prev_min_s)
        (max_min_s, max_max_s) = put(prev_max_s)
        chose *= 2
        if K < chose:
            # all stall are chosen
            if K-chose/2 <= wider:
                return (max_min_s, max_max_s)
            else:
                return (min_min_s, min_max_s)

        if max_max_s%2 == 0:
            pass
        
        prev_min_s = min_min_s
        prev_max_s = max_max_s
    # never reach here
    return None

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, K) = map(int, f.readline().rstrip().split())

        (ans1, ans2) = solve(N, K)
        print "Case #%d: %d %d" % (i+1, ans1, ans2)

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

