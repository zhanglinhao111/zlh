a = input("a边的长度：")
a = int(a)
b = input("b边的长度：")
b = int(b)
c = input("c边的长度：")
c = int(c)
if a+b>c and b+c>a and a+c>b :

    if a == b == c :
        print("构成等边三角形")
    elif a==b or a==c or b==c:
        print("构成等腰三角形")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
        print("构成直角三角形")
    else:
        print("构成普通三角形")

else:
    print("不能构成三角形")
