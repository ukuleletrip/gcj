#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import copy

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


def calcit(i, n_yes, committees, yp, np):
    if len(committees)-i < n_yes:
        return 0
    if i == len(committees):
        return yp+np if n_yes == 0 else 0.0

    p1 = calcit(i+1, n_yes, committees, yp*(1-committees[i]), np*committees[i])
    if n_yes == 0:
        p2 = 0
    else:
        p2 = calcit(i+1, n_yes-1, committees, yp*committees[i], np*(1-committees[i]))
    return p1+p2

def get_probability_list(committees):
    if len(committees) == 0:
        return 0
    p1 = 1.0
    p2 = 1.0
    for i in range(len(committees)):
        if i < len(committees)/2:
            p1 *= (1-committees[i])
            p2 *= (committees[i])
        else:
            p1 *= committees[i]
            p2 *= (1-committees[i])
    return p1+p2

kuso = 0
def doit(i, k, members, committees):
    if len(members)-i < k:
        # cut branch
        return 0
    if i == len(members) or k == 0:
        if k == 0:
            rv = calcit(0, len(committees)/2, committees, 1.0, 1.0)/2
            return rv
        else:
            return 0.0
    
    p1 = doit(i+1, k, members, committees)
    committees.append(members[i])
    p2 = doit(i+1, k-1, members, committees)
    committees.pop()
    return max(p1, p2)


def bf_solve(K, members):
    ans = doit(0, K, members, [])
    return ans


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

        answer = bf_solve(K, sorted(members))

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

