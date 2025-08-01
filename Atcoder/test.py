#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os

def test_solution(solution_file, test_cases):
    """
    AtCoder問題のテストケースを実行する
    
    Args:
        solution_file: 解答ファイルのパス
        test_cases: テストケースのリスト [(入力, 期待出力), ...]
    """
    python_path = "/home/motty1050/kyopro/.venv/bin/python"
    
    for i, (input_data, expected_output) in enumerate(test_cases, 1):
        print(f"テストケース {i}:")
        print(f"入力: {input_data}")
        print(f"期待出力: {expected_output}")
        
        try:
            # Pythonスクリプトを実行
            result = subprocess.run(
                [python_path, solution_file],
                input=input_data,
                text=True,
                capture_output=True,
                timeout=2
            )
            
            actual_output = result.stdout.strip()
            print(f"実際の出力: {actual_output}")
            
            if actual_output == expected_output.strip():
                print("✅ PASS")
            else:
                print("❌ FAIL")
                if result.stderr:
                    print(f"エラー: {result.stderr}")
                    
        except subprocess.TimeoutExpired:
            print("❌ TIMEOUT (2秒)")
        except Exception as e:
            print(f"❌ ERROR: {e}")
        
        print("-" * 40)

def main():
    if len(sys.argv) < 2:
        print("使用方法: python test.py <solution_file.py>")
        return
    
    solution_file = sys.argv[1]
    
    if not os.path.exists(solution_file):
        print(f"ファイルが見つかりません: {solution_file}")
        return
    
    # サンプルテストケース（実際の問題に応じて変更）
    test_cases = [
        ("3\n1 2 3\n", "6"),
        ("5\n10 20 30 40 50\n", "150"),
    ]
    
    test_solution(solution_file, test_cases)

if __name__ == "__main__":
    main()
