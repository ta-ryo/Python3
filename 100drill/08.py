"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

"""
正規表現のパターン文字列を定義するときは、クォーテーションの前に r を付て利用した方が良いです。
正規表現にはバックスラッシュを使用したパターンが存在するため、r を付けることによって raw 文字列として扱われ、
エスケープシーケンスを無効にしてくれます。
"""

"""
lambda関数は無名関数。
lambda 引数: 返り値という形でかく。
def return_twice(n):　　return n * 2　　＝＝ lambda n: n * 2
m.group(0)で[a-z]でマッチした文字全てを表せられる。
次にord()でUnicode変換。chr()でUnicodeを文字変換。
"""

import re
def cipher(x):
    return re.sub(r'[a-z]',lambda m: chr(219-ord(m.group(0))),x)

a = "I am Onion"
print(cipher(a)) #暗号化
print(cipher(cipher(a))) #複合化
