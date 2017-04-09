#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def put_h(l, pos, cells, N):
    for i in range(N):
        if cells[pos*N+i] != -1 and cells[pos*N+i] != l[i]:
            # cannot do that !
            return False
    for i in range(N):
        cells[pos*N+i] = l[i]
    return True
            

def put_v(l, pos, cells, N):
    for i in range(N):
        if cells[i*N+pos] != -1 and cells[i*N+pos] != l[i]:
            # cannot do that !
            return False
    for i in range(N):
        if cells[i*N+pos] = l[i]
    return True

def solve(N, lists):
    cells = [-1]*(N*N)
    
    order_l = {}
    for l in lists:
        if l[0] not in order_l:
            order_l[l[0]] = []
        order_l[l[0]].append(l)

    pos = 0
    i = 0
    for k,ls in sorted(order_l.items()):
        for l in ls:
            if i%2 == 0:
                if !put_h(l, pos, cells, N):
                    #
                    pass
            else:
                if !put_v(l, pos, cells, N):
                    #
                    pass
            

    return lists[0]


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        N = int(f.readline())
        lists = []
        for j in range(N*2-1):
            lists.append(map(int, f.readline().rstrip().split()))

        answer = solve(N, lists)
        
        print "Case #%d: %s" % (i+1, ' '.join(map(str, answer)))

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

