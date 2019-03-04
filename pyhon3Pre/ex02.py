english = input("英語の成績を入力してください>")
math = input("数学の成績を入力してください>")
#input()で所得した値はstring型である。
sum = int(english) + int(math)
print("英語の得点: " + english)
print("数学の得点: " + math)
print("合計: ", sum)
print("平均: ", sum/2)
