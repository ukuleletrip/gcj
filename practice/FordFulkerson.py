#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

# http://even-eko.hatenablog.com/entry/2013/08/08/195120 was helpful

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

def dfs(problem, used, frm, to, f):
    if frm == to:
        # goal
        return f
    used[frm] = True
    for i in range(len(problem[frm])):
        if not used[i] and problem[frm][i] > 0:
            d = dfs(problem, used, i, to, min(f, problem[frm][i]))
            if d:
                problem[frm][i] -= d
                problem[i][frm] += d
                return d
    return 0

def solve(problem, s, t):
    flow = 0
    while True:
        used = [False]*len(problem)
        f = dfs(problem, used, s, t, sys.maxint)
        print problem
        if f == 0:
            break
        flow += f

    return flow

if __name__ == '__main__':
    pass
