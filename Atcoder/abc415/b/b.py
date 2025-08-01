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
    S = input()
    
    
   
    N=[]

    for i in range(len(S)):
        if S[i]=="#":
                N.append(i+1)

    for i in range(0, len(N), 2):
        print(f"{N[i]},{N[i+1]}")
    
    
if __name__ == "__main__":
    main()
