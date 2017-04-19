#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

Q1 = [[0, 3, 2, 0, 0, 0],
      [0, 0, 0, 2, 2, 0],
      [0, 0, 0, 2, 3, 0],
      [0, 0, 0, 0, 0, 3],
      [0, 0, 0, 0, 0, 2],
      [0, 0, 0, 0, 0, 0]]

Q2 = [[0, 10, 0, 2, 0],
      [0, 0, 6, 6, 0],
      [0, 0, 0, 3, 8],
      [0, 0, 0, 0, 5],
      [0, 0, 0, 0, 0]]

used = None
rev = None

def dfs(problem, frm, to, f):
    if frm == to:
        # goal
        return f
    used[frm] = True
    for i in range(len(problem[frm])):
        if not used[i] and (problem[frm][i] > 0 or rev[frm][i] > 0):
            if problem[frm][i]:
                d = dfs(problem, i, to, min(f, problem[frm][i]))
                if d:
                    problem[frm][i] -= d
                    rev[i][frm] += d
                    return d
            else:
                d = dfs(problem, i, to, min(f, rev[frm][i]))
                if d:
                    rev[frm][i] -= d
                    problem[i][frm] += d
                    return d

    return 0

def solve(problem, s, t):
    global used, rev

    rev = [[0 for j in range(len(problem[0]))] for i in range(len(problem))]
    flow = 0
    while True:
        used = [False]*len(problem)
        f = dfs(problem, s, t, sys.maxint)
        print problem, rev
        if f == 0:
            break
        flow += f

    return flow

if __name__ == '__main__':
    pass
