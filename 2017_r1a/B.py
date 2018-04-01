#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1


def try_to_make2(n, kit, N, P, recipe, packages):
    for i in range(1, N):
        for j in range(len(packages[i])):
            if recipe[i]*n*1.1 < packages[i][j] or recipe[i]*n*0.9 > packages[i][j]:
                pass
            else:
                # this can be used
                kit.append(j)
                break
        else:
            # any package not found
            return None
    return kit


def try_to_make(N, P, recipe, packages):
    # let's start with 1st ingredient
    for i in range(len(packages[0])):
        kit = []
        n = packages[0][i]/recipe[0]
        if recipe[0]*n*1.1 >= packages[0][i]:
            kit.append(i)
            ans = try_to_make2(n, kit, N, P, recipe, packages)
            if ans:
                return ans
            kit.pop()

        if recipe[0]*(n+1)*0.9 <= packages[0][i]:
            kit.append(i)
            n += 1
            ans = try_to_make2(n, kit, N, P, recipe, packages)
            if ans:
                return ans

    # any package not found
    return None
        

def solve(N, P, recipe, packages):
    answer = 0

    while True:
        kit = try_to_make(N, P, recipe, packages)
        print kit
        if kit is None or len(kit) == 0:
            return answer

        if len(kit) == N:
            # we've done
            answer += 1
    
        for i in range(len(kit)):
            packages[i].pop(kit[i])
            if len(packages[i]) == 0:
                return answer


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, P) = map(int, f.readline().rstrip().split())
        recipe = map(int, f.readline().rstrip().split())
        packages = []
        for j in range(N):
            packages.append(map(int, f.readline().rstrip().split()))

        answer = solve(N, P, recipe, packages)
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

