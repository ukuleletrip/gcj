#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def doit(i, a, k):
    if i == len(a):
        return k == 0
    elif k == 0:
        return True

    if doit(i+1, a, k-a[i]) or doit(i+1, a, k):
        return True
    return False

def solve_recursive(n, a, k):
    return doit(0, a, k)

def solve_dp(n, a, k):
    dp = [[0 for j in range(n)] for i in range(k+1)]
    dp[0][0] = 1
    dp[1][0] = 1
    for i in range(1, n):
        for j in range(k+1):
            if dp[j][i-1] and j+a[i] <= k:
                if j+a[i] == k:
                    return True
                dp[j+a[i]][i] += 1
                dp[j][i] += 1
    return False
