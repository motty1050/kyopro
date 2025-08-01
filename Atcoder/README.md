# AtCoder プログラミング環境

このディレクトリは、AtCoderのプログラミング問題を効率的に解くための環境です。

## ディレクトリ構成

```
Atcoder/
├── template.py           # 問題解答用テンプレート
├── library.py           # よく使うアルゴリズムライブラリ
├── test.py             # テスト実行用スクリプト
├── setup_problem.py    # 新しい問題セットアップ用スクリプト
└── README.md           # このファイル
```

## 使い方

### 1. 新しい問題を始める

```bash
cd /home/motty1050/kyopro/Atcoder
python setup_problem.py <コンテスト名> <問題ID>
```

例：
```bash
python setup_problem.py abc123 a
```

これにより以下の構造が作成されます：
```
abc123/
└── a/
    ├── a.py          # 解答ファイル（テンプレートから生成）
    ├── test_a.py     # テスト用ファイル
    └── README.md     # 問題メモ用
```

### 2. 問題を解く

1. `abc123/a/a.py`を開いてコードを書く
2. `test_a.py`にサンプルケースを追加
3. テストを実行して確認

### 3. テストの実行

#### 個別テスト
```bash
cd abc123/a
python test_a.py
```

#### 汎用テスト
```bash
python /home/motty1050/kyopro/Atcoder/test.py solution.py
```

### 4. VS Code スニペット

- `atcoder` + Tab → 問題テンプレート全体
- `fastinput` + Tab → 高速入力関数
- `readints` + Tab → 整数入力
- `readmulti` + Tab → 複数整数入力
- `fori` + Tab → for文
- `unionfind` + Tab → Union-Find
- `binsearch` + Tab → 二分探索
- `dijkstra` + Tab → ダイクストラ法

### 5. ライブラリの使用

```python
# ライブラリをインポート
import sys
sys.path.append('/home/motty1050/kyopro/Atcoder')
from library import UnionFind, dijkstra, gcd, lcm

# Union-Findの使用例
uf = UnionFind(n)
uf.union(a, b)
if uf.same(x, y):
    print("same")
```

### 6. VS Code タスク

- `Ctrl+Shift+P` → "Tasks: Run Task" → "AtCoder: Run Current File"
- または `F5` で現在のファイルを実行

## インストール済みパッケージ

- `numpy` - 数値計算
- `scipy` - 科学計算
- `networkx` - グラフ理論
- `sympy` - 記号計算
- `online-judge-tools` - オンラインジャッジツール
- `atcoder-tools` - AtCoder用ツール

## 便利なコマンド

### AtCoder Tools（オプション）
```bash
# ログイン
acc login

# 問題をダウンロード（サンプルケース付き）
acc new abc123

# テストケースで確認
acc test

# 提出
acc submit
```

### Online Judge Tools（オプション）
```bash
# サンプルケースのダウンロード
oj d https://atcoder.jp/contests/abc123/tasks/abc123_a

# テスト実行
oj t -c "python3 a.py"

# 提出
oj s https://atcoder.jp/contests/abc123/tasks/abc123_a a.py
```

## Tips

1. **高速入力**: 大量のデータを扱う場合は`sys.stdin.readline()`を使用
2. **デバッグ**: `print`文でのデバッグを活用
3. **時間計算量**: 制約を確認してアルゴリズムを選択
4. **エッジケース**: 最小値・最大値での動作を確認
5. **ライブラリ活用**: よく使うアルゴリズムはライブラリから使用

## アルゴリズム学習リソース

- [AtCoder公式](https://atcoder.jp/)
- [競技プログラミングの鉄則](https://book.mynavi.jp/ec/products/detail/id=131288)
- [蟻本](https://www.amazon.co.jp/dp/4839931992)
- [AtCoder Problems](https://kenkoooo.com/atcoder/)

---

問題解決を楽しんでください！ 🚀
