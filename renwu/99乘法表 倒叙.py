print("-------------九九乘法表-------------")
i = 0
while i <9:
    i =i+ 1

    j = 10
    while i < j:
        j =j - 1
        print(i, '*', j, '=', (i * j), end='\t')
    print("")
