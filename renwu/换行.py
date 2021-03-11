num = int(input("请输入层数:"))
i = 1
while i <= num:

    j = 1
    while j <= (num - i):
        print(" ",end="")   # end="”不换行
        j = j + 1
    k = 1
    while k <= i:
        print("* ", end="")
        k = k + 1
    i = i + 1
    print()     # 换到下一行
