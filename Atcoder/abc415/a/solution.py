#!/usr/bin/env python3

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
