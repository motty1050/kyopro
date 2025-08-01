#!/bin/bash
# AtCoder競技プログラミング用エイリアス設定スクリプト

echo "# AtCoder競技プログラミング用エイリアス" >> ~/.bashrc
echo "alias atgen='/root/kyopro/.venv/bin/atcoder-tools gen --config /root/kyopro/atcodertools.toml --without-login'" >> ~/.bashrc
echo "alias attest='/root/kyopro/.venv/bin/atcoder-tools test'" >> ~/.bashrc
echo "alias atsub='/root/kyopro/.venv/bin/atcoder-tools submit'" >> ~/.bashrc
echo "alias oj='/root/kyopro/.venv/bin/oj'" >> ~/.bashrc
echo "alias kyopro='cd /root/kyopro/Atcoder'" >> ~/.bashrc

echo "エイリアスが設定されました！"
echo "新しいターミナルを開くか、以下のコマンドを実行してください："
echo "source ~/.bashrc"
echo ""
echo "利用可能なエイリアス："
echo "  atgen abc123    # 問題ダウンロード"
echo "  attest          # テスト実行"
echo "  atsub           # 提出"
echo "  oj              # online-judge-tools"
echo "  kyopro          # Atcoderディレクトリに移動"
