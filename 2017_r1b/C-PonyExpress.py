#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

dp = None

def dfs(E, S, horses, i, cities, G):
    global dp

    if (E, S, i) in dp:
        return dp[(E, S, i)]

    if i == G:
        # goal !
        return 0

    h = sys.maxint
    for j in range(len(cities[i])):
        if cities[i][j] > 0:
            if E >= cities[i][j]:
                # can continue to ride this horse
                h = dfs(E-cities[i][j], S, horses, 
                        j, cities, G)+float(cities[i][j])/S

            h = min(dfs(horses[i][0]-cities[i][j], horses[i][1], horses, 
                        j, cities, G)+float(cities[i][j])/horses[i][1], h)
            break

    dp[(E, S, i)] = h
    return h

def solve(N, Q, horses, cities, routes):
    global dp

    answer = []

    for route in routes:
        s = route[0]-1
        g = route[1]-1
        dp = {}
        for j in range(len(cities[s])):
            if cities[s][j] > 0:
                answer.append(dfs(horses[s][0]-cities[s][j], horses[s][1], horses,
                                  j, cities, g)+float(cities[s][j])/horses[s][1])
                break

    return answer


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, Q) = map(int, f.readline().rstrip().split())
        horses = []
        cities = []
        routes = []
        for j in range(N):
            horses.append(map(int, f.readline().rstrip().split()))
        for j in range(N):
            cities.append(map(int, f.readline().rstrip().split()))
        for j in range(Q):
            routes.append(map(int, f.readline().rstrip().split()))
            
        answer = solve(N, Q, horses, cities, routes)

        print "Case #%d: %s" % (i+1, ' '.join(map(str, answer)))

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

