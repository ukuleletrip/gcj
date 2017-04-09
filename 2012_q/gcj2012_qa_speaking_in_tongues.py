#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

googlerese_sample = [ "ejp mysljylc kd kxveddknmc re jsicpdrysi",
                      "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                      "de kr kd eoya kw aej tysr re ujdr lkgc jv" ]
normal_sample = [ "our language is impossible to understand",
                  "there are twenty six factorial possibilities",
                  "so it is okay if you want to just give up" ]

tr_table = { 'y' : 'a' , 'e' : 'o', 'q' : 'z', ' ' : ' ' }

def find_non_exist_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        if not alphabet[i] in tr_table:
            non_key = alphabet[i]
            break
    for i in range(len(alphabet)):
        if not alphabet[i] in tr_table.values():
            non_value = alphabet[i]
            break
    tr_table[non_key] = non_value

def create_tr_table():
    for i in range(len(googlerese_sample)):
        for j in range(len(googlerese_sample[i])):
            cg = googlerese_sample[i][j]
            cn = normal_sample[i][j]
            if not cg in tr_table:
                tr_table[cg] = cn
    find_non_exist_alphabet()
    #print tr_table
    #print len(tr_table)

def solveit(googlerese):
    answer = ''
    for i in range(len(googlerese)):
        cg = googlerese[i]
        if not cg in tr_table:
            print "it cannot be solved... %s" % (cg)
            return None
        answer += tr_table[cg]
    return answer

if __name__ == '__main__':

    create_tr_table()

    f = open(sys.argv[1])
    num_of_case = int(f.readline())
    for i in range(num_of_case):
        #n = int(f.readline().rstrip())
        #candies = map(int, f.readline().rstrip().split())
        answer = solveit(f.readline().rstrip())
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

