with open('col1.txt') as col1:
    with open('col2.txt') as col2:
        with open('col3.txt','w') as col3:
            for col1_line, col2_line in zip(col1,col2):
                col3.write(col1_line.rstrip() + '\t' +col2_line)


"""
Ta-ryo > python3 13.py
Ta-ryo > paste col1.txt col2.txt > col3_test.txt
Ta-ryo > diff -s col3.txt col3_test.txt
Files col3.txt and col3_test.txt are identical
"""
