#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1


def solve(N, P, recipe, ingredients):
    kittbl = []
    ingtbl = []
    for i in range(N):
        kittbl.append({})
        ingtbl.append({})
        for ingredient in ingredients[i]:
            n = ingredient/recipe[i]
            ingtbl[i][ingredient] = []
            for k in range(max(0, n-1), n+1+1):
                if ingredient >= k*recipe[i]*0.9 and ingredient <= k*recipe[i]*1.1:
                    ingtbl[i][ingredient].append(k)
                    if k in kittbl[i]:
                        kittbl[i][k].append(ingredient)
                    else:
                        kittbl[i][k] = [ingredient]

    for i in range(N):
        for ingredient in ingtbl[i]:
            if len(ingtbl[i][ingredient]) == 1:
                # it must used
                n = ingtbl[i][ingredient][0]

    return 0

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

