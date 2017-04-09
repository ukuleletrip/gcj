#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

MAX_DINERS = 1000

def next_bottle_neck(spect, idx):
    for i in reversed(range(idx)):
        if spect[i] != 0:
            return i+1
    return 0

def create_spect(cakes):
    spect = [0]*MAX_DINERS
    for n in cakes:
        spect[n-1] += 1
    return spect

def solve(cakes):
    spect = create_spect(cakes)
    answer = 0
    rest_max = max(cakes)
    for i in reversed(range(MAX_DINERS)):
        if spect[i] != 0:
            n = i+1
            nbn = next_bottle_neck(spect, i)
            if n/2 + n%2 > nbn and n - (n/2 + n%2) > spect[i]:
                # do it !
                answer += spect[i]
                spect[n/2 + n%2 - 1] += spect[i]
                spect[n/2 - 1] += spect[i]
                spect[i] = 0
                rest_max = n/2 + n%2
            else:
                break
        
    answer += rest_max
    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        n = int(f.readline())
        cakes = map(int, f.readline().rstrip().split())
        answer = solve(cakes)
        print "Case #%d: %d" % (i+1, answer)


