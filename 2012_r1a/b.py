#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def cleanup(star, rs, starlevel, cleared):
    for i in range(len(star[rs])-1, -1, -1):
        level = star[rs][i]
        if cleared[starlevel][level] == 1:
            del star[rs][i]
    if len(star[rs]) == 0:
        del star[rs]

def solveit(N, levels):
    star = 0
    answer = 0
    while True:
        found = False
        exist_not_cleared = False
        # at first try to complete with 2 stars
        for level in levels:
            if star >= level[1]:
                # comlete it !
                answer += 1
                star += (2 if star >= level[0] else 1)
                level[1] = sys.maxint
                found = True
                break
            elif level[1] != sys.maxint:
                exist_not_cleared = True
        if found:
            continue
        elif not exist_not_cleared:
            break

        # second, try to complete with 1 star
        reserve = None
        max2star = 0
        for level in levels:
            if star >= level[0] and level[1] != sys.maxint:
                if level[1] >= max2star:
                    # remember this
                    reserve = level
                    max2star = level[1]
        if reserve:
            # complete it !
            answer += 1
            star += 1
            reserve[0] = sys.maxint
        else:
            return "Too Bad"

    return str(answer)

if __name__ == '__main__':
    f = open(sys.argv[1])
    for i in xrange(1, int(f.readline())+1):
        N = int(f.readline())
        levels = []
        for j in range(N):
            levels.append([int(w) for w in f.readline().rstrip().split()])
        answer = solveit(N, levels)
        print "Case #%d: %s" % (i, answer)

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

