# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# dict = {}
# for key in List:
#     dict[key] = dict.get(key, 0) + 1
# print (dict)

List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
i = 1
while i <=10:
    print(i,"相同的次数：",List.count(i))
    i += 1
