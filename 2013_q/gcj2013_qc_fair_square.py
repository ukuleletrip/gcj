#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def is_palindrome(n):
    ns = str(n)
    for i in range(len(ns)/2):
        if ns[i] != ns[len(ns)-i-1]:
            return False
    return True

def create_fair_and_square(s, e):
    fss = []
    for n in range(s, e+1):
        if is_palindrome(n):
            nn = n*n
            if is_palindrome(nn):
                fss.append(nn)
    print fss

# >>> create_fair_and_square(1,100)
#fss = [1, 4, 9, 121, 484]
# >>> create_fair_and_square(1,10000000)
fsstbl = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        s, e = map(int, f.readline().rstrip().split())
        answer = 0
        for j in range(len(fsstbl)):
            if fsstbl[j] >= s and fsstbl[j] <= e:
                answer += 1
        print "Case #%d: %d" % (i+1, answer)


