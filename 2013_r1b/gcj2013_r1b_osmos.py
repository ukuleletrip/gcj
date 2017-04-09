#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def doit(A, motes):
    answer = 0
    i = 0
    while i < len(motes):
        if A > motes[i]:
            A += motes[i]
            i += 1
        elif A+(A-1) > motes[i]:
            A += (A-1)
            answer += 1
        else:
            answer += 1
            i += 1
    return answer

def doit2(A, motes, idx, proc):
    if proc > len(motes):
        return sys.maxint

    if idx >= len(motes):
        return proc

    if A > motes[idx]:
        return min(doit2(A, motes, idx+1, proc+1), doit2(A+motes[idx], motes, idx+1, proc))
    elif A+(A-1) > motes[idx]:
        return doit2(A+A-1, motes, idx, proc+1)
    else:
        if A > 1:
            return min(doit2(A, motes, idx+1, proc+1), doit2(A+A-1, motes, idx, proc+1))
        else:
            return doit2(A, motes, idx+1, proc+1)

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (A, N) = map(int, f.readline().rstrip().split())
        motes = map(int, f.readline().rstrip().split())
        #answer = doit(A, sorted(motes))
        answer = doit2(A, sorted(motes), 0, 0)
        print "Case #%d: %d" % (i+1, answer)

