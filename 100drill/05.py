"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""
def gram(seq,n):
    return([ seq[ct:ct + n] for ct in range(len(seq) - n + 1)])

"""
任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法．
「図書館情報学」を2(bi)-gramで分割すると，「図書」「書館」「館情」「情報」「報学」となる
"""

a = "I am an NLPer"
b = a.split()
# ctはcountの意味
print(gram(a,2))
