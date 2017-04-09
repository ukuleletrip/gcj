#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def solveit(scores, num_surprising, p):
    absolutely_ok = 0
    surprising_ok = 0
    for score in scores:
        rest = score%3
        avg = score/3
        if rest == 0:
            if avg >= p:
                absolutely_ok += 1
            elif avg+1 >= p and score > 0:
                surprising_ok += 1
        elif rest == 1:
            if avg+1 >= p:
                absolutely_ok += 1
        else:
            if avg+1 >= p:
                absolutely_ok += 1
            elif avg+2 >= p:
                surprising_ok += 1

    return absolutely_ok + min(surprising_ok, num_surprising)

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        params = map(int, f.readline().rstrip().split())
        num_googlers = params[0]
        num_surprising = params[1]
        p = params[2]
        scores = params[3:]
        answer = solveit(scores, num_surprising, p)

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

