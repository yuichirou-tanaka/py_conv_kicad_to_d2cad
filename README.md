# 概要
KiCADのファイルをコピペでD2CADにコピーするツール。
逆は未実装のため、KiCADからD2CADへ持ってくるだけです。

# 環境
- windows10 64bit
- python 3.7.7
上記の環境で動作確認済み

# 使い方
## KiCADのschファイルを txtに変換しD2CADにコピペ可能な形式にする
1. python conv_sch.py "Kicadの.libファイルへのパス" "出力ファイル名.txt" 

## KiCADのlibファイルを txtに変換しD2CADにコピペ可能な形式にする
1. python conv_lib.py "Kicadの.libファイルへのパス" "出力ファイル名.txt" 

# ライセンス
MIT License
Copyright (c) 2020 Yuichiro Tanaka

This software is released under the MIT License, see LICENSE.txt.
