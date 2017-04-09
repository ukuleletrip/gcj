#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import math

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def solveit(D, TXs, As):
    answers = [0.0]*len(As)

    # [TODO]N can be 1???, t0 must be0, xN-1 must be greater than D
    for i in range(len(As)):
        pp_me = 0
        pv_me = 0
        ppos = 0
        ptime = 0
        for j in range(0,len(TXs)):
            pos = TXs[j][1]
            d = pos-ppos
            v_other = 0 if j == 0 else (d/(TXs[j][0]-TXs[j-1][0]))
            if pos > D:
                t_other = 0 if v_other == 0 else (TXs[j-1][0] + (D-TXs[j-1][1])/v_other)


            # time to reach jth position
            t_me = math.sqrt(D*2/As[i])
            # jth position of me
            t = TXs[j][0]-TXs[j-1][0]
            p1 = pp_me + pv_me*t + 0.5*As[i]*t*t
            # jth position of other car
            
        #vcar = 
        #pcar = TXs[0][1] + vcar*t
        t = 
        answers[i] = t

    return answers

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        params = f.readline().rstrip().split()
        D = float(params[0])
        N = int(params[1])
        A = int(params[2])
        TXs = []
        for j in range(N):
            TXs.append([float(w) for w in f.readline().split()])
        As = [float(w) for w in f.readline().split()]
        answers = solveit(D, TXs, As)
        print "Case #%d:" % (i+1)
        for answer in answers:
            print "%f" % (answer)

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

