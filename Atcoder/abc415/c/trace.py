#!/usr/bin/env python3
# ABC415-C 詳細トレーススクリプト

def trace_solution():
    print("=== ABC415-C 問題トレース ===")
    print()
    
    # 状態の説明
    print("【問題理解】")
    print("- N種類の薬品を全て混ぜ合わせたい")
    print("- 状態iは2進法表記でどの薬品が含まれるかを表す")
    print("- S[i-1]が'0'なら状態iは安全、'1'なら危険")
    print("- 空瓶から始めて、薬品を1つずつ追加")
    print("- 追加した時の状態が危険であってはならない")
    print()
    
    # テストケース1の詳細トレース
    print("【テストケース1】N=3, S='0010000'")
    N = 3
    S = "0010000"
    
    print(f"N={N}, S='{S}'")
    print(f"目標: 全ての薬品が混ざった状態 = {(1<<N)-1} = {bin((1<<N)-1)}")
    print()
    
    print("状態と安全性の対応:")
    for i in range(1, 1 << N):
        state_bin = bin(i)[2:].zfill(N)
        drugs = [j+1 for j in range(N) if i & (1 << j)]
        safety = "安全" if S[i-1] == '0' else "危険"
        print(f"状態{i:2}: {state_bin} → 薬品{drugs} → {safety}")
    print()
    
    print("DPトレース:")
    dp = [False] * (1 << N)
    dp[0] = True
    print(f"dp[0] = True (空の瓶は安全)")
    
    for mask in range(1 << N):
        if not dp[mask]:
            continue
        print(f"\n現在の状態 mask={mask} ({bin(mask)})")
        current_drugs = [j+1 for j in range(N) if mask & (1 << j)]
        print(f"  現在含まれる薬品: {current_drugs if current_drugs else '空'}")
        
        for add in range(N):
            if not (mask & (1 << add)):
                nmask = mask | (1 << add)
                print(f"  薬品{add+1}を追加 → 新状態{nmask} ({bin(nmask)})")
                if S[nmask - 1] == '0':
                    dp[nmask] = True
                    print(f"    S[{nmask-1}] = '{S[nmask-1]}' → 安全 → dp[{nmask}] = True")
                else:
                    print(f"    S[{nmask-1}] = '{S[nmask-1]}' → 危険 → 追加不可")
    
    result = "Yes" if dp[(1 << N) - 1] else "No"
    print(f"\n最終結果: dp[{(1<<N)-1}] = {dp[(1<<N)-1]} → {result}")
    print()
    
    # テストケース2の簡易トレース
    print("【テストケース2】N=3, S='0010110'")
    N = 3
    S = "0010110"
    print(f"N={N}, S='{S}'")
    
    print("危険な状態:")
    for i in range(1, 1 << N):
        if S[i-1] == '1':
            state_bin = bin(i)[2:].zfill(N)
            drugs = [j+1 for j in range(N) if i & (1 << j)]
            print(f"状態{i}: {state_bin} → 薬品{drugs} → 危険")
    
    print("→ 状態3(薬品1,2)と状態6(薬品2,3)が危険")
    print("→ 薬品1,2を先に混ぜることができない")
    print("→ 全ての薬品を安全に混ぜることは不可能")
    print("→ 結果: No")
    print()

if __name__ == "__main__":
    trace_solution()
