# AtCoder 問題解析・コード生成ツール一覧

## 主要なツール

### 1. **atcoder-tools (acc)**
- **概要**: AtCoder専用の最も人気のあるツール
- **機能**:
  - 問題文からサンプルケースを自動取得
  - 入力フォーマットを解析してコードテンプレート生成
  - テスト実行・提出まで一貫サポート
- **インストール**: `pip install atcoder-tools`
- **使用例**:
  ```bash
  # ログイン
  acc login
  
  # コンテストの問題をダウンロード
  acc new abc123
  
  # 個別問題をダウンロード
  acc new https://atcoder.jp/contests/abc123/tasks/abc123_a
  
  # テスト実行
  acc test
  
  # 提出
  acc submit
  ```

### 2. **online-judge-tools (oj)**
- **概要**: 汎用オンラインジャッジツール（AtCoder以外も対応）
- **機能**:
  - サンプルケースのダウンロード
  - テスト実行
  - 提出
- **インストール**: `pip install online-judge-tools`
- **使用例**:
  ```bash
  # ログイン
  oj login https://atcoder.jp/
  
  # サンプルケースをダウンロード
  oj d https://atcoder.jp/contests/abc123/tasks/abc123_a
  
  # テスト実行
  oj t -c "python3 main.py"
  
  # 提出
  oj s https://atcoder.jp/contests/abc123/tasks/abc123_a main.py
  ```

### 3. **AtCoder Library (ACL)**
- **概要**: AtCoder公式のライブラリ
- **機能**: 高度なアルゴリズムの実装済みライブラリ
- **対応言語**: C++, Python, Java
- **使用例**:
  ```python
  # Union-Find
  from atcoder import DSU
  
  # セグメント木
  from atcoder import SegTree
  ```

### 4. **VS Code拡張機能**

#### **AtCoder Tools**
- 機能: VS Code内でAtCoderの問題を管理
- インストール: VS Code拡張機能から検索

#### **Competitive Programming Helper**
- 機能: テンプレート生成、テスト実行
- 多言語対応

### 5. **ブラウザ拡張機能**

#### **AtCoder Easy Test**
- ブラウザ上でサンプルケースを簡単テスト
- Chrome/Firefox対応

#### **ac-predictor**
- レーティング予測
- パフォーマンス分析

## 自作ツールの作成

### 問題解析スクリプト例
```python
import requests
from bs4 import BeautifulSoup
import re

def parse_atcoder_problem(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # サンプル入力/出力を取得
    samples = []
    pre_tags = soup.find_all('pre')
    
    for i in range(0, len(pre_tags), 2):
        if i + 1 < len(pre_tags):
            input_data = pre_tags[i].text.strip()
            output_data = pre_tags[i + 1].text.strip()
            samples.append((input_data, output_data))
    
    return samples

# 使用例
samples = parse_atcoder_problem('https://atcoder.jp/contests/abc123/tasks/abc123_a')
for i, (inp, out) in enumerate(samples):
    with open(f'input_{i}.txt', 'w') as f:
        f.write(inp)
    with open(f'output_{i}.txt', 'w') as f:
        f.write(out)
```

## 推奨セットアップ

### 基本構成
1. **atcoder-tools**: 問題ダウンロード・提出
2. **online-judge-tools**: サンプルテスト
3. **VS Code拡張**: 開発環境
4. **カスタムテンプレート**: 個人用テンプレート

### エイリアス設定（kyoproワークスペース）
当環境では便利なエイリアスが設定済みです：
```bash
# エイリアス一覧
atgen abc123    # 問題ダウンロード（atcoder-tools gen）
attest          # テスト実行（atcoder-tools test）
atsub           # 提出（atcoder-tools submit）
oj              # online-judge-tools
kyopro          # Atcoderディレクトリに移動
```

### 効率的なワークフロー
```bash
# 1. 問題ダウンロード
atgen abc123

# 2. 問題を解く（VS Codeで編集）
kyopro
cd abc123/A
code main.py

# 3. テスト実行
attest

# 4. 提出
atsub
```

### フルパス版（参考）
エイリアスが効かない場合のフルパスコマンド：
```bash
/root/kyopro/.venv/bin/atcoder-tools gen abc123 --config /root/kyopro/atcodertools.toml --without-login
/root/kyopro/.venv/bin/oj login https://atcoder.jp/
```

## トラブルシューティング

### よくある問題
1. **ログインエラー**: ブラウザでログイン後、Cookieを確認
2. **サンプル取得失敗**: 問題URLが正しいか確認
3. **テスト失敗**: 出力フォーマット（改行、スペース）を確認
4. **コマンドが見つからない**: フルパスまたはエイリアスを使用

### 現在の環境状況
**kyoproワークスペース**では以下が設定済み：
- ✅ atcoder-tools 2.14.0（依存関係修正済み）
- ✅ online-judge-tools 11.5.1
- ✅ 仮想環境（/root/kyopro/.venv/）
- ✅ カスタム設定ファイル（atcodertools.toml）
- ✅ 便利なエイリアス設定
- ✅ Pythonテンプレート対応

### 環境設定のポイント
- Python環境の統一
- 依存関係の管理（Jinja2/MarkupSafe問題解決済み）
- テンプレートの標準化
- エイリアスによる効率化

---

これらのツールを組み合わせることで、AtCoderでの競技プログラミングを効率化できます。
