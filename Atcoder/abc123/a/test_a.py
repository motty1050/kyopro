#!/usr/bin/env python3
# テストケース for abc123 - a

import subprocess
import sys
import os

def test_solution(solution_file, test_cases):
    """
    AtCoder問題のテストケースを実行する
    """
    python_path = "/home/motty1050/kyopro/.venv/bin/python"
    
    for i, (input_data, expected_output) in enumerate(test_cases, 1):
        print(f"テストケース {i}:")
        print(f"入力: {repr(input_data)}")
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
    solution_file = "a.py"
    
    # 問題のサンプルケースをここに記載
    test_cases = [
        # ("入力", "期待出力"),
        # 例: ("3\n1 2 3\n", "6"),
    ]
    
    print(f"Testing abc123 - a")
    test_solution(solution_file, test_cases)

if __name__ == "__main__":
    main()
