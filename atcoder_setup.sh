#!/bin/bash
# atcoder_setup.sh - AtCoder問題セットアップスクリプト (Atcoderディレクトリ版)

if [ $# -eq 0 ]; then
    echo "使用方法: $0 <問題URL>"
    echo "例: $0 https://atcoder.jp/contests/abc415/tasks/abc415_a"
    echo ""
    echo "推奨使用方法:"
    echo "cd /root/kyopro/Atcoder"
    echo "../atcoder_setup.sh https://atcoder.jp/contests/abc415/tasks/abc415_a"
    exit 1
fi

PROBLEM_URL=$1
PROBLEM_ID=$(echo $PROBLEM_URL | grep -o '[^/]*$')

echo "🚀 問題をセットアップ中: $PROBLEM_ID"

# Atcoderディレクトリ内に問題ディレクトリを作成
mkdir -p $PROBLEM_ID && cd $PROBLEM_ID

# サンプルケースダウンロード
echo "📥 サンプルケースをダウンロード中..."
/root/kyopro/.venv/bin/oj download $PROBLEM_URL

# テンプレートファイル作成（既存のtemplate.pyを参考に）
if [ -f "../template.py" ]; then
    echo "📄 既存のテンプレートを使用..."
    cp ../template.py solution.py
else
    echo "📄 デフォルトテンプレートを作成..."
    cat > solution.py << 'EOF'
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

# ライブラリのインポート
sys.path.append('/root/kyopro/Atcoder')
# from library import UnionFind, dijkstra, gcd, lcm

def main():
    # 入力処理
    
    
    # メイン処理
    
    
    # 出力
    

if __name__ == "__main__":
    main()
EOF
fi

# テストスクリプト作成
cat > test_solution.sh << 'EOF'
#!/bin/bash
echo "🧪 テスト実行中..."
/root/kyopro/.venv/bin/oj test -c "python3 solution.py"
EOF

chmod +x test_solution.sh

# 提出スクリプト作成
cat > submit_solution.sh << EOF
#!/bin/bash
echo "📤 提出中..."
/root/kyopro/.venv/bin/oj submit $PROBLEM_URL solution.py
EOF

chmod +x submit_solution.sh

# README.md作成
cat > README.md << EOF
# $PROBLEM_ID

## 問題URL
$PROBLEM_URL

## ファイル構成
- \`solution.py\`: 解答ファイル
- \`test_solution.sh\`: テスト実行スクリプト
- \`submit_solution.sh\`: 提出スクリプト
- \`test/\`: サンプルケース

## 使用方法
1. \`solution.py\`を編集してコードを書く
2. \`./test_solution.sh\`でテスト実行
3. \`./submit_solution.sh\`で提出

## 実装日時
$(date '+%Y-%m-%d %H:%M:%S')
EOF

echo "✅ セットアップ完了: $PROBLEM_ID/"
echo "📁 生成されたファイル:"
echo "  - test/sample-*.in, test/sample-*.out: サンプルケース"
echo "  - solution.py: 解答テンプレート"
echo "  - test_solution.sh: テスト実行スクリプト"
echo "  - submit_solution.sh: 提出スクリプト"
echo "  - README.md: 問題情報"
echo ""
echo "🎯 次のステップ:"
echo "  1. solution.py を編集してコードを書く"
echo "  2. ./test_solution.sh でテスト実行"
echo "  3. ./submit_solution.sh で提出"
echo ""
echo "💡 ヒント:"
echo "  - ライブラリを使用する場合: from library import UnionFind, gcd, lcm"
echo "  - VS Codeタスク: F5キーで実行"
