#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        cards = []
        r1 = int(f.readline())
        for j in range(4):
            cards.append(map(int, f.readline().rstrip().split()))
        r1_row = set(cards[r1-1])

        cards = []
        r2 = int(f.readline())
        for j in range(4):
            cards.append(map(int, f.readline().rstrip().split()))
        r2_row = set(cards[r2-1])

        union = r1_row & r2_row
        if len(union) == 0:
            answer = 'Volunteer cheated!'
        elif len(union) == 1:
            answer = str(union.pop())
        else:
            answer = 'Bad magician!'
        
        print "Case #%d: %s" % (i+1, answer)


