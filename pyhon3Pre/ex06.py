money = int(input("金額(円)> "))
print("金額: ", money ," 円")
money_kind = [10000,5000,1000,500,100,50,10,5]
for i in money_kind:
    print(i,"円 = ",money//i,"枚")
    money = money % i
print("1円 = ", money, "枚 ")
