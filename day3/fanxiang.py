List = [1,2,3,4,5,6,7,8,9]
list = [1,1,1,1,1,1,1,1,1]
i = 0
k = 8
while i <=8:
    list[k] = List[i]
    i = i + 1
    k = k - 1
print("list=",list)