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

#Tweetを検索するエンドポイント
url = "https://api.twitter.com/1.1/search/tweets.json"

print("検索するTweetワード")
keyword = input(">> ")
print("*******************************************")
params = {'q':keyword,'count':10}
res = twitter.get(url, params = params)

if res.status_code == 200:
    search_tweet = json.loads(res.text)
    #search_tweetの中身に['status'{"":""}]ってなってる
    for tweet in search_tweet['statuses']:
        print(tweet['user']['name'] + '::' + tweet['text'])
        print(tweet['created_at'])
        print('------------------------------------')
else:
    print("Failed: %d" % res.status_code)
