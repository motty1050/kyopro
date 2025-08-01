#!/usr/bin/env python3
# トレース用スクリプト

def trace_solution():
    s = ".#.##..##.#.###....#"
    print("=== ABC415-B 問題トレース ===")
    print(f"入力文字列: {s}")
    print(f"文字列長: {len(s)}")
    print()

    print("Step 1: 位置の特定")
    print("インデックス:", end=" ")
    for i in range(len(s)):
        print(f"{i:2}", end=" ")
    print()
    
    print("文字列     :", end=" ")
    for c in s:
        print(f"{c:2}", end=" ")
    print()
    
    print("区画番号   :", end=" ")
    for i in range(len(s)):
        print(f"{i+1:2}", end=" ")
    print()
    print()

    positions = []
    print("'#'がある位置:")
    for i, c in enumerate(s):
        if c == '#':
            positions.append(i + 1)
            print(f"  インデックス{i:2} → 区画{i+1:2}")

    print()
    print(f"記録された位置: {positions}")
    print(f"荷物の総数: {len(positions)}個")
    print()

    print("Step 2: ペア出力")
    for i in range(0, len(positions), 2):
        print(f"{i//2+1}回目: positions[{i}], positions[{i+1}] → {positions[i]},{positions[i+1]}")

    print()
    print("=== 最終出力 ===")
    for i in range(0, len(positions), 2):
        print(f"{positions[i]},{positions[i+1]}")

if __name__ == "__main__":
    trace_solution()
