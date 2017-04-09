#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import struct
import copy

def revbit(outlets, pos):
    for i in range(len(outlets)):
        outlets[i] ^= 1<<pos

def count_diff_bit(outlets, devices, L, N):
    diffs = 0
    for i in range(N):
        for j in range(L):
            if outlets[i]&(1<<j) != devices[i]&(1<<j):
                diffs += 1
    return diffs

def check(outlets, devices, pos, is_switch, N):
    o_set = set()
    d_set = set()
    mask = 0

    if is_switch:
        #outlets_ = copy.deepcopy(outlets)
        revbit(outlets, pos)
        outlets_ = outlets

    for i in range(pos+1):
        mask |= 1<<i

    for i in range(N):
        if is_switch:
            outlet = outlets_[i]^(1<<pos)
        else:
            outlet = outlets[i]
        o_set.add(outlet&mask)
        d_set.add(devices[i]&mask)
    wrong = o_set ^ d_set
    return len(wrong) == 0

def try_maybe(outlets, devices, maybe, pos, N, times):
    if pos >= len(maybe):
        return 0
    
    outlets_ = copy.deepcopy(outlets)
    if check(outlets_, devices, maybe[pos], True, N):
        revbit(outlets, maybe[pos])
        return times + 1
    else:
        rv1 = try_maybe(outlets, devices, maybe, pos+1, N, times)
        revbit(outlets, maybe[pos])
        rv2 = try_maybe(outlets, devices, maybe, pos+1, N, times+1)
        if rv1 == 0 and rv2 == 0:
            return 0
        if rv1 == 0 or rv2 == 0:
            return rv1+rv2
        return min(rv1, rv2)

def solve(outlets, devices, L, N):
    # for each bit
    answer = 0
    maybe = []
    for i in range(L):

        xor_pattern = 1<<i
        num_1_o = 0
        num_1_d = 0
        for j in range(N):
            if outlets[j]&xor_pattern:
                num_1_o += 1
            if devices[j]&xor_pattern:
                num_1_d += 1

        if num_1_o == num_1_d:
            if num_1_o == N-num_1_o:
                # can switch
                if check(outlets, devices, i, False, N):
                    maybe.append(i)
                elif check(outlets, devices, i, True, N):
                    answer += 1
                else:
                    # try maybe bits
                    more = try_maybe(outlets, devices, maybe, 0, N, 0)
                    if more:
                        answer += more
                    else:
                        return None
            else:
                # must not switch
                if not check(outlets, devices, i, False, N):
                    more = try_maybe(outlets, devices, maybe, 0, N, 0)
                    if more:
                        answer += more
                    else:
                        return None
        else:
            if num_1_o == N-num_1_d:
                # must switch
                if not check(outlets, devices, i, True, N):
                    more = try_maybe(outlets, devices, maybe, 0, N, 0)
                    if more:
                        answer += more
                    else:
                        return None
                answer += 1
            else:
                # impossible
                return None
            
    return answer

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, L) = map(int, f.readline().rstrip().split())
        outlets = map((lambda x: int(x,2)), f.readline().rstrip().split())
        devices = map((lambda x: int(x,2)), f.readline().rstrip().split())
        
        answer = solve(outlets, devices, L, N)
        answer_s = 'NOT POSSIBLE' if answer is None else str(answer)

        print "Case #%d: %s" % (i+1, answer_s)
        
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

