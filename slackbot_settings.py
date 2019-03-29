# coding: utf-8
import boto3

# botアカウントのトークンを指定
ssm = boto3.client('ssm', region_name='ap-northeast-1')
parameter = ssm.get_parameter(Name='slackapp_bot_token', WithDecryption=True)
API_TOKEN = parameter['Parameter']['Value']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "Sorry but I didn't understand you"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']