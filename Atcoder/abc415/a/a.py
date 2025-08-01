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
    X = int(input())
    A = list(map(int, input().split()))
    
    # メイン処理
    # XがAに含まれるかチェック
    if X in A:
        print("yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
