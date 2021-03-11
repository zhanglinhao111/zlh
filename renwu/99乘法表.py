print("-------------九九乘法表-------------")
j = 0
while j < 9:
    j =j+ 1

    i = 0
    while i < j:
        i =i + 1
        print(j, '*', i, '=', (j * i), end='\t')
    print("")