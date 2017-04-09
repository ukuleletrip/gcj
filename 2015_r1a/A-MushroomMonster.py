#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def solveit(mushrooms):
    p_mrs = -1
    max_inc = 0
    answer1 = 0
    for n in mushrooms:
        if p_mrs >= 0 and p_mrs > n:
            max_inc = max(max_inc, p_mrs - n)
            answer1 += (p_mrs - n)
        p_mrs = n

    answer2 = 0
    for n in mushrooms[:-1]:
        answer2 += min(n, max_inc)
        
    return (answer1, answer2)
        

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        n = int(f.readline())
        mushrooms = map(int, f.readline().rstrip().split())
        answers = solveit(mushrooms)

        print "Case #%d: %d %d" % (i+1, answers[0], answers[1])

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

