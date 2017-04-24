#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

blended = {
    'O' : 'B',
    'G' : 'R',
    'V' : 'Y',
}

pure = [ 'B', 'Y', 'R' ]

def solve(N, R, O, Y, G, B, V):
    tbl = {
        'B' : B,
        'R' : R,
        'Y' : Y,
        'O' : O,
        'G' : G,
        'V' : V
    }

    # consolidate blended color into pure color block
    consol = {}
    for color in blended:
        if tbl[color]:
            if tbl[blended[color]] < tbl[color]:
                return 'IMPOSSIBLE'
            elif tbl[blended[color]] == tbl[color]:
                if N == tbl[blended[color]] + tbl[color]:
                    return (color + blended[color])*tbl[color]
                else:
                    return 'IMPOSSIBLE'
            
            N -= tbl[color]*2
            consol[blended[color]] =[blended[color], color]*tbl[color] + [blended[color]]
            tbl[blended[color]] -= tbl[color]
            tbl[color] = 0

    # place pure colors
    answer = []
    prev = None
    while N:
        is_progress = False
        for c in pure:
            if c != prev and tbl[c]:
                answer.append(c)
                tbl[c] -= 1
                N -= 1
                is_progress = True
                prev = c

        if not is_progress:
            break

    # try to insert
    while N:
        is_progress = False
        for c in pure:
            if tbl[c]:
                for i in range(1, len(answer)):
                    if answer[i-1] != c and answer[i] != c:
                        answer.insert(i, c)
                        tbl[c] -= 1
                        N -= 1
                        is_progress = True
                        break
        if not is_progress:
            return 'IMPOSSIBLE'

    if answer[0] == answer[-1]:
        c = answer.pop()
        for i in range(1, len(answer)):
            if answer[i-1] != c and answer[i] != c:
                answer.insert(i, c)
                break
        else:
            return 'IMPOSSIBLE'

    # extract consolidated string
    for c in consol:
        pos = answer.index(c)
        answer = answer[:pos] + consol[c] + answer[pos+1:]

    return ''.join(answer)


if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, R, O, Y, G, B, V) = map(int, f.readline().rstrip().split())
        answer = solve(N, R, O, Y, G, B, V)

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
# for tc in xrange(1, int(sys.stdin.readline())+1):
#   A, B = [int(w) for w in sys.stdin.readline().split()]
#   p = [float(w) for w in sys.stdin.readline().split()]
#
# array = [[0 for j in range(m)] for i in range(n)]

