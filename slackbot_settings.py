# coding: utf-8
import os

# botアカウントのトークンを指定
API_TOKEN = os.getenv("SLACK_TOKEN")

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "Sorry but I didn't understand you"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']