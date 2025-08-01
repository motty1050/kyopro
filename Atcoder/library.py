#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AtCoder用ライブラリ
よく使用されるアルゴリズムやデータ構造をまとめたもの
"""

import sys
from collections import defaultdict, deque
import heapq
import math

# ==== 数学 ====

def gcd(a, b):
    """最大公約数"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """最小公倍数"""
    return a * b // gcd(a, b)

def is_prime(n):
    """素数判定"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factorize(n):
    """素因数分解"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def mod_pow(base, exp, mod):
    """高速べき乗 (mod付き)"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# ==== グラフ ====

class UnionFind:
    """Union-Find (素集合データ構造)"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        return self.size[self.find(x)]

def dijkstra(graph, start):
    """ダイクストラ法"""
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        
        for to, cost in graph[v]:
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(pq, (dist[to], to))
    
    return dist

def bfs(graph, start):
    """幅優先探索"""
    n = len(graph)
    visited = [False] * n
    dist = [-1] * n
    queue = deque([start])
    visited[start] = True
    dist[start] = 0
    
    while queue:
        v = queue.popleft()
        for to in graph[v]:
            if not visited[to]:
                visited[to] = True
                dist[to] = dist[v] + 1
                queue.append(to)
    
    return dist

def dfs(graph, start, visited=None):
    """深さ優先探索"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# ==== その他 ====

def binary_search(arr, target):
    """二分探索"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def lis_length(arr):
    """最長増加部分列の長さ"""
    if not arr:
        return 0
    
    dp = []
    for num in arr:
        pos = binary_search_bisect_left(dp, num)
        if pos == len(dp):
            dp.append(num)
        else:
            dp[pos] = num
    
    return len(dp)

def binary_search_bisect_left(arr, target):
    """bisect.bisect_leftの実装"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# ==== 入力用関数 ====

def read_ints():
    """整数のリストを読み込み"""
    return list(map(int, input().split()))

def read_int():
    """整数を読み込み"""
    return int(input())

def read_string():
    """文字列を読み込み"""
    return input().strip()

def read_strings():
    """文字列のリストを読み込み"""
    return input().split()
