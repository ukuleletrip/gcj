#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1


def solve(N, K, U, cores):
    print N, K, U, cores
    for i in range(N):
        cores[i] = int(cores[i]*10000)
    U = int(U*10000)

    if N == 1:
        cores[0] += U
    else:
        i = 0
        while U:
            if i == N-1 and cores[i-1] == cores[i]:
                # all is same
                to_use = float(U)/N
                for j in range(N):
                    cores[j] += to_use
                U = 0.0
                break

            if i > 0 and cores[i-1] < cores[i]:
                to_use = min(U, cores[i]-cores[i-1])
                cores[i-1] += to_use
                U -= to_use
                i = 0
                continue

            i += 1

    print cores
    answer = 1.0
    for core in cores:
        answer *= (core/10000.0)
    return answer


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, K) = map(int, f.readline().rstrip().split())
        U = float(f.readline().rstrip())
        cores = map(float, f.readline().rstrip().split())

        answer = solve(N, K, U, sorted(cores))

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
#
# array = [[0 for j in range(m)] for i in range(n)]

