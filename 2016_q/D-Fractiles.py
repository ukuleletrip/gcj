#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def solve(K, C, S):
    answers = []
    if C == 1:
        for i in range(K):
            answers.append(i+1)
    else:
        i = 0
        while i < K:
            answers.append(K**(C-1)*i+2)
            i += 2

    if len(answers) > S:
        return 'IMPOSSIBLE'

    return ' '.join(map(str, answers))

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (K, C, S) = map(int, f.readline().rstrip().split())
        answer = solve(K, C, S)

        print "Case #%d: %s" % (i+1, answer)


