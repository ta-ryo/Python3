import json, config
from requests_oauthlib import OAuth1Session

#認証までは同じ
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
#OAuth認証処理
twitter = OAuth1Session(CK,CS,AT,ATS)

#エンドポイントは前回のタイムラインと異なる
#ツイートポストエンドポイント
url = "https://api.twitter.com/1.1/statuses/update.json"

print("ツイートする内容の入力フォーム")
#input()でキーボード入力
tweet = input(">> ")
print('*******************************************')

#辞書型で保存
params = {"status" : tweet}

#post送信
res = twitter.post(url, params = params)

#status_code = 200だと正常に動作した
if res.status_code == 200:
    print("Success.")
#正常投稿出来なかった場合
else:
    print("Failed. : %d"% res.status_code)
