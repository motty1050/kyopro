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

def main():
    # 入力処理
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    
    # メイン処理
    # XがAに含まれるかチェック
    if X in A:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
