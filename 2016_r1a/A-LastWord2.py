#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def solve(S):
    answer = [S[0]]
    for i in range(1, len(S)):
        if S[i] >= answer[0]:
            answer.insert(0, S[i])
        else:
            answer.append(S[i])
    return ''.join(answer)


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        S = f.readline().rstrip()
        answer = solve(S)

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
#
# array = [[0 for j in range(m)] for i in range(n)]

