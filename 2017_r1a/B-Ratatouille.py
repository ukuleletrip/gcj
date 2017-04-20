#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

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

def solve(N, P, recipe, ingredients):
    kittbl = [] # key is number of serving, value is index of package
    ingtbl = [] # array of number of serving, orderd in index of package

    for i in range(N):
        kittbl.append({})
        ingtbl.append([])
        for j in range(P):
            ingredient = ingredients[i][j]
            n = ingredient/recipe[i]
            ingtbl[i].append([])
            for k in range(max(0, n-1), n+1+1):
                if ingredient >= k*recipe[i]*0.9 and ingredient <= k*recipe[i]*1.1:
                    ingtbl[i][j].append(k)
                    if k in kittbl[i]:
                        kittbl[i][k].append(j)
                    else:
                        kittbl[i][k] = [j]

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

            for n in ingtbl[i][j]:
                if n in kittbl[i+1]:
                    for k in kittbl[i+1][n]:
                        # link the node
                        graph[1+i*P+j][1+(i+1)*P+k] = 1
            
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

