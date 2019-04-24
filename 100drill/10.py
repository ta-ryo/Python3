#10:行数をカウントせよ．確認にはwcコマンドを用いよ．
f = open('data.txt','r') #open('ファイル名','r')で読みこみ専用で開く
print("length=",+len(f.readline()))#readline()で行を要素とした配列を得る
f.close()#開けたら閉める

# ヽ(*ﾟдﾟ)ノ> wc data.txt
#       24      98     813 data.txt
