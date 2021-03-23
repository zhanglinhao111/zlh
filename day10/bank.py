from DBUtils import select
from DBUtils import update
class Bank:
    bankName = "中国工商银行昌平回龙观支行"

    def  bank_AddUser(self,user):
        # 判断数据库是否已满
        sql1 = "select  count(*)  from user"
        data = select(sql1, [])
        if data[0][0] >= 100:  # 如果返回的统计数据超出100，则已满
            return 3
        # 判断数据是否存在改用户
        # 获取所有键，然后在判断是否有
        sql2 = "select * from user  where  account = %s"
        param2 = [user.getAccount()]
        data2 = select(sql2, param2)
        if len(data2) != 0:  # 如果通过sql语句能查到数据并且不为空，则说明改用户已存在
            return 2
        # 正常开户：insert into 表  ，否则则执行存储数据操作
        sql3 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"  # now() 使用的mysql数据库自己的时间
        param3 = [user.getAccount(),
                  user.getUsername(),
                  user.getPassword(),
                  user.getAddress().getCountry(),
                  user.getAddress().getProvince(),
                  user.getAddress().getStreet(),
                  user.getAddress().getDoor(),
                  user.getMoney(),
                  self.bankName]
        update(sql3, param3)
        return 1

        # 银行的存款逻辑

    def bank_deposit(self, user):
        sql = "select * from user  where  account = %s"
        param = [user.getAccount()]
        data = select(sql, param)
        # 账号存在
        for d in data:
            if d[0] == user.getAccount():
                money = int(input("请输入金额："))
                money = money + int(d[7])
                sql2 = "update user set money='" + str(money) + "' where account=" + user.getAccount()
                param2 = []
                update(sql2, param2)
                return True

        # 账号不存在
        return False

        # 银行的取钱逻辑

    def bank_withdraw(self, user):
        sql = "select * from user  where  account = %s"
        param = [user.getAccount()]
        data = select(sql, param)
        # 账号存在
        for d in data:
            if d[0] == user.getAccount():
                password = input("请输入密码：")
                if d[2] == password:
                    money = int(input("请输入金额："))
                    if money <= int(d[7]):
                        money = int(d[7]) - money
                        sql2 = "update user set money='" + str(money) + "' where account =" + user.getAccount()
                        update(sql2, [])
                        return 0
                    else:
                        return 3
                else:
                    return 2
        return 1

        # 银行的转账逻辑

    def bank_transfer(self, user1, user2):
        sql = "select * from user where account=%s"
        param = [user1.getAccount()]
        param2 = [user2.getAccount()]
        data = select(sql, param)
        data2 = select(sql, param2)
        # 账号存在
        for c in data2:
            if c[0] == user2.getAccount():
                for d in data:
                    if d[0] == user1.getAccount():
                        password = input("请输入密码：")
                        if d[2] == password:
                            money = int(input("请输入金额："))
                            if money <= int(d[7]):
                                money1 = int(d[7]) - money
                                money2 = int(c[7]) + money
                                sql2 = "update bank set money='" + str(money1) + "' where account=" + user1.getAccount()
                                sql3 = "update bank set money='" + str(money2) + "' where account=" + user2.getAccount()
                                update(sql2, [])
                                update(sql3, [])
                                return 0
                            else:
                                return 3
                        else:
                            return 2

        return 1

        # 银行的查询逻辑

    def bank_inquire(self, user):
        sql = "select * from user  where  account = %s"
        param = [user.getAccount()]
        data = select(sql, param)
        # 账号存在
        i = 0
        for c in data:
            if c[0] == user.getAccount():
                i = i + 1
                password = input("请输入密码：")
                if password == c[2]:
                    print("前账号：", user.getAccount())
                    print("密码：******")
                    print("余额：", c[7])
                    print("用户居住地址：", c[3], c[4], c[5], c[6])
                    print("当前账户的开户行：", c[9])
                else:
                    print("密码不正确")
        if i == 0:
            print("账户不存在")























