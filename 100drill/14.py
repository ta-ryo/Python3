n = input("自然数を入力してください:")
with open('data.txt') as data:
    for i in range(int(n)):
        print(data.readline().rstrip())

"""
Ta-ryo > head -n 10 data.txt
高知県	江川崎	41  2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
山梨県	甲府	40.7	2013-08-10
和歌山県	かつらぎ	40.6	1994-08-08
静岡県	天竜	40.6	1994-08-04
山梨県	勝沼	40.5	2013-08-10
埼玉県	越谷	40.4	2007-08-16
群馬県	館林	40.3	2007-08-16
Ta-ryo > python3 14.py
自然数を入力してください:10
高知県	江川崎	41  2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
山梨県	甲府	40.7	2013-08-10
和歌山県	かつらぎ	40.6	1994-08-08
静岡県	天竜	40.6	1994-08-04
山梨県	勝沼	40.5	2013-08-10
埼玉県	越谷	40.4	2007-08-16
群馬県	館林	40.3	2007-08-16
"""
