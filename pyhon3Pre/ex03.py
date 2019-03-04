height = input("身長をm単位で入力してください> ")
weight = input("体重をkg単位で入力してください> ")
# **で累乗できる
BMI = float(weight) / float(height)**2
print("BMI = ",BMI)
