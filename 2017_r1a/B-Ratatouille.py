#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import math

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1


def print_graph(graph):
    for i in range(len(graph)):
        print graph[i]

def dfs(graph, used, frm, to, f):
    if frm == to:
        # goal
        return f
    used[frm] = True
    for i in range(len(graph[frm])):
        if not used[i] and graph[frm][i] > 0:
            d = dfs(graph, used, i, to, min(f, graph[frm][i]))
            if d:
                graph[frm][i] -= d
                graph[i][frm] += d
                return d
    return 0

def is_crossed(n1, n2):
    if len(n1) == 0 or len(n2) == 0:
        return False
    if n1[0] > n2[1] or n2[0] > n1[1]:
        return False
    return True

def solve(N, P, recipe, ingredients):
    ingtbl = [] # array of (min, max) serving, orderd in index of package

    for i in range(N):
        ingtbl.append([])
        for j in range(P):
            g = ingredients[i][j]*100.0
            min_n = int(math.ceil(g/(recipe[i]*110)))
            max_n = int(math.floor(g/(recipe[i]*90)))
            if min_n <= max_n:
                ingtbl[i].append((min_n, max_n))
            else:
                ingtbl[i].append(())

    # create graph
    graph = [[0 for j in range(N*P+2)] for i in range(N*P+2)] # +2 means s, t
    for i in range(N):
        for j in range(P):
            if i == 0:
                # link from s for 1st ingredient
                if len(ingtbl[i][j]):
                    graph[i][1+j] = 1
            if i == N-1:
                # link to t for last ingredient
                if len(ingtbl[i][j]):
                    graph[1+i*P+j][N*P+1] = 1
                continue

            for n in range(len(ingtbl[i+1])):
                if is_crossed(ingtbl[i+1][n], ingtbl[i][j]):
                    graph[1+i*P+j][1+(i+1)*P+n] = 1
            
    #print_graph(graph)
    answer = 0
    while True:
        used = [False]*(N*P+2)
        f = dfs(graph, used, 0, N*P+1, sys.maxint)
        if f == 0:
            break
        answer += f

    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, P) = map(int, f.readline().rstrip().split())
        recipe = map(int, f.readline().rstrip().split())
        ingredients = []
        for j in range(N):
            ingredients.append(map(int, f.readline().rstrip().split()))

        answer = solve(N, P, recipe, ingredients)
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

