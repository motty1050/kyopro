#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math
import bisect
import itertools
import collections
import heapq
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, product
from functools import lru_cache


import sys

input = sys.stdin.readline

def main():
    T = int(input())
    results = []
    for _ in range(T):
        N = int(input())
        S = input().strip()
        # dp[mask]: mask状態を安全に作れるか
        dp = [False] * (1 << N)
        dp[0] = True  # 空の瓶は安全
        for mask in range(1 << N):
            if not dp[mask]:
                continue
            for add in range(N):
                if not (mask & (1 << add)):
                    nmask = mask | (1 << add)
                    # Sのindexはnmask-1
                    if S[nmask - 1] == '0':
                        dp[nmask] = True
        results.append("Yes" if dp[(1 << N) - 1] else "No")
    print('\n'.join(results))

if __name__ == "__main__":
    main()