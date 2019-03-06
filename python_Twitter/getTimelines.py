#標準のjsonモジュールとconfig.pyの読み込み
import json, config

#OAuthのライブラリの読み込み
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

#OAuth認証処理
twitter = OAuth1Session(CK,CS,AT,ATS)

#タイムライン取得エンドポイント
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#覚えてる辞書型だよ
params = {'count' : 5}

#getメソッドでの処理
res = twitter.get(url, params = params)

 # HTTPのステータスコードを所得してが200だと成功
if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        print(line['user']['name'] + '::' + line['text'])
        print(line['created_at'])
        print("*******************************************")
else:
    print("Failed: %d" % res.status_code)
