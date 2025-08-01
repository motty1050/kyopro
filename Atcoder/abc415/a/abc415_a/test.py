#!/usr/bin/env python3
"""
テスト実行スクリプト
"""

import subprocess
import sys
from pathlib import Path

def run_test(sample_num):
    """指定されたサンプルでテスト実行"""
    input_file = f"sample{sample_num}_input.txt"
    expected_output_file = f"sample{sample_num}_output.txt"
    
    if not Path(input_file).exists():
        print(f"入力ファイルが見つかりません: {input_file}")
        return False
    
    if not Path(expected_output_file).exists():
        print(f"期待出力ファイルが見つかりません: {expected_output_file}")
        return False
    
    # 入力データを読み込み
    with open(input_file, 'r') as f:
        input_data = f.read()
    
    # 期待出力を読み込み
    with open(expected_output_file, 'r') as f:
        expected_output = f.read().strip()
    
    # プログラムを実行
    try:
        result = subprocess.run(
            [sys.executable, "solution.py"],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5
        )
        
        actual_output = result.stdout.strip()
        
        print(f"サンプル {sample_num}:")
        print(f"入力: {repr(input_data)}")
        print(f"期待出力: {repr(expected_output)}")
        print(f"実際出力: {repr(actual_output)}")
        
        if actual_output == expected_output:
            print("✅ 正解")
            return True
        else:
            print("❌ 不正解")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ タイムアウト（5秒以上）")
        return False
    except Exception as e:
        print(f"❌ 実行エラー: {e}")
        return False

def main():
    """全サンプルケースでテスト実行"""
    sample_count = 3
    
    print(f"{sample_count}個のサンプルケースでテスト実行")
    print("-" * 50)
    
    passed = 0
    for i in range(1, sample_count + 1):
        if run_test(i):
            passed += 1
        print()
    
    print(f"結果: {passed}/{sample_count} サンプル通過")
    
    if passed == sample_count:
        print("🎉 全サンプル通過！")
    else:
        print("🔍 デバッグが必要です")

if __name__ == "__main__":
    main()
