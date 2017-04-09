#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)

def do_act(acts, idx, use, regain, energy, gain, max_e):
    if idx >= len(acts):
        return gain
    energy = min(energy+regain, max_e)
    gain += acts[idx]*use
    max_gain = 0
    for i in range(0, energy+1):
        got = do_act(acts, idx+1, i, regain, energy-i, gain, max_e)
        if got > max_gain:
            max_gain = got
    return max_gain

def doit(E, R, acts):
    answer = 0
    for i in range(0, E+1):
        got = do_act(acts, 0, i, R, E-i, 0, E)
        if got > answer:
            answer = got
    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (E, R, N) = map(int, f.readline().rstrip().split())
        acts = map(int, f.readline().rstrip().split())
        answer = doit(E, R, acts)
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
#
# array = [[0 for j in range(m)] for i in range(n)]

