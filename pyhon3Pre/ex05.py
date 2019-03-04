num_10 = input("10進数> ")
if int(num_10) > 255:
    print("255より小さな数字で打ち直しです")
    num_10 = int(input("10進数> "))
con_num_10 = int(num_10)
ans = []
while con_num_10 > 1:
    ans.append(int(con_num_10 % 2))
    con_num_10 = int(con_num_10/2)
else:
    ans.append(int(con_num_10))
while len(ans) < 8:
    ans.append(0)
ans.reverse()
#listの向きをひっくり返す。代入しなくてもいいやつ
ans = map(str,ans)
#map(型名,list[])でlistの要素を全て型名に変更することができる。
print(num_10, " = ","".join(ans))
