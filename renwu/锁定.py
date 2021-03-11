
username = "root"
password = "admin"
number = 0
while True:
    A = input("请输入用户名:")
    B = input("请输入密码：")

    if A ==username and B == password :
        print("欢迎进入本系统")
        break
    elif A != username or B !=password:
        print("密码或用户名错误")
        number = number + 1
        if number>2:
            print("次数用完,已锁定")
            break

