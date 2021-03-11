import random

num = random.randint(1,50)
# print(num)
number = 0
while True:
    a = input("请输入数字：")
    a = int(a)
    if a < num:
        print("小了")
    elif a > num :
        print("大了")

    elif a == num:
        print("恭喜！")
        if number<=2:
            print("＋2000💲")
        elif number > 2 and number <= 5:
            print("+1000$")
        break
    number = number + 1
    if number > 6:
        print("次数用完,已锁定","次数：",number)
        break