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

# 高速入力
def input():
    return sys.stdin.readline().strip()

def main():
    # 入力処理
    N, L, R = map(int, input().split())
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
    ans += (x <= L < R <= y)
    print(ans)

if __name__ == "__main__":
    main()
