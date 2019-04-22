"""
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を
単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
b = [1,5,6,7,8,9,15,16,19]
dic = {}
for (i,j) in enumerate(a.split(" ")):
    if i in b: #inの使い方は英語と同じ
        dic[i] = j[0]
    else:
        dic[i] = j[:2]
print(dic)
