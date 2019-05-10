with open('data.txt') as data:
    with open('col1.txt',"w") as col1:
        with open('col2.txt',"w") as col2:
            for line in data:
                law=line.split("\t")
                col1.write(law[0] + '\n')
                col2.write(law[1] + '\n')

"""
Ta-ryo > cut -f 1 data.txt > col1_test.txt
Ta-ryo > cut -f 2 data.txt > col2_test.txt
Ta-ryo > diff -s col1.txt col1_test.txt
Files col1.txt and col1_test.txt are identical
Ta-ryo > diff -s col2.txt col2_test.txt
Files col2.txt and col2_test.txt are identical
"""
