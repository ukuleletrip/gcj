#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def solveit(K, S):
    digits = "123456789"
    answer = ""
    prefix = ""
    for i in digits:
        idx = 0
        candidates = []
        answers = []
        while True:
            idx = S.find(i, idx)
            if idx < 0 or idx+K > len(S):
                break
            substr = S[idx:idx+K]
            idx += 1
            if substr in candidates:
                if substr not in answers:
                    answers.append(substr)
            else:
                candidates.append(substr)

        for a in sorted(answers):
            answer += prefix + str(a)
            prefix = " "

    if len(answer) == 0:
        answer = "NONE"
    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        params = f.readline().rstrip().split()
        answer = solveit(int(params[0]), params[1])
        print "Case #%d: %s" % (i+1, answer)

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

