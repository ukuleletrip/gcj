#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def flip(pancakes, i, K):
    if i+K > len(pancakes):
        return False
    for j in range(i, i+K):
        pancakes[j] = '+' if pancakes[j] == '-' else '-'
    return True

def solve(pancakes, K):
    count = 0
    while True:
        try:
            left_blank = pancakes.index('-')
        except ValueError:
            break
        if not flip(pancakes, left_blank, K):
            return None
        count += 1
    return count

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (S, K) = f.readline().rstrip().split()
        answer = solve(list(S), int(K))

        print "Case #%d: %s" % (i+1, str(answer) if answer is not None else 'IMPOSSIBLE')

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

