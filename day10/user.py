class User:
    __account = None
    __username = None
    __password = None
    __money = None
    __adress = None
    __RegisterDate = None
    __bank_name = None



    def setAccount (self,account) :
        self.__account = account
    def getAccount (self):
        return self.__account
    def setUsername (self, username) :
        self.__username = username
    def getUsername (self):
        return self.__username
    def setPassword(self,password) :
        self.__password = password
    def getPassword(self):
        return self.__password
    def setMoney (self,money) :
        self.__money = money
    def getMoney (self):
        return self.__money

    def setAddress (self,address):
        self.__address = address
    def getAddress (self):
        return self.__address
    def setRegisterDate (self,registerDate) :
        self.__registerDate = registerDate
    def getRegisterDate (self):
        return self.__registerDate

    def setBank_Name (self,bank_name):
        self.__bank_name = bank_name
    def getBank_Name (self):
        return self.__bank_name