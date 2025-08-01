#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
from datetime import datetime

def create_problem_dir(contest_name, problem_id):
    """
    新しい問題用のディレクトリとファイルを作成
    
    Args:
        contest_name: コンテスト名 (例: abc123)
        problem_id: 問題ID (例: a, b, c, d)
    """
    base_dir = "/home/motty1050/kyopro/Atcoder"
    problem_dir = os.path.join(base_dir, contest_name, problem_id)
    
    # ディレクトリ作成
    os.makedirs(problem_dir, exist_ok=True)
    
    # テンプレートをコピー
    template_path = os.path.join(base_dir, "template.py")
    solution_path = os.path.join(problem_dir, f"{problem_id}.py")
    
    if os.path.exists(template_path):
        shutil.copy2(template_path, solution_path)
    
    # テスト用ファイル作成
    test_content = f'''#!/usr/bin/env python3
# テストケース for {contest_name} - {problem_id}

import subprocess
import sys
import os

def test_solution(solution_file, test_cases):
    """
    AtCoder問題のテストケースを実行する
    """
    python_path = "/home/motty1050/kyopro/.venv/bin/python"
    
    for i, (input_data, expected_output) in enumerate(test_cases, 1):
        print(f"テストケース {{i}}:")
        print(f"入力: {{repr(input_data)}}")
        print(f"期待出力: {{expected_output}}")
        
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
            print(f"実際の出力: {{actual_output}}")
            
            if actual_output == expected_output.strip():
                print("✅ PASS")
            else:
                print("❌ FAIL")
                if result.stderr:
                    print(f"エラー: {{result.stderr}}")
                    
        except subprocess.TimeoutExpired:
            print("❌ TIMEOUT (2秒)")
        except Exception as e:
            print(f"❌ ERROR: {{e}}")
        
        print("-" * 40)

def main():
    solution_file = "{problem_id}.py"
    
    # 問題のサンプルケースをここに記載
    test_cases = [
        # ("入力", "期待出力"),
        # 例: ("3\\n1 2 3\\n", "6"),
    ]
    
    print(f"Testing {contest_name} - {problem_id}")
    test_solution(solution_file, test_cases)

if __name__ == "__main__":
    main()
'''
    
    test_path = os.path.join(problem_dir, f"test_{problem_id}.py")
    with open(test_path, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    # README作成
    readme_content = f'''# {contest_name.upper()} - Problem {problem_id.upper()}

## 問題概要
<!-- 問題の概要を記載 -->

## 制約
<!-- 制約を記載 -->

## サンプル
<!-- サンプル入出力を記載 -->

## 解法
<!-- 解法のアイデアを記載 -->

## 実装日時
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
'''
    
    readme_path = os.path.join(problem_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"問題ディレクトリを作成しました: {problem_dir}")
    print(f"ファイル:")
    print(f"  - {solution_path}")
    print(f"  - {test_path}")
    print(f"  - {readme_path}")

def main():
    if len(sys.argv) != 3:
        print("使用方法: python setup_problem.py <contest_name> <problem_id>")
        print("例: python setup_problem.py abc123 a")
        return
    
    contest_name = sys.argv[1].lower()
    problem_id = sys.argv[2].lower()
    
    create_problem_dir(contest_name, problem_id)

if __name__ == "__main__":
    main()
