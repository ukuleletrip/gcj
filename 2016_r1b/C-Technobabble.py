#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def solve(entries):
    list1 = {}
    list2 = {}
    for entry in entries:
        if entry[0] not in list1:
            list1[entry[0]] = 0
        list1[entry[0]] += 1

        if entry[1] not in list2:
            list2[entry[1]] = 0
        list2[entry[1]] += 1

    dlist = {}
    for i in range(len(entries)):
        entry = entries[i]
        if list1[entry[0]] + list2[entry[1]] not in dlist:
            dlist[list1[entry[0]] + list2[entry[1]]] = []
        dlist[list1[entry[0]] + list2[entry[1]]].append(entry)

    s_dlist = []
    for k, vs in sorted(dlist.items()):
        for v in vs:
            s_dlist.append(v)

    if len(s_dlist) == 0:
        return 0

    answer = 0
    list1 = {}
    list2 = {}
    for v in s_dlist:
        if v[0] in list1 and v[1] in list2:
            answer += 1
            
        if v[0] not in list1:
            list1[v[0]] = 0

        if v[1] not in list2:
            list2[v[1]] = 0

    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        entries = []
        for j in range(N):
            entries.append(f.readline().rstrip().split())
        answer = solve(entries)
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

