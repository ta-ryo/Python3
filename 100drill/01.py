#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
a = "パタトクカシーー"
print(a[::2])

# 別案
b = "".join(a[i] for i in [1,3,5,7])
#print(b)
