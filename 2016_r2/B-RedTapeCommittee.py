#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def test_bitcount_bf(a, k):
    for i in range(1<<len(a)):
        sel = []
        for j in range(len(a)):
            if (i>>j)&1:
                sel.append(a[j])
        if len(sel) != k:
            continue
        print sel

dp = None
def calcit(i, n_yes, committees):
    if i == len(committees):
        return 1.0 if n_yes == 0 else 0.0

    global dp
    if dp and dp[i][n_yes] >= 0:
        return dp[i][n_yes]

    p = calcit(i+1, n_yes, committees)*committees[i]
    if n_yes != 0:
        p += calcit(i+1, n_yes-1, committees)*(1-committees[i])

    dp[i][n_yes] = p
    return p

def doit(i, k, members, committees):
    if len(members)-i < k:
        # cut branch
        return 0
    if i == len(members) or k == 0:
        if k == 0:
            rv = calcit(0, len(committees)/2, committees)
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

def get_probability(n, K, members):
    committees = []
    for i in range(n):
        committees.append(members[i])

    for i in range(K-n):
        committees.append(members[len(members)-1-((K-n)-1-i)])

    global dp
    dp = []
    for i in range(len(committees)):
        dp.append([-1]*len(committees))

    return calcit(0, len(committees)/2, committees)

def solve(K, members):
    maxp = 0
    for i in range(K+1):
        # i is number of 'NO' person
        p = get_probability(i, K, members)
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
        #answer = bf_solve(K, sorted(members))

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

