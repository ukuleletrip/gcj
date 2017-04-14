#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def find_list_has(lists, value, in_pos):
    results = []
    for i in range(len(lists)):
        if lists[i][in_pos] == value:
            results.append(i)
    return results

def place_list_v(field, pos, l):
    for i in range(len(l)):
        field[i][pos] = l[i]

def place_list_h(field, pos, l):
    for i in range(len(l)):
        field[pos][i] = l[i]

def solve(N, lists):
    # create field
    field = [[0 for j in range(N)] for i in range(N)]
    # create memo which represents existence of list
    memo = [[0 for j in range(N)] for i in range(2)]

    # find left-top value
    min_value = 2500
    for i in range(len(lists)):
        if lists[i][0] < min_value:
            min_value = lists[i][0]
    
    idxs = find_list_has(lists, min_value, 0)

    place_list_v(field, 0, lists[idxs[0]])
    memo[0][0] = 1

    if len(idxs) > 1:
        place_list_h(field, 0, lists[idxs[1]])
        memo[1][0] = 1

    print field

    return [1,2,3]

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        lists = []
        for j in range(2*N-1):
            lists.append(map(int, f.readline().rstrip().split()))

        answer = solve(N, lists)
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

