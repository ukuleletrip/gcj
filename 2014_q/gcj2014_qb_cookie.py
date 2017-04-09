#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (C, F, X) = map(float, f.readline().rstrip().split())

        n = 0
        t = 0
        while True:
            tt = C/(2+n*F)
            t_not_buy = X/(2+n*F)
            t_buy = tt+X/(2+(n+1)*F)
            if t_buy > t_not_buy:
                answer = t + t_not_buy
                break
            t += tt
            n += 1

        # l = 0
        # r = 100000
        # while r > l:
        #     n = l+(r-l)/2
        #     not_buy = X/(2+(n-1)*F)
        #     buy = X/(2+nF)+C/(2+(n-1)*F)
        #     if not_buy <= buy:
        #         r = n
        #     else:
        #         l = n
        
        print "Case #%d: %f" % (i+1, answer)


