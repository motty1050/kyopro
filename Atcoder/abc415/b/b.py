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
# def input():
#     return sys.stdin.readline().strip()

def main():
    # 入力処理
    s = input()
    
    # '#'の位置を収集
    positions = [i + 1 for i, c in enumerate(s) if c == '#']
    
    # 2つずつペアにして出力
    for i in range(0, len(positions), 2):
        print(f"{positions[i]},{positions[i+1]}")
    
if __name__ == "__main__":
    main()
