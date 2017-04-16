#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import copy

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def solve_w(R, C, maze):
    answer = sys.maxint
    ops = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                ops.append((i, j, []))
                while len(ops):
                    op = ops.pop(0)
                    if maze[op[0]][op[1]] == '#':
                        continue
                    elif maze[op[0]][op[1]] == 'G':
                        answer = min(answer, len(op[2]))
                        continue

                    if (op[0], op[1]) in op[2]:
                        continue

                    if len(op[2]) >= answer:
                        continue

                    steps = copy.deepcopy(op[2])
                    steps.append((op[0], op[1]))
                    ops.append((op[0]-1, op[1], copy.deepcopy(steps)))
                    ops.append((op[0], op[1]-1, copy.deepcopy(steps)))
                    ops.append((op[0], op[1]+1, copy.deepcopy(steps)))
                    ops.append((op[0]+1, op[1], copy.deepcopy(steps)))
    
    return answer

def doit_d(maze, r, c, steps):
    if maze[r][c] == '#':
        return sys.maxint
    elif maze[r][c] == 'G':
        return len(steps)

    if (r, c) in steps:
        # loop
        return sys.maxint

    steps.append((r, c))
    s = sys.maxint
    s = min(s, doit_d(maze, r-1, c, steps)) # up
    s = min(s, doit_d(maze, r, c-1, steps)) # left
    s = min(s, doit_d(maze, r, c+1, steps)) # right
    s = min(s, doit_d(maze, r+1, c, steps)) # down
    steps.pop()
    return s

def solve_d(R, C, maze):
    answer = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                answer = doit_d(maze, i, j, [])
                return answer


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (R, C) = map(int, f.readline().rstrip().split())
        maze = [['#' for c in range(C+2)] for r in range(R+2)]
        for j in range(R):
            row = list(f.readline().rstrip())
            for k in range(C):
                maze[j+1][k+1] = row[k]

        answer = solve_w(R, C, maze)
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

