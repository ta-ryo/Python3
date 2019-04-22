# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans = []
for i in a.split(" "):
    count = 0
    for b in i:
        if b not in ('.',','):
            count += 1
    ans.append(count)
print(ans)
