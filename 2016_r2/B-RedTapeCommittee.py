#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def get_probability(num_no, num_yes, members):
    yp = 1.0
    np = 1.0
    for i in range(num_no):
        yp *= (1-members[i])
        np *= members[i]
    for i in range(num_yes):
        yp *= members[len(members)-1-i]
        np *= (1-members[len(members)-1-i])
    return yp+np

def solve(K, members):
    maxp = 0
    for i in range(1, K):
        # i is number of 'NO' person
        p = get_probability(i, K-i, members)
        if p > maxp:
            maxp = p
    return maxp

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, K) = map(int, f.readline().rstrip().split())
        members = map(float, f.readline().rstrip().split())

        answer = solve(K, sorted(members))

        print "Case #%d: %f" % (i+1, answer)

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

