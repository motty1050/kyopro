#!/usr/bin/env python3
"""
AtCoder問題解析・入出力ファイル生成ツール
使用方法: python problem_parser.py <問題URL>
"""

import requests
from bs4 import BeautifulSoup
import re
import sys
import os
from pathlib import Path

def parse_atcoder_problem(url):
    """AtCoderの問題ページから情報を取得"""
    print(f"問題を解析中: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"エラー: {e}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 問題名を取得
    title_elem = soup.find('span', class_='h2')
    title = title_elem.text.strip() if title_elem else "Unknown Problem"
    
    # 問題文を取得
    problem_statement = soup.find('div', id='task-statement')
    problem_text = problem_statement.get_text().strip() if problem_statement else ""
    
    # サンプルケースを取得
    samples = []
    
    # サンプル入力/出力のセクションを探す
    h3_tags = soup.find_all('h3')
    
    for h3 in h3_tags:
        if 'サンプル入力' in h3.text or 'Sample Input' in h3.text:
            # 次のpreタグを取得
            pre_input = h3.find_next('pre')
            if pre_input:
                # 対応する出力を探す
                next_h3 = h3.find_next('h3')
                if next_h3 and ('サンプル出力' in next_h3.text or 'Sample Output' in next_h3.text):
                    pre_output = next_h3.find_next('pre')
                    if pre_output:
                        input_data = pre_input.text.strip()
                        output_data = pre_output.text.strip()
                        samples.append((input_data, output_data))
    
    return {
        'title': title,
        'problem_text': problem_text,
        'samples': samples,
        'url': url
    }

def generate_files(problem_data, output_dir):
    """問題データからファイルを生成"""
    if not problem_data:
        return
    
    # 出力ディレクトリを作成
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # README.md生成
    readme_content = f"""# {problem_data['title']}

## 問題URL
{problem_data['url']}

## サンプルケース

"""
    
    for i, (inp, out) in enumerate(problem_data['samples'], 1):
        readme_content += f"""### サンプル {i}
**入力:**
```
{inp}
```

**出力:**
```
{out}
```

"""
    
    with open(f"{output_dir}/README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # サンプル入出力ファイルを生成
    for i, (inp, out) in enumerate(problem_data['samples']):
        with open(f"{output_dir}/sample{i+1}_input.txt", 'w', encoding='utf-8') as f:
            f.write(inp)
        
        with open(f"{output_dir}/sample{i+1}_output.txt", 'w', encoding='utf-8') as f:
            f.write(out)
    
    # テンプレートファイルを生成
    template_content = '''#!/usr/bin/env python3
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

def main():
    # 入力処理
    
    
    # メイン処理
    
    
    # 出力
    

if __name__ == "__main__":
    main()
'''
    
    with open(f"{output_dir}/solution.py", 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    # テストスクリプトを生成
    test_script = f'''#!/usr/bin/env python3
"""
テスト実行スクリプト
"""

import subprocess
import sys
from pathlib import Path

def run_test(sample_num):
    """指定されたサンプルでテスト実行"""
    input_file = f"sample{{sample_num}}_input.txt"
    expected_output_file = f"sample{{sample_num}}_output.txt"
    
    if not Path(input_file).exists():
        print(f"入力ファイルが見つかりません: {{input_file}}")
        return False
    
    if not Path(expected_output_file).exists():
        print(f"期待出力ファイルが見つかりません: {{expected_output_file}}")
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
        
        print(f"サンプル {{sample_num}}:")
        print(f"入力: {{repr(input_data)}}")
        print(f"期待出力: {{repr(expected_output)}}")
        print(f"実際出力: {{repr(actual_output)}}")
        
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
        print(f"❌ 実行エラー: {{e}}")
        return False

def main():
    """全サンプルケースでテスト実行"""
    sample_count = {len(problem_data['samples'])}
    
    print(f"{{sample_count}}個のサンプルケースでテスト実行")
    print("-" * 50)
    
    passed = 0
    for i in range(1, sample_count + 1):
        if run_test(i):
            passed += 1
        print()
    
    print(f"結果: {{passed}}/{{sample_count}} サンプル通過")
    
    if passed == sample_count:
        print("🎉 全サンプル通過！")
    else:
        print("🔍 デバッグが必要です")

if __name__ == "__main__":
    main()
'''
    
    with open(f"{output_dir}/test.py", 'w', encoding='utf-8') as f:
        f.write(test_script)
    
    print(f"ファイルを生成しました: {output_dir}/")
    print(f"- README.md: 問題概要")
    print(f"- solution.py: 解答テンプレート")
    print(f"- test.py: テスト実行スクリプト")
    print(f"- sample*_input.txt: サンプル入力 ({len(problem_data['samples'])}個)")
    print(f"- sample*_output.txt: サンプル出力 ({len(problem_data['samples'])}個)")

def main():
    if len(sys.argv) != 2:
        print("使用方法: python problem_parser.py <AtCoder問題URL>")
        print("例: python problem_parser.py https://atcoder.jp/contests/abc123/tasks/abc123_a")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # URLから問題IDを抽出
    match = re.search(r'/tasks/([^/]+)', url)
    if match:
        problem_id = match.group(1)
        output_dir = problem_id
    else:
        output_dir = "atcoder_problem"
    
    # 問題を解析
    problem_data = parse_atcoder_problem(url)
    
    if problem_data:
        generate_files(problem_data, output_dir)
    else:
        print("問題の解析に失敗しました")
        sys.exit(1)

if __name__ == "__main__":
    main()
