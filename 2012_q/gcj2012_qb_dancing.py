#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def possible_max(score, surprising):
    rest = score%3
    avg = score/3
    if rest == 0:
        return avg+1 if surprising and score > 0 else avg
    elif rest == 1:
        return avg+1
    else:
        return avg+2 if surprising else avg+1

def possible_over(score, surprising, p):
    return 1 if possible_max(score, surprising) >= p else 0

def next(scores, i, rest_surprising, p, answer):
    if i >= len(scores):
        return answer

    use_surprising = 0
    if rest_surprising and scores[i]%3 != 1:
        use_surprising = next(scores, i+1, rest_surprising-1, p, answer + possible_over(scores[i], True, p))
    no_surprising = next(scores, i+1, rest_surprising, p, answer + possible_over(scores[i], False, p))

    return max(no_surprising, use_surprising)

def solveit(scores, num_surprising, p):
    return next(scores, 0, num_surprising, p, 0)

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        params = map(int, f.readline().rstrip().split())
        num_googlers = params[0]
        num_surprising = params[1]
        p = params[2]
        scores = params[3:]
        answer = solveit(scores, num_surprising, p)

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

