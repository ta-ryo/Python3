"""
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

"""
set型は重複しない要素（同じ値ではない要素、ユニークな要素）のコレクションで、
和集合、積集合、差集合などの集合演算を行うことができる。
"""

a = "paraparaparadise"
b = "paragraph"

def bigram(seq):
    return( [seq[ct:ct + 2] for ct in range(len(seq) - 2 + 1)] )

X = bigram(a)
Y = bigram(b)

#積集合
m = [i for i in Y if i in X ]
print(set(m))

#差集合 y^c
s = [i for i in X if i not in Y ]
print(set(s))

#差集合 x^c
d = [i for i in Y if i not in X ]
print(set(d))

#それの足し算 積集合以外
sd = s+d
print(set(sd))

#積集合 + 排反関係を作ったAとB　= 和集合
u = m + sd
print(set(u))
#別解
setX = set(X)
setY = set(Y)
_sum = setX.union(setY)
print(_sum)

n = "se"
print('se'in X)
print('se' in Y)
