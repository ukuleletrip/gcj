#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1



def get_row(stage, r):
    return stage[r]

def get_column(stage, c):
    column = []
    for row in stage:
        column.append(row[c])
    return column

def get_diagonals(stage, r_, c_):
    # right upper to left down
    l_line = []
    r = r_ - min(r_, len(stage[0])-1-c_)
    c = c_ + min(r_, len(stage[0])-1-c_)
    while r < len(stage) and c >= 0:
        l_line.append(stage[r][c])
        r += 1
        c -= 1

    # left upper to right down
    r_line = []
    r = r_ - min(r_, c_)
    c = c_ - min(r_, c_)
    while r < len(stage) and c < len(stage[0]):
        r_line.append(stage[r][c])
        r += 1
        c += 1

    return (l_line, r_line)

def is_at_least_one_of_two(line, legal_model):
    num_blanks = line.count('.')
    num_models = len(line)-num_blanks
    if num_models < 2:
        return True

    num_legal_models = line.count(legal_model)
    return (num_models-num_legal_models <= 1)


def is_legal_model(stage, r, c):
    # check the row
    row = get_row(stage, r)
    if not is_at_least_one_of_two(row, '+'):
        return False

    # check the column
    column = get_column(stage, c)
    if not is_at_least_one_of_two(column, '+'):
        return False

    # check the diagonals
    diagonals = get_diagonals(stage, r, c)
    for d in diagonals:
        if not is_at_least_one_of_two(d, 'x'):
            return False

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
            org = stage[r][c]
            if org == 'o':
                continue
            stage[r][c] = 'o'
            if is_legal_model(stage, r, c):
                ops.append('o %d %d' % (r+1, c+1))
            else:
                stage[r][c] = org

    # try + or x
    for r in range(len(stage)):
        for c in range(len(stage[r])):
            org = stage[r][c]
            if org != '.':
                continue
            stage[r][c] = 'x'
            if is_legal_model(stage, r, c):
                ops.append('x %d %d' % (r+1, c+1))
                continue
            else:
                stage[r][c] = '+'
                if is_legal_model(stage, r, c):
                    ops.append('+ %d %d' % (r+1, c+1))
                    continue
                else:
                    stage[r][c] = org

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

