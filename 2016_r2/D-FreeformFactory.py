#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import itertools

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def do():
    for i in range(N):
        if skill[i] == '1':
            push()


def is_good(N, workers):
    queue = []
    queue.append([])
    while len(queue) != 0:
        a = queue.pop(0)
        if len(a) == N:
            continue

        skill = workers[len(a)]
        is_found = False
        for i in range(N):
            if not i in a and skill[i] == '1':
                # can operate this!
                is_found = True
                queue.append(a+[i])
        if not is_found:
            return False

    return True

def is_good_in_all_order(N, workers):
    for order in itertools.permutations(range(N)):
        ordered_workers = []
        for i in order:
            ordered_workers.append(workers[i])
        if not is_good(N, ordered_workers):
            return False
    return True

def bitmap_to_workes(N, bitmap):
    workers = []
    for i in range(N):
        workers.append([' ']*N)

    for i in range(N*N):
        workers[i/N][i%N] = '1' if bitmap&(1<<i) else '0'

    return workers

def count_diffs(N, w1, w2):
    diffs = 0
    for i in range(N):
        for j in range(N):
            if w1[i][j] != w2[i][j]:
                diffs += 1
    return diffs

def solve(N, workers):
    answer = N*N
    for b in range(1<<N*N):
        cand = bitmap_to_workes(N, b)
        for i in range(N):
            for j in range(N):
                if workers[i][j] == '1' and cand[i][j] != '1':
                    break
            else:
                continue
            break
        else:
            if is_good_in_all_order(N, cand):
                n = count_diffs(N, workers, cand)
                answer = min(answer, n)

    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        workers = []
        for j in range(N):
            workers.append(f.readline().rstrip())

        answer = solve(N, workers)
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

