#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def can_put_model(stage, r, c, model):
    # check row
    out = 0
    if model != '+':
        for i in range(len(stage[r])):
            if i == c:
                continue
            if stage[r][i] == 'x' or stage[r][i] == 'o':
                return False
        for i in range(len(stage)):
            if i == r:
                continue
            if stage[i][c] == 'x' or stage[i][c] == 'o':
                return False

    # check diagonals
    if model != 'x':
        r_ = r - min(r, len(stage[0])-1-c)
        c_ = c + min(r, len(stage[0])-1-c)
        while r_ < len(stage) and c_ >= 0:
            if r_ == r and c_ == c:
                pass
            elif stage[r_][c_] == '+' or stage[r_][c_] == 'o':
                return False
            r_ += 1
            c_ -= 1

        r_ = r - min(r, c)
        c_ = c - min(r, c)
        while r_ < len(stage) and c_ < len(stage[0]):
            if r_ == r and c_ == c:
                pass
            elif stage[r_][c_] == '+' or stage[r_][c_] == 'o':
                return False
            r_ += 1
            c_ += 1
        
    return True

def calc_style_points(stage):
    points = 0
    for r in range(len(stage)):
        points += (stage[r].count('o')*2 + stage[r].count('x') + stage[r].count('+'))
    return points

def solve(N, models):
    ops = []
    stage = []
    for i in range(N):
        stage.append(['.']*N)

    for model in models:
        stage[model[1]-1][model[2]-1] = model[0]

    # try o
    for r in range(len(stage)):
        for c in range(len(stage[r])):
            if stage[r][c] == 'o':
                continue
            if can_put_model(stage, r, c, 'o'):
                stage[r][c] = 'o'
                ops.append('o %d %d' % (r+1, c+1))

    # try + or x
    for r in range(len(stage)):
        for c in range(len(stage[r])):
            if stage[r][c] != '.':
                continue
            if can_put_model(stage, r, c, 'x'):
                stage[r][c] = 'x'
                ops.append('x %d %d' % (r+1, c+1))
                continue
            if can_put_model(stage, r, c, '+'):
                stage[r][c] = '+'
                ops.append('+ %d %d' % (r+1, c+1))

    return (calc_style_points(stage), ops)
            

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        models = []
        (N, M) = map(int, f.readline().rstrip().split())
        for j in range(M):
            (model, r, c) = f.readline().rstrip().split()
            models.append((model, int(r), int(c)))

        (points, ops) = solve(N, models)
        print "Case #%d: %d %d" % (i+1, points, len(ops))
        for op in ops:
            print op

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

