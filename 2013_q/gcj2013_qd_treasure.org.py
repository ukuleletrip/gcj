#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import copy

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

class Key(object):
    def __init__(self, id):
        self.id = int(id)
        self.used = False
    def __repr__(self):
        return 'Key(' + str(self.id) + ',' + str(self.used) + ')'

class Chest(object):
    def __init__(self, key_id, keys):
        self.key_id = int(key_id)
        self.keys = keys
        self.opened = False
    def __repr__(self):
        return 'Chest(' + str(self.key_id) + ',' + str(self.opened) + ',' + str(self.keys) + ')'

def comp_array(a, b):
    print a,b 
    i = 0
    for i in range(len(a)):
        if i >= len(b):
            return -1
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
    if len(b) >= i:
        return 1
    return 0

def next(keys, chests, num, seq):
    print keys, chests, num, seq
    if chests[num].opened:
        return seq
    key_to_use = None
    for i in range(len(keys)):
        print keys[i], chests[num]
        if keys[i].used is False and keys[i].id == chests[num].key_id:
            print 'opened %d' % (num)
            chests[num].opened = True
            key_to_use = keys[i]
            break
    else:
        for i in range(len(chests)):
            if chests[i].opened:
                for j in range(len(chests[i].keys)):
                    if chests[i].keys[j].used is False and chests[i].keys[j].id == chests[num].key_id:
                        chests[num].opened = True
                        key_to_use = chests[i].keys[j]
                        
        return None

    key_to_use.used = True
    new_seq = copy.copy(seq)
    new_seq.append(num+1)

    min_result = None
    for j in range(len(chests)):
        result = next(keys, chests, j, new_seq)
        if result is None:
            continue
        if min_result is None or comp_array(result, min_result) < 0:
            min_result = result
        
    key_to_used = False
    chests[num].opend = False
    print key_to_used
    print chests[num]
    return min_result

def doit(keys, chests):
    min_result = None
    for i in range(len(chests)):
        result = next(keys, chests, i, [])
        if result is None:
            continue
        if min_result is None or comp_array(result, min_result) < 0:
            min_result = result
    return str(min_result)

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (K, N) = map(int, f.readline().split())
        keys = map(Key, f.readline().split())
        chests = []
        for j in range(N):
            elms = map(int, f.readline().split())
            chests.append(Chest(elms[0], map(Key, elms[2:])))
        answer = doit(keys, chests)
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

