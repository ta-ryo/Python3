with open('data.txt') as data:
    for line in data:
        print(line.replace('\t',' '),end="")
