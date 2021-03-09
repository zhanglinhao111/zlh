id1 = 1
name1 = "卫衣"
price1 = 200
quanlity1 = "A+"
mold1 = "上衣"
Sales1 = 500

id2 = 2
name2 = "工装裤"
price2 = 150
quanlity2 = "A+"
mold2 = "裤子"
Sales2 = 500

print("--------------------------------------------------")
print("-             欢迎来到衣服商城系统                   -")
print("--------------------------------------------------")
print("编号      衣服名称     价格     品质     类型      销量")
print("--------------------------------------------------")
print(id1 ,"      ",name1,"     ",price1,"     ",quanlity1,"   ",mold1,"     ",Sales1,"  " )
print(id2 ,"      ",name2,"    ",price2,"    ",quanlity2,"    ",mold2,"    ",Sales2,"  " )
print("---------------------------------------------------")
print("总销售额",(price1 * Sales1 + price2 * Sales2),"￥！")