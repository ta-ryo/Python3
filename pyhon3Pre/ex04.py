hour_speed = input("時速(km/h)> ")
minute_speed = float(hour_speed) / 60
second_speed = minute_speed / 60
# k = 10 ** 3
print("秒速 = ", second_speed * 10**3 ,"m/s")
