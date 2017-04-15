#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def check_make_rect(cake, r1, c1, r2, c2):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if cake[i][j] != '?':
                return False
    return True

def fill(cake, c, r1, c1, r2, c2):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cake[i][j] = c

def is_all_filled(cake):
    for i in range(len(cake)):
        for j in range(len(cake[i])):
            if cake[i][j] == '?':
                return False
    return True
    

def solve(R, C, cake):
    letters = {}
    for i in range(R):
        for j in range(C):
            c = cake[i][j] 
            if c != '?':
                if c not in letters:
                    letters[c] = [[i,j],[i,j]]
                else:
                    if i < letters[c][0][0]:
                        letters[c][0][0] = i
                    if i > letters[c][1][0]:
                        letters[c][1][0] = i
                    if j < letters[c][0][1]:
                        letters[c][0][1] = j
                    if j > letters[c][1][1]:
                        letters[c][1][1] = j

    for c in letters:
        fill(cake, c, letters[c][0][0], letters[c][0][1], letters[c][1][0], letters[c][1][1])

    count = 0
    while not is_all_filled(cake):
        count += 1
        if count > 100:
            print 'infinit loop'
            for k in range(R):
                print ''.join(cake[k])

            sys.exit(1)
        for c in letters:
            l = letters[c]
            # top
            if l[0][0] > 0:
                if check_make_rect(cake, l[0][0]-1, l[0][1], l[0][0]-1, l[1][1]):
                    l[0][0] -= 1
                    fill(cake, c, l[0][0], l[0][1], l[1][0], l[1][1])
            # left
            if l[0][1] > 0:
                if check_make_rect(cake, l[0][0], l[0][1]-1, l[1][0], l[0][1]-1):
                    l[0][1] -= 1
                    fill(cake, c, l[0][0], l[0][1], l[1][0], l[1][1])
            # bottom
            if l[1][0] < R-1:
                if check_make_rect(cake, l[1][0]+1, l[0][1], l[1][0]+1, l[1][1]):
                    l[1][0] += 1
                    fill(cake, c, l[0][0], l[0][1], l[1][0], l[1][1])
            # right
            if l[1][1] < C-1:
                if check_make_rect(cake, l[0][0], l[1][1]+1, l[1][0], l[1][1]+1):
                    l[1][1] += 1
                    fill(cake, c, l[0][0], l[0][1], l[1][0], l[1][1])
            
    return cake

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (R, C) = map(int, f.readline().rstrip().split())
        cake = []
        for j in range(R):
            cake.append(list(f.readline().rstrip()))

        answer = solve(R, C, cake)
        print "Case #%d:" % (i+1)
        for k in range(R):
            print ''.join(answer[k])

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

