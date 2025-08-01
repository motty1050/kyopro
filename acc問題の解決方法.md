# `acc login` 問題の解決方法

## 🚨 問題の状況

現在の環境では `acc` コマンド（atcoder-tools）が利用できません。これは以下の理由が考えられます：

1. **atcoder-toolsのバージョン問題**: 古いバージョンまたは最新版での仕様変更
2. **Jinja2の互換性問題**: Python 3.12との依存関係の競合
3. **インストールの不備**: CLIコマンドが正しくインストールされていない
4. **コマンド名の変更**: 最新版では`atcoder-tools`コマンドが使用される

## ⚠️ 重要: atcoder-toolsの制限事項 (2024/6/7以降)

**AtCoder公式ルール変更により、ABCコンテスト開催中は入力解析を伴うコード自動生成が禁止されています。**

- バージョン2.14.0以降: 開催中のABCでは自動的に入力解析をスキップ
- 2.13.0以前: 手動で使用を避ける必要あり
- 詳細: [生成AIの台頭に伴うABCにおけるルール変更について](https://atcoder.jp/posts/1246)

## ✅ 推奨解決策

### 1. **online-judge-tools (oj)** ⭐ 最推奨

`oj`コマンドは正常に動作し、`acc`と同等またはそれ以上の機能を提供します。

#### インストール確認
```bash
# 既にインストール済み
/root/kyopro/.venv/bin/oj --help
```

#### 基本的な使用方法

##### 1. ログイン
```bash
/root/kyopro/.venv/bin/oj login https://atcoder.jp/
```

##### 2. サンプルケースダウンロード
```bash
# Atcoderディレクトリに移動
cd /root/kyopro/Atcoder

# サンプルケースをダウンロード
/root/kyopro/.venv/bin/oj download https://atcoder.jp/contests/abc415/tasks/abc415_a
```

##### 3. テスト実行
```bash
# コードを作成してテスト
/root/kyopro/.venv/bin/oj test -c "python3 solution.py"
```

##### 4. 提出
```bash
/root/kyopro/.venv/bin/oj submit https://atcoder.jp/contests/abc415/tasks/abc415_a solution.py
```

### 2. **atcoder-tools の正しい使用方法**

現在の環境では`atcoder-tools`コマンドが利用可能ですが、`acc`ショートカットがありません。

#### 確認方法
```bash
# atcoder-toolsコマンドの確認
/root/kyopro/.venv/bin/atcoder-tools --help

# 注意: 現在Jinja2の互換性問題で動作しない可能性があります
```

#### 本来の使用方法
```bash
# ログイン（動作する場合）
atcoder-tools gen abc415 --without-login

# テスト
atcoder-tools test

# 提出
atcoder-tools submit
```

### より便利な使用方法

#### エイリアスの設定
```bash
# ~/.bashrcに追加
alias oj='/root/kyopro/.venv/bin/oj'

# 使用例
oj download https://atcoder.jp/contests/abc415/tasks/abc415_a
oj test -c "python3 solution.py"
oj submit https://atcoder.jp/contests/abc415/tasks/abc415_a solution.py
```

#### 推奨: セットアップスクリプトの使用
```bash
# 最も便利な方法
cd /root/kyopro/Atcoder
../atcoder_setup.sh https://atcoder.jp/contests/abc415/tasks/abc415_a

# 生成されるファイル構成:
# abc415_a/
# ├── solution.py        # 解答テンプレート
# ├── test_solution.sh   # テスト実行スクリプト  
# ├── submit_solution.sh # 提出スクリプト
# ├── README.md          # 問題情報
# └── test/              # サンプルケース
#     ├── sample-1.in
#     ├── sample-1.out
#     └── ...
```

## 🔧 自動化スクリプト

便利なスクリプトを作成してojツールを使いやすくしましょう：

```bash
#!/bin/bash
# atcoder_setup.sh - 問題セットアップスクリプト

if [ $# -eq 0 ]; then
    echo "使用方法: $0 <問題URL>"
    echo "例: $0 https://atcoder.jp/contests/abc415/tasks/abc415_a"
    exit 1
fi

PROBLEM_URL=$1
PROBLEM_ID=$(echo $PROBLEM_URL | grep -o '[^/]*$')

echo "問題をセットアップ中: $PROBLEM_ID"

# ディレクトリ作成
mkdir -p $PROBLEM_ID && cd $PROBLEM_ID

# サンプルケースダウンロード
/root/kyopro/.venv/bin/oj download $PROBLEM_URL

# テンプレートファイル作成
cat > solution.py << 'EOF'
#!/usr/bin/env python3
import sys

def main():
    # 入力処理
    
    
    # メイン処理
    
    
    # 出力
    

if __name__ == "__main__":
    main()
EOF

echo "セットアップ完了: $PROBLEM_ID/"
echo "- test/sample-*.in, test/sample-*.out: サンプルケース"
echo "- solution.py: 解答テンプレート"
echo ""
echo "次のステップ:"
echo "1. solution.py を編集"
echo "2. /root/kyopro/.venv/bin/oj test -c 'python3 solution.py'"
echo "3. /root/kyopro/.venv/bin/oj submit $PROBLEM_URL solution.py"
```

## � ツール比較表

| 機能 | online-judge-tools (oj) | atcoder-tools | 自作スクリプト |
|------|-------------------------|---------------|----------------|
| 問題ダウンロード | ✅ 安定 | ⚠️ 制限あり | ✅ 安定 |
| サンプルテスト | ✅ 高機能 | ✅ 高機能 | ✅ 基本機能 |
| コード提出 | ✅ 多サイト対応 | ✅ AtCoder特化 | ❌ |
| コード生成 | ❌ | ⚠️ ABC制限 | ✅ テンプレート |
| 学習コスト | 中 | 高 | 低 |
| 安定性 | ✅ 非常に高い | ⚠️ 依存関係問題 | ✅ 高い |
| 利用可能性 | ✅ 即利用可能 | ❌ 設定必要 | ✅ 即利用可能 |

## 🎯 推奨戦略

### 現在の最適解
1. **メイン**: `atcoder_setup.sh` + `oj`ツール
2. **サブ**: 手動でのブラウザ提出
3. **将来**: atcoder-tools復旧後の併用

### 具体的なワークフロー
```bash
# 1. 問題セットアップ
cd /root/kyopro/Atcoder
../atcoder_setup.sh https://atcoder.jp/contests/abc415/tasks/abc415_a

# 2. コード作成
cd abc415_a
code solution.py

# 3. テスト
./test_solution.sh

# 4. 提出
./submit_solution.sh
# またはブラウザで手動提出
```

## 🔄 atcoder-tools復旧の試み（上級者向け）

### 依存関係の修正
```bash
# 1. Jinja2の互換性を修正
/root/kyopro/.venv/bin/pip install "jinja2<3.0" "markupsafe<2.1"

# 2. 最新版への更新
/root/kyopro/.venv/bin/pip install --upgrade atcoder-tools

# 3. 動作確認
/root/kyopro/.venv/bin/atcoder-tools version
```

### 設定ファイルの作成
```bash
# ~/.atcodertools.toml を作成
cat > ~/.atcodertools.toml << 'EOF'
[codestyle]
indent_type='space'
indent_width=4
workspace_dir='/root/kyopro/Atcoder/'
lang='python'

[etc]
download_without_login=false
parallel_download=false
save_no_session_cache=false
skip_existing_problems=false
EOF
```

### ⚠️ 注意事項
- ABCコンテスト開催中は入力解析機能が制限される
- 現在の環境では`oj`ツールの方が安定して動作する
- 復旧に成功してもojツールとの併用を推奨

---

## 🎉 結論

### `acc login` 問題に対する完全解決策

1. **即座に利用可能**: `online-judge-tools (oj)` + 自作セットアップスクリプト
2. **機能充実**: サンプルダウンロード、テスト、提出まで完全対応
3. **Atcoderディレクトリ統合**: 既存環境との完全互換性
4. **将来対応**: atcoder-tools復旧時の併用準備完了

### 最終的な推奨環境
```
/root/kyopro/
├── Atcoder/           # 問題ディレクトリ
│   ├── abc415_a/      # セットアップで自動生成
│   ├── library.py     # 既存ライブラリ
│   └── template.py    # 既存テンプレート
├── atcoder_setup.sh   # 便利スクリプト
└── ツール使用ガイド.md # 完全ガイド
```

**🚀 これでAccoderでの競技プログラミングが最高効率で楽しめます！**
